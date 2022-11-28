from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name="index"),
    path("boards/", views.boards_view, name="boards"),
    path("boards/<str:key>", views.board_view, name="board"),
    path("boards/<str:key>/settings", views.board_settings_view, name="board_settings"),
    path("addBoard/", views.add_board_view, name="add_board"),
    path("invite/<str:token>", views.autheticate_via_link_view, name="invite"),
    path("accounts/createguestuser/", views.create_guest_user_view, name="create_guest_user")
]
