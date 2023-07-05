from django.urls import path, include
from . import views

from rest_framework import routers

# router
router = routers.DefaultRouter()
# router.register(r'api/boards-overview', views.UserBoardsViewSet, basename='boards-overview')

urlpatterns = [
    path('', views.index_view, name="index"),
    path("boards/", views.boards_view, name="boards"),
    path("boards/<str:slug>", views.board_view, name="board"),
    path("boards/<str:slug>/settings", views.board_settings_view, name="board_settings"),
    path("addBoard/", views.add_board_view, name="add_board"),
    path("invite/<str:token>", views.authenticate_via_link_view, name="invite"),
    path("accounts/createguestuser/", views.create_guest_user_view, name="create_guest_user"),
    path('api/personal/user/', views.UserDetailView.as_view(), name='personal-user'),
    path('api/board/<str:slug>/users/', views.BoardUsersListView.as_view(), name='board-users'),
    path('api/board/<str:slug>/info/', views.BoardDetailView.as_view(), name='board-info'),
    path('api/board/<str:slug>/', views.BoardUpdateView.as_view(), name='board-update'),
    path('api/board/<str:slug>/users/<str:username>/', views.BoardAdministerUsersView.as_view(), name='board-administer-users'),
    path('api/board/<str:slug>/users/<str:username>/kick/', views.BoardKickUserView.as_view(), name='board-kick-user'),
    # Add the remaining URL paths for other views
    path('api/', include(router.urls)),
]
