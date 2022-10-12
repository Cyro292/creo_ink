from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from guest_user.decorators import allow_guest_user
from . import models, forms
# Create your views here.

@allow_guest_user
def index_view(request):
    return render(request, 'core/index.html')

@login_required(login_url="signin")
@require_http_methods(["POST", "GET"])
def add_board_view(request):
    form = forms.AddBoardFrom()
    if request.method == "POST":
        form = forms.AddBoardFrom(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            
            models.Board.objects.create(name=name, owner=request.user, password=password)

            return redirect('boards')
    
    return render(request, "core/addBoard.html", {'form': form})
      
@require_http_methods(["GET"])
@login_required(login_url="signin")
def boards_view(request: HttpRequest):
    board_list = []
    for board in request.user.boards.all():
        dic = {}
        dic['name'] = board.name
        dic['permission'] = board.get_permission_label(request.user)
        board_list.append(dic)
    
    return render(request, "core/boards.html", {"boards" : str(board_list)})  

@require_http_methods(["GET"])
@login_required(login_url="signin")
def board_view(request: HttpRequest, id):

    obj = get_object_or_404(request.user.boards, pk=id)
    return HttpResponse(f"worked {obj}")
    
@allow_guest_user
def invite_view(request: HttpRequest, code):
    
    return HttpResponse(code)
