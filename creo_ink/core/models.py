from django.contrib.auth import get_user_model
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.db import models
from guardian.shortcuts import assign_perm, remove_perm

from .exceptions import (MultipleIdenticalUserException,
                         MultipleOwnerException, NoOtherUserException,
                         NoOwnerException)
from .utils import unique_slug_generator

def str_through(base, a, b):
    return [base+str(i) for i in range(a, b+1)]

def str_list(base, l):
    return [base+str(i) for i in l]

OWNER_RANK = 0
ADMIN_RANK = 1
WRITER_RANK = 2
READER_RANK = 3

# Create your models here.

MyUserModel = get_user_model()


class BoardManager(models.Manager):

    def create(self, name, owner, password, *args, **kwargs):
        board = Board(name=name, password=password, *args, **kwargs)
        board.save()
        board.set_owner(owner)

        return self


class Board(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False)
    password = models.CharField(max_length=128)
    slug = models.SlugField(max_length=12, unique=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True, null=False)
    users = models.ManyToManyField(
        to=MyUserModel, related_name="boards", through="Participation")
    elements = models.JSONField(null=True)

    objects = BoardManager()

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = unique_slug_generator(self)
        return super().save(*args, **kwargs)


    # Functions concerning users

    @property
    def owner(self):
        try:
            return self.participation_set.get(permission=Participation.OWNER).user
        except ObjectDoesNotExist:
            return None
        except MultipleObjectsReturned as exc:
            raise MultipleOwnerException from exc

    def add_user(self, user, permission=None):

        if permission is None:
            permission = Participation.READER

        if self.users.all().filter(pk=user.pk).exists():
            raise MultipleIdenticalUserException

        if permission is Participation.OWNER:
            self.set_owner(user)
            return

        Participation.objects.create(
            board=self,
            user=user,
            permission=permission)

        self.assign_user_perms(user, permission)

    def has_user(self, user):
        if self.users.all().filter(pk=user.pk).exists():
            return True

        return False


    # Functions concerning perms + access

    def has_access(self, user, min_permission=None):

        if min_permission is None:
            min_permission = Participation.READER

        if self.users.filter(pk=user.pk).exists():
            if min_permission >= self.get_permission(user=user):
                return True

        return False

    def set_permission(self, user, permission):
        """sets permission

        Args:
            user (user): user to change permission
            permission (int): permission

        Raises:
            NoOwnerException: if no other user exists who can be owner
        """

        owner = self.owner

        if user.pk is owner.pk: # Note: Should the down-grading of owners be allowed?
            if permission is not Participation.OWNER:
                try:
                    self.change_random_owner()
                except NoOtherUserException as exc:
                    raise NoOwnerException from exc

        if permission is Participation.OWNER:
            self.set_owner(user)
        else:
            participation = self.participation_set.get(user=user.pk)
            participation.permission = permission
            participation.save()
            self.assign_user_perms(user, permission)

    def assign_user_perms(self, user, permission):
        participation = self.participation_set.get(user=user.pk)
        participation.permission = permission
        participation.save()
        for perm_name, perm_desc in Participation.role_permissions['ALL']: # Remove all current permissions
            if user.has_perm(perm_name, self):
                remove_perm(perm_name, user, self)

        for perm in Participation.role_permissions[permission]: # Assign correct perms
            #print("assigning perm", perm, "to user", user.username)
            assign_perm(perm, user, self)

    def user_has_perm(self, user, permission):
        self.assign_user_perms(user, permission=self.participation_set.get(user=user.pk).permission)
        # Check if user is missing proper perms
        has_perms = user.has_perm(permission, self)
        return has_perms

    def get_permission_label(self, user):
        return self.participation_set.get(user=user.pk).get_permission_display()

    def get_permission(self, user):
        return self.participation_set.get(user=user.pk).permission


    # Functions concerning owners

    def set_owner(self, user):

        owner = self.owner

        if owner is not None:
            old_owner_participation = self.participation_set.get(user=owner.pk)
            old_owner_participation.permission = Participation.ADMIN
            old_owner_participation.save()

        try:
            user_participation = self.participation_set.get(user=user.pk)
        except Participation.DoesNotExist:
            user_participation = None

        if user_participation is None:
            Participation.objects.create(
                board=self,
                user=user,
                permission=Participation.OWNER)
        else:
            user_participation.permission = Participation.OWNER
            user_participation.save()

        self.assign_user_perms(owner, permission=Participation.ADMIN)
        self.assign_user_perms(user, permission=Participation.OWNER)

    def change_random_owner(self, depth=1, iteration=0):

        if self.users.count() <= 1:
            raise NoOtherUserException

        if depth >= len(Participation.permissions):
            raise NoOtherUserException

        if not self.participation_set.filter(permission=depth).exists():
            return self.change_random_owner(depth+1, 0)

        participation = self.participation_set.filter(permission=depth)

        try:
            participation[iteration]
        except IndexError:
            return self.change_random_owner(depth+1, 0)

        user = participation[iteration].user

        if user is self.owner:
            return self.change_random_owner(depth, iteration+1)

        self.set_permission(user, Participation.OWNER)
        return user


    # Other

    def get_absolute_url(self):
        return self.slug

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        permissions = ( # You can't set roles higher than your own, and you can't demote someone with higher role than you
            *tuple(zip(str_through('can_set_role_', OWNER_RANK, READER_RANK),
                       str_list('Allows promotion to role ', ['OWNER', 'ADMIN', 'WRITER', 'READER']))),
            *tuple(zip(str_through('can_modify_', OWNER_RANK, READER_RANK),
                       str_list('Allows modifying roles of people currently ', ['OWNER', 'ADMIN', 'WRITER', 'READER'])))
        )

class Participation(models.Model):
    OWNER = OWNER_RANK
    ADMIN = ADMIN_RANK
    WRITER = WRITER_RANK
    READER = READER_RANK

    permissions = [
        (OWNER, "Owner"),
        (ADMIN, "Admin"),
        (WRITER, "Writer"),
        (READER, "Reader"),
    ]

    role_permissions = { # Perms for each role
        READER: (),
        WRITER: (),
        ADMIN: (
            *str_through('can_set_role_', ADMIN, READER),
            *str_through('can_modify_', WRITER, READER)
        ),
        OWNER: (
            *str_through('can_set_role_', OWNER, READER),
            *str_through('can_modify_', OWNER, READER)
        ),
        'ALL': Board._meta.permissions
    }

    board = models.ForeignKey(
        Board, on_delete=models.CASCADE, blank=False, null=False)
    user = models.ForeignKey(
        MyUserModel, on_delete=models.CASCADE, blank=False, null=False)
    join_date = models.DateTimeField(auto_now_add=True)
    permission = models.IntegerField(
        choices=permissions, default=READER, blank=False, null=False)

    def delete(self, *args, **kwargs):
        if self.permission is Participation.OWNER:
            try:
                self.board.change_random_owner()
            except NoOtherUserException:
                self.board.delete()
        return super().delete(*args, **kwargs)

    class Meta:
        unique_together = [["user", "board"]]
        permissions = (
            ('owner', 'Owner'),
        )

class BoardSession(models.Model):
    user = models.ForeignKey(
        to=MyUserModel, on_delete=models.SET_NULL, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    data = models.JSONField()
