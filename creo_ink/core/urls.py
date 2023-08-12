from django.urls import path, include
from . import views

from rest_framework import routers

# router
router = routers.DefaultRouter()
# router.register(r'boards', views.UserBoardsViewSet)
# router.register(r'api/board-overview', views.UserBoardsViewSet)
router.register(r'api/boards-overview', views.UserBoardsViewSet,
                basename='boards-overview')

urlpatterns = [
    path('', views.index_view, name="index"),
    path("boards/", views.boards_view, name="boards"),
    path("boards/<str:slug>", views.board_view, name="board"),
    path("boards/<str:slug>/settings",
         views.board_settings_view, name="board_settings"),
    path("addBoard/", views.add_board_view, name="add_board"),
    path("invite/<str:token>", views.authenticate_via_link_view, name="invite"),
    path("accounts/createguestuser/",
         views.create_guest_user_view, name="create_guest_user"),
    path('', include(router.urls)),
    path('where-the-funny-is-at/', views.joke_view)
]
