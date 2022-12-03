from django.core.cache import cache
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpRequest
from guest_user.functions import maybe_create_guest_user
from allauth import app_settings
from .utils import generate_numbered_username, get_invite_token, get_invite_link, create_invite_link, get_redirect_value
from .exceptions import NoOwnerException
from .models import Board
from . import models, forms

from .serializers import BoardSerializer
from rest_framework import viewsets

from json import dumps

# DRF
class BoardViewSet(viewsets.ModelViewSet):
        queryset = Board.objects.all()
        serializer_class = BoardSerializer

# Create your views here.
@login_required
def index_view(request):
    return render(request, 'core/index.html')

@login_required
def add_board_view(request):
    form = forms.AddBoardFrom()
    if request.method == "POST":
        form = forms.AddBoardFrom(request.POST)
        
        
        
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            
            models.Board.objects.create(name=name, owner=request.user, password=password)

            return redirect('boards')
    
    return render(request, "core/add_board.html", {'form': form})
      
@login_required
def boards_view(request):
    board_list = []
    for board in request.user.boards.all():
        dic = {}
        dic['pk'] = board.pk
        dic['name'] = board.name
        dic['permission'] = board.get_permission_label(user=request.user)
        board_list.append(dic)
    
    return render(request, "core/boards.html", {"boards" : board_list})  

@login_required
def board_view(request, key):

    board = get_object_or_404(request.user.boards, pk=key)

    if not board.has_access(user=request.user):
        raise PermissionDenied()
    
    user_permission = board.get_permission_label(user=request.user)

    key_py_to_json = dumps(board.pk)
    return render(request, 'core/board.html', 
            {"board":board, "permission":user_permission, "key":key_py_to_json})
    
@login_required
def board_settings_view(request, key):
    
    board = get_object_or_404(request.user.boards, pk=key)
    invite_token = get_invite_token()
    invite_form = forms.make_create_invitaion_link_form(invite_token)()
    user_permission = board.get_permission(user=request.user)          
    change_user_permission_form = forms.make_change_board_permission_form(board, user_permission)()
    
    if request.method == "POST":
        if 'permission' in request.POST:
            user_permission = board.get_permission(user=request.user)
            change_user_permission_form = forms.make_change_board_permission_form(board, user_permission)(request.POST)
            
            if change_user_permission_form.is_valid():
                target_user = change_user_permission_form.cleaned_data['user'][0]
                target_permission = int(change_user_permission_form.cleaned_data['permission'])
                
                if not board.has_access(user=request.user, min_permission=models.Participation.ADMIN):            
                    messages.info(request, "you have to be at least admin in order to change permissions")
                    
                if not target_permission >= user_permission:
                    messages.info(request, "you are not allowed to set higher positions then yourself")
                    
                try:
                    board.set_permission(user=target_user, permission=target_permission)
                except NoOwnerException:
                    messages.info(request, "You can not set permission if you are the only Owner") 
        
        if 'max_usages' in request.POST:
            invite_form = forms.make_create_invitaion_link_form(invite_token)(request.POST)
            
            if invite_form.is_valid():
                max_usages = invite_form.cleaned_data['max_usages']
                url = invite_form.cleaned_data['url']
                token = get_invite_token(link=url)
                create_invite_link(board=board, token=token, max_usages=max_usages)
        
    
    
    content = {}
    content['board'] = board
    content["change_user_permission_form"] = change_user_permission_form
    content['invite_form'] = invite_form
    
    return render(request, "core/board_settings.html", content)
    
def create_guest_user_view(request: HttpRequest):
    
    form = forms.CreateGuestUserForm()

    
    redirect_field_name = 'next'
    redirect_field_value = get_redirect_value(request)
    
    if request.method == "POST":
        form = forms.CreateGuestUserForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            maybe_create_guest_user(request)
            generate_numbered_username(username, request.user)
            redirect_field_value = get_redirect_value(request)

            if redirect_field_value:
                return redirect(redirect_field_value)
            return redirect('index')
        
    
    return render(request, "core/create_guest_user.html", 
            {'form':form, 
            'login_url':app_settings.LOGIN_REDIRECT_URL, 
            'redirect_field_value':redirect_field_value,
            'redirect_field_name':redirect_field_name})

@login_required(login_url="create_guest_user")
def authenticate_via_link_view(request, token):
    
    data = cache.get(token)
    if data is None:
        return HttpResponse("Link invalid/expired")
    
    board = data['board']
    
    if board.has_user(request.user):
        return HttpResponse(f"{request.user} is already member of {board.name}(board))")
        
    board.add_user(request.user)
    
    if 'max_usages' in data.keys():
        data['max_usages'] -= 1
        
        if data['max_usages'] > 0:
            cache.set(token, data)
        else:
            cache.delete(token) 
    else:    
        cache.delete(token)
    
    return HttpResponse("Nice")
