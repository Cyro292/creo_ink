from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.dispatch import Signal
from django.db.models.signals import post_delete
from .exceptions import NoOwnerException, MultipleOwnerException, MultipleIdenticalUserException
from django.forms import PasswordInput

# Create your models here.

MyUserModel = get_user_model()
    
class BoardManager(models.Manager):
    def create(self, name, owner, password, *args, **kwargs):
        board = Board(name=name, password=password, *args, **kwargs)
        board.save()
        board._set_owner(owner)
        
        return self
    
class Board(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False)
    password = models.CharField(max_length=128)
    creation_date = models.DateTimeField(auto_now_add=True, null=False)
    users = models.ManyToManyField(to=MyUserModel, related_name="boards", through="Participation")
    
    objects = BoardManager()
    
    @property
    def owner(self):
        try:
            return self.participation_set.get(permission=Participation.OWNER).user
        except ObjectDoesNotExist:
            return None       
        except MultipleObjectsReturned:
            raise MultipleOwnerException
        
    def add_user(self, user, permission=None):
        
        if permission is None:
            permission = Participation.READER
        
        if self.users.all().filter(pk=user.pk).exists():
            raise MultipleIdenticalUserException
        
        if permission is Participation.OWNER:
            self._set_owner(user)
            return
    
        Participation.objects.create(
            board=self, 
            user=user, 
            permission=permission)
   
    def has_user(self, user):
        if self.users.all().filter(pk=user.pk).exists():
            return True
        
        return False
   
    def set_permission(self, user, permission):   

        owner = self.owner
        
        if user.pk is owner.pk:
            try:
                self._change_random_owner()
            except ObjectDoesNotExist:
                raise NoOwnerException
        
        if permission is Participation.OWNER:
            self._set_owner(user)
        
        else:
            participation = self.participation_set.get(user=user.pk)
            participation.permission = permission
            participation.save()
    
    def get_permission_label(self, user):
        return self.participation_set.get(user=user.pk).get_permission_display()
        
    def get_permission(self, user): 
        return self.participation_set.get(user=user.pk).permission
    
    def _delete_on_signal(self, sender, instance, **kwargs):
        self.delete()
    
    def _set_owner(self, user):
        
        owner = self.owner
        
        if owner is not None:
            old_owner_participation = self.participation_set.get(user=owner.pk)
            old_owner_participation.permission = Participation.ADMIN
            Signal.connect(post_delete, receiver=self._delete_on_signal(), sender=owner)
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
            Signal.connect(post_delete, receiver=self._delete_on_signal, sender=user)
        else:   
            user_participation.permission = Participation.OWNER
            Signal.connect(post_delete, receiver=self._delete_on_signal, sender=user)
            user_participation.save()
    
    def _change_random_owner(self, depth=1, iteration=0):
        
        if self.users.count() <= 1:
            raise ObjectDoesNotExist
        
        if depth >= len(Participation.permissions):
            raise ObjectDoesNotExist
    
        if not self.participation_set.filter(permission=depth).exists():
            self._change_random_owner(depth+1, 0)
        
        participation = self.participation_set.filter(permission=depth)

        try:
            participation[iteration]
        except IndexError:
            self._change_random_owner(depth+1, 0)
           
        
        user = participation[iteration].user

        if user.pk is self.owner.pk:
            self._change_random_owner(depth, iteration+1)
        
        self.set_permission(user, Participation.OWNER)
        return user
            
    def __str__(self) -> str:
        return f"{self.name}"

class Participation(models.Model):
    OWNER = 0
    ADMIN = 1
    WRITER = 2
    READER = 3
    
    permissions = [
        (OWNER, "Owner"),
        (ADMIN, "Admin"),
        (WRITER, "Writer"),
        (READER, "Reader"),
    ]

    board = models.ForeignKey(Board, on_delete=models.CASCADE, blank=False, null=False)
    user = models.ForeignKey(MyUserModel, on_delete=models.CASCADE, blank=False, null=False)
    join_date = models.DateTimeField(auto_now_add=True)
    permission = models.IntegerField(choices=permissions, default=READER, blank=False, null=False)
    
    class Meta:
        unique_together = [["user", "board"]] 
