from datetime import timedelta
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import now

# Create your models here.

MyUserModel = get_user_model()
    
class BoardManager(models.Manager):
    def create(self, name, owner, password, *args, **kwargs):
        board = Board(name=name, password=password, *args, **kwargs)
        board.save()
        Participation.objects.create(board=board, user=owner, permission=Participation.OWNER)
        
        return board
    
class Board(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False)
    password = models.CharField(max_length=64)
    creation_date = models.DateTimeField(auto_now=True, null=False)
    users = models.ManyToManyField(to=MyUserModel, related_name="boards", through="Participation")
    
    objects = BoardManager()
     
    @property
    def owner(self):
        try:
            return self.participation_set.filter(permission=Participation.OWNER)
        except self.DoesNotExist:
            return None
    
    def add_user(self, user, permission=None):
        
        if permission is None:
            permission = Participation.READER
            
        if permission == Participation.OWNER:
            ValueError("cannot add new Owner")

        return Participation.objects.create(
                board=self, 
                user=user, 
                permission=permission)        
    
    def get_permission_label(self, user):
        return self.participation_set.get(user=user).get_permission_display()
    
    def get_permission(self, user):

        return self.participation_set.get(user=user).permission    
        
    def set_permission(self, user, permission):
        
        if permission > Participation.OWNER:
            
            self.participation_set.get(user=user).permission = permission
                
        elif permission is Participation.OWNER: 
            self.owner.t.get(permission=Participation.OWNER).permission = Participation.ADMIN
        
            self.participation_set.get(user=user).permission = Participation.OWNER
        else:
            raise ValueError("unknown permission " + permission)
        
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
    join_date = models.DateTimeField(auto_now=True)
    permission = models.IntegerField(choices=permissions, default=READER, blank=False, null=False)
    
    class Meta:
        unique_together = [["user", "board"]]
    