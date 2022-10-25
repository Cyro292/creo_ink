from django import forms
from .utils import get_lower_permission_list
from . import models
        
class AddBoardFrom(forms.ModelForm):
    
    class Meta:
        model = models.Board
        fields = ['name', 'password']

class CreateGuestUserForm(forms.Form):
    username = forms.CharField(max_length=64)

def make_change_board_permission_form(board, user_permission):
    
    class ChangeBoardPermissionForm(forms.Form):
        permission = forms.ChoiceField(choices=get_lower_permission_list(user_permission))
    
        user = forms.ModelMultipleChoiceField(queryset=board.users.all())
        
    return ChangeBoardPermissionForm
    
class InvitationLinkForm(forms.Form):
    url = forms.URLField(max_length=128, widget=forms.TextInput(attrs={'readonly': True}))
    max_usages = forms.IntegerField(min_value=1, max_value=100, initial=1)
        
