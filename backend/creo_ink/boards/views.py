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
        board_id = self.kwargs["board_id"]
        return Participation.objects.filter(board_id=board_id)


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
        board_id = self.kwargs["board_id"]
        board = get_object_or_404(Board, pk=board_id, owner=request.user)

        link_token = generate_invite_token()
        cache_key = f"invite_link_{link_token}"

        # Store the link in cache with a timeout (e.g., 5 minutes)
        cache.set(cache_key, board_id, 300)

        return Response({"invite_link": link_token}, status=status.HTTP_201_CREATED)


class JoinBoardByLinkView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        link_token = self.kwargs["link_token"]
        cache_key = f"invite_link_{link_token}"

        board_id = cache.get(cache_key)

        if board_id is None:
            return Response(
                {"detail": "Invalid or expired link token."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        board = get_object_or_404(Board, pk=board_id)
        user = request.user

        # Automatically add the user to the board
        if not board.has_user(user):
            board.add_user(user, Participation.READER)

        return Response(
            {"message": "Successfully joined the board."}, status=status.HTTP_200_OK
        )
