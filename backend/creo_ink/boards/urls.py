from django.urls import path
from .views import (
    BoardListView,
    BoardMembersListView,
    BoardDetailView,
    UserSettingsUpdateView,
    CreateInviteLinkView,
    JoinBoardByLinkView,
    LeaveBoardView,
    # Other views for invite links, join codes, etc.
)

urlpatterns = [
    path('boards/', BoardListView.as_view(), name='board-list'),
    path('boards/<str:slug>/', BoardDetailView.as_view(), name='board-detail'),
    path('boards/<str:slug>/members/', BoardMembersListView.as_view(), name='board-members'),
    path('settings/', UserSettingsUpdateView.as_view(), name='user-settings'),
    path('boards/<str:slug>/invite/', CreateInviteLinkView.as_view(), name='create-invite-link'),
    path('boards/join/<str:link_token>/', JoinBoardByLinkView.as_view(), name='join-board-by-link'),
    path('leave/<str:slug>', LeaveBoardView.as_view(), name='leave-board'),
    # Other URLs for invite links, join codes, etc.
]
