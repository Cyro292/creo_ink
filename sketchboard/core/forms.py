from django import forms
from .utils import get_changeable_permission_list, get_changeable_user_list, create_invite_link
from django.forms import formset_factory
from . import models
        
class AddBoardFrom(forms.ModelForm):
    
    class Meta:
        model = models.Board
        fields = ['name', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class CreateGuestUserForm(forms.Form):
    username = forms.CharField(max_length=64)

def make_change_board_permission_form(board, user_permission):
    
    class ChangeBoardPermissionForm(forms.Form):
        permission = forms.ChoiceField(choices=get_changeable_permission_list(user_permission))
    
        user = forms.ModelMultipleChoiceField(queryset=get_changeable_user_list(board, user_permission))
        
    return ChangeBoardPermissionForm

    
class InvitationLinkForm(forms.Form):
    url = forms.URLField(max_length=128, disabled=True)
    max_usages = forms.IntegerField(min_value=1, max_value=100, initial=1)
        
