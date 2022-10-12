from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index_view, name="index"),
    path("board/<str:id>", views.board_view, name="board"),
    path("boards", views.boards_view, name="boards"),
    path("addBoard/", views.add_board_view, name="add_board"),
    path("invite/<str:code>", views.invite_view, name="invite"),
]
