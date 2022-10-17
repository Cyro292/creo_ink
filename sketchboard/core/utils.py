import random

from . import app_settings, models
from django.core.cache import cache
import secrets

def has_access(board, user, min_permission=models.Participation.OWNER):

    if board.users.filter(pk=user.pk).exists():
        if min_permission <= board.get_permission(user=user):
            return True
                  
    return False   

def generate_numbered_username(username, user, iteration=0) -> str:

    digits = 3 + int(iteration/5)
    number = random.randint(1, (10 ** digits) - 1)
    new_username = f"{username}#G{number}"
    
    if models.get_user_model().objects.filter(username=new_username).exists():        
        return generate_numbered_username(username, user, iteration+1)
    
    user.username = new_username
    user.save()
        
    return user

def get_changeable_permission_list(user_permission):
    return list(filter(lambda t: t[0] >= user_permission, models.Participation.permissions))
    
def get_changeable_user_list(board, user_permission):
    user_access_permissions = get_changeable_permission_list(user_permission)
    
    #Something like this
    
    q = board.participation_set.all().filter(
        permission__in=[p[0] for p in user_access_permissions]).values_list('user')
    
    users = board.users.all().filter(id__in=q)
        
    return users

def get_invite_data(token=None):
    if token is None:
        token = secrets.token_urlsafe(nbytes=32)
        
    link = f"http://127.0.0.1:8000/invite/{token}"
    return {"link":link, "token":token}

def create_invite_link(board, token, **kwargs):
    cache.set(key=token, value={"board": board, **kwargs}, timeout=app_settings.CORE_INVITE_LINK_MAX_AGE)
    