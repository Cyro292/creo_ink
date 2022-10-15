from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from allauth import app_settings
from guest_user.functions import maybe_create_guest_user
from .utils import has_access, generate_numbered_username, get_user_permission_label
from . import models, forms
# Create your views here.

@login_required()
def index_view(request):
    return render(request, 'core/index.html')

@login_required()
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
      
@login_required()
def boards_view(request: HttpRequest):
    board_list = []
    for board in request.user.boards.all():
        dic = {}
        dic['pk'] = board.pk
        dic['name'] = board.name
        dic['permission'] = get_user_permission_label(board=board, user=request.user)
        board_list.append(dic)
    
    return render(request, "core/boards.html", {"boards" : board_list})  

@login_required()
def board_view(request: HttpRequest, key):

    board = get_object_or_404(request.user.boards, pk=key)

    if not has_access(board=board, user=request.user):
        raise PermissionDenied()
    
    return render(request, 'core/board.html', 
            {"board":board}, 
            {'permission':get_user_permission_label(board, request.user)})
    
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
    
@login_required()
def invite_view(request: HttpRequest, code):
    return HttpResponse(str(request.user))
