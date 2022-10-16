from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from guest_user.functions import maybe_create_guest_user
from django.core.cache import cache
from allauth import app_settings
from .utils import has_access, generate_numbered_username, create_invite_link
from .exceptions import NoOwnerException
from . import models, forms
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

    if not has_access(board=board, user=request.user):
        raise PermissionDenied()
    
    user_permission = board.get_permission_label(user=request.user)
    
    return render(request, 'core/board.html', 
            {"board":board, "permission":user_permission})
    
@login_required
def board_settings_view(request, key):
    
    board = get_object_or_404(request.user.boards, pk=key)

    
    if request.method == "POST":
        user_permission = board.get_permission(user=request.user)
        change_user_permission_form = forms.make_change_board_permission_form(board, user_permission)(request.POST)
        
        if form.is_valid():
            user_pk = form.cleaned_data['user'][0]
            permission = int(form.cleaned_data['permission'])
            
            try:
                board.set_permission(user_pk, permission)
            except NoOwnerException:
                messages.info(request, "You are not able to have no Owner")
      
    user_permission = board.get_permission(user=request.user)          
    change_user_permission_form = forms.make_change_board_permission_form(board, user_permission)()
    invite_form = forms.make_invitation_link_form(board)()
    
    content = {}
    content['board'] = board
    content["change_user_permission_form"] = change_user_permission_form
    content['invite_form'] = invite_form
    
    return render(request, "core/board_settings.html", content)
    
def create_guest_user_view(request):
    form = forms.CreateGuestUserForm()
    
    if request.method == "POST":
        form = forms.CreateGuestUserForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            maybe_create_guest_user(request)
            generate_numbered_username(username, request.user)
            
            return redirect('index')
        
    return render(request, "core/create_guest_user.html", {'form':form, 'login_url': app_settings.LOGIN_REDIRECT_URL})
    
def invite_view(request: HttpRequest, code):
    return HttpResponse("")

@login_required
def autheticate_via_link_view(request, token):
    board = cache.get(token)
    if board is None:
        return HttpResponse("Link invalid/expired")
    
    print(board.users.all(), request.user)
    
    
    try:
        board.add_user(request.user)
        cache.delete(token)
    except:
        return HttpResponse(f"same user {request.user}")
        
    
    return HttpResponse("Nice")
