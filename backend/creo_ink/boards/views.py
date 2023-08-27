from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import Http404
from django.core.cache import cache
from django.shortcuts import get_object_or_404
from rest_framework import status
from .models import Board, Participation
from .serializers import (
    BoardSerializer,
    BoardMembershipSerializer,
    UserSettingsUpdateSerializer,
    JoinBoardSerializer,
    ParticipationStatusSerializer,
)
from .utils import generate_invite_token


class BoardListView(ListCreateAPIView):
    serializer_class = BoardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Board.objects.filter(users=self.request.user)


class BoardMembersListView(ListAPIView):
    serializer_class = BoardMembershipSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        slug = self.kwargs["slug"]
        return Participation.objects.filter(slug=slug)


class BoardDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = BoardSerializer
    # is board owner or admin
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Board.objects.filter(users=self.request.user)


class UserSettingsUpdateView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSettingsUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.participation_set.all()


class LeaveBoardView(UpdateAPIView):
    serializer_class = ParticipationStatusSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        slug = self.kwargs["slug"]
        return Participation.objects.filter(board__slug=slug, user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(status=Participation.INACTIVE)

    def dispatch(self, request, *args, **kwargs):
        # Check if a board with the given slug exists
        slug = self.kwargs["slug"]
        try:
            Board.objects.get(slug=slug)
        except Board.DoesNotExist:
            raise Http404("Board not found")

        return super().dispatch(request, *args, **kwargs)


class CreateInviteLinkView(CreateAPIView):
    serializer_class = JoinBoardSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        slug = self.kwargs["slug"]
        board = get_object_or_404(Board, slug=slug, owner=request.user)

        link_token = generate_invite_token()
        cache_key = f"invite_link_{link_token}"

        # Store the link in cache with a timeout (e.g., 5 minutes)
        cache.set(cache_key, slug, 300)

        return Response({"invite_link": link_token}, status=status.HTTP_201_CREATED)


class JoinBoardByLinkView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        link_token = self.kwargs["link_token"]
        cache_key = f"invite_link_{link_token}"

        slug = cache.get(cache_key)

        if slug is None:
            return Response(
                {"detail": "Invalid or expired link token."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        board = get_object_or_404(Board, slug=slug)
        user = request.user

        # Automatically add the user to the board
        if not board.has_user(user):
            board.add_user(user, Participation.READER)

        return Response(
            {"message": "Successfully joined the board."}, status=status.HTTP_200_OK
        )


def board_settings_view(request, slug):

    board = get_object_or_404(request.user.boards, slug=slug)
    invite_token = get_invite_token()
    invite_form = forms.make_create_invitaion_link_form(invite_token)()
    user_permission = board.get_permission(user=request.user)
    change_user_permission_form = forms.make_change_board_permission_form(
        board, user_permission)()
    
    if request.method == "POST":
        if 'permission' in request.POST:
            change_user_permission_form = forms.make_change_board_permission_form(
                board, user_permission)(request.POST)
            
            if change_user_permission_form.is_valid(): # Check validity of form
                target_user = change_user_permission_form.cleaned_data['user'][0]
                target_permission = int(
                    change_user_permission_form.cleaned_data['permission'])
                
                if board.user_has_perm(request.user, 'can_set_role_'+str(target_permission)): # Check user's ability to set role
                    if board.user_has_perm(request.user, 'can_modify_'+str(board.get_permission(target_user))): # Check user's ability to modify current role
                        try:
                            board.set_permission(
                                user=target_user,
                                permission=target_permission
                            )
                        except NoOwnerException:
                            messages.info(
                                request, "You can not set permissions if you are the only user"
                            )
                    else:
                        messages.info(
                            request, "You are not allowed to modify permissions of your superiors!"
                        )
                else:
                    messages.info(request, "You do not have the necessary permissions!")
        
        if 'max_usages' in request.POST:
            invite_form = forms.make_create_invitaion_link_form(
                invite_token)(request.POST)

            if invite_form.is_valid():
                max_usages = invite_form.cleaned_data['max_usages']
                url = invite_form.cleaned_data['url']
                token = get_invite_token(link=url)
                create_invite_link(board=board, token=token,
                                   max_usages=max_usages)
        
        return board_view(request, slug)

    content = {}
    content['board'] = board
    content["change_user_permission_form"] = change_user_permission_form
    content['invite_form'] = invite_form

    return render(request, "core/board_settings.html", content)
