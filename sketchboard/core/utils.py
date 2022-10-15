from django.core.exceptions import ObjectDoesNotExist
from .exceptions import NoOwnerException
import random
from . import models

def has_access(board, user, min_permission=models.Participation.OWNER):
            
    board = _get_object(models.Board, board)
    user = _get_object(models.get_user_model(), user)

    if board.users.filter(pk=user.pk).exists():
        if min_permission <= get_user_permission(board=board, user=user):
            return True
                  
    return False

def add_user_to_board(board, user, permission=models.Participation.READER):
    
    board = _get_object(models.Board, board)
    user = _get_object(models.get_user_model(), user)
    
    if permission is models.Participation.OWNER:
        old_owner_participation = board.participation_set(board=board, user=user)
        old_owner_participation.permission = models.Participation.ADMIN
        
   
    return models.Participation.objects.create(
        board=board, 
        user=user, 
        permission=permission)
   
def set_user_permission(board, user, permission):
    
    board = _get_object(models.Board, board)
    user = _get_object(models.get_user_model(), user)
    
    if user is board.owner:
        try:
            _change_random_owner(board)
        except ObjectDoesNotExist:
            raise NoOwnerException()
    
    if permission is models.Participation.OWNER:
        old_owner_participation = board.participation_set(board=board, user=board.owner)
        old_owner_participation.permission = models.Participation.ADMIN
        
    return models.Participation.objects.create(
            board=board,
            user=user,
            permission=models.Participation.OWNER
    )
    
def get_user_permission_label(board, user):
    return board.participation_set.get(user=user).get_permission_display()
    
def get_user_permission(board, user):
    return board.participation_set.get(user=user).permission     

def _get_object(model, key):
    if isinstance(key, int):
        key = model.objects.get(pk=key)
        
    return key

def _change_random_owner(board, depth=0, iteration=0):
    
    if not board.participation_set.filter(permission=depth).exists():
        raise ObjectDoesNotExist()
    
    users = board.participation_set.filter(permission=depth)

    if not users[iteration].exists():
        _change_random_owner(board, depth+1, 0)
    
    user = users[iteration]

    if user is board.owner:
        _change_random_owner(board, depth, iteration+1)
    
    set_user_permission(board, user, models.Participation.OWNER)
    return user

def generate_numbered_username(username, user, iteration=0) -> str:

    digits = 3 + int(iteration/5)
    number = random.randint(1, (10 ** digits) - 1)
    new_username = f"{username}#G{number}"
    
    if models.get_user_model().objects.filter(username=new_username).exists():        
        return generate_numbered_username(username, user, iteration+1)
    
    user.username = new_username
    user.save()
        
    return user
