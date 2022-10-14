from django import forms
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
    