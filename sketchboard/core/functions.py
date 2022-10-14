from . import models

def has_access(board, user, min_permission=models.Participation.OWNER):
            
    if board.users.filter(pk=user.pk).exists():
        if min_permission <= board.get_permission(user):
            return True
                  
    return False
