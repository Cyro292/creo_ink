import random

from . import app_settings, models
from django.core.cache import cache
import secrets

def generate_numbered_username(username, user, iteration=0) -> str:

    digits = 3 + int(iteration/5)
    number = random.randint(1, (10 ** digits) - 1)
    new_username = f"{username}#{number}"
    
    if models.get_user_model().objects.filter(username=new_username).exists():        
        return generate_numbered_username(username, user, iteration+1)
    
    user.username = new_username
    user.save()
        
    return user

def get_lower_permission_list(user_permission):
    return list(filter(lambda t: t[0] >= user_permission, models.Participation.permissions))

def get_invite_data(token=None):
    if token is None:
        token = secrets.token_urlsafe(nbytes=32)
        
    link = f"http://127.0.0.1:8000/invite/{token}"
    return {"link":link, "token":token}

def create_invite_link(board, token, **kwargs):
    if '/' in token:
        token = token.rsplit('/', 1)[-1]
        
    cache.set(key=token, value={"board": board, **kwargs}, timeout=app_settings.CORE_INVITE_LINK_MAX_AGE)
    
def get_redirect_value(request, parm='next'):
    return request.GET.get(parm) or request.POST.get(parm)
