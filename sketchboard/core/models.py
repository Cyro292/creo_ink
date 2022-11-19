import random
from django.db import models
from django.db.models import Count
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db.models.signals import post_delete
from .exceptions import NoOwnerException, MultipleOwnerException, MultipleIdenticalUserException, NoOtherUserException
from django.forms import PasswordInput
from django.dispatch import receiver

# Create your models here.

MyUserModel = get_user_model()
  
class CustomUser(AbstractUser):
    config_set = models.ForeignKey(to=ConfigurationSet, on_delete=models.SET_DEFAULT, default=get_a_configuration_set())
    
    def get_a_configuration_set(self):
        return ConfigurationSet.objects.order_by('?').first()
    
class ConfigurationSet(models.Model):
    config = models.JSONField()
    
    def get_avarge_rating(self):
        total_rating = Judgement.objects.filter(pk=self.pk).annotate(total_rating = 'rating')
        number_of_judgements = Judgement.objects.annotate(total_users = Count('user'))
        return total_rating/number_of_judgements
    
    def create_judgement(self, user, rating):
        Judgement.objects.create(self, user, rating)
    
    def get_number_of_participents(self):
        return Judgement.objects.filter(pk=self.pk).annotate(total_users = Count('user'))
    
    def get_number_of_boards(self):
        pass
    
    def get_attr(self, attr):
        # returns the attr from Json file
        pass
    
    def set_attr(self, key, value):
        # sets an attr
        pass
    
    def get_all_attr(self):
        # returns all attr
        pass
    
class Judgement(models.Model):
    RATING = [
    (1, 'Bad'),
    (2, 'Could be better'),
    (3, 'Average'),
    (4, 'Great'),
    (5, 'Amazing'),
    ]   
    
    config_set = models.ForeignKey(to=ConfigurationSet, on_delete=models.CASCADE)
    user = models.ForeignKey(MyUserModel, on_delete=models.SET_NULL)
    rating = models.IntegerField(choices=RATING)
    creation_date = models.DateField(auto_now_add=True, null=False)
    
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
    elements = models.JSONField(null=True)
    
    objects = BoardManager()
    
    @property
    def owner(self):
        try:
            return self.participation_set.get(permission=Participation.OWNER).user
        except ObjectDoesNotExist:
            return None       
        except MultipleObjectsReturned:
            raise MultipleOwnerException
       
    def has_access(self, user, min_permission=None):

        if min_permission is None:
            min_permission = Participation.READER

        if self.users.filter(pk=user.pk).exists():
            if min_permission >= self.get_permission(user=user):
                return True
                  
        return False   
        
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
        
        if user is owner:
            try:
                self._change_random_owner()
            except NoOtherUserException:
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
    
    def _set_owner(self, user):
        
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
    
    def _change_random_owner(self, depth=1, iteration=0):
        
        if self.users.count() <= 1:
            raise NoOtherUserException
        
        if depth >= len(Participation.permissions):
            raise NoOtherUserException
    
        if not self.participation_set.filter(permission=depth).exists():
            return self._change_random_owner(depth+1, 0)
        
        participation = self.participation_set.filter(permission=depth)

        try:
            participation[iteration]
        except IndexError:
            return self._change_random_owner(depth+1, 0)
           
        
        user = participation[iteration].user

        if user is self.owner:
            return self._change_random_owner(depth, iteration+1)
        
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

@receiver(post_delete, sender=Participation)
def _handel_owner_delete(sender, instance, **kwargs):
    if instance.permission is Participation.OWNER:
        try:
            instance.board._change_random_owner()
        except NoOtherUserException:
            instance.board.delete()
    