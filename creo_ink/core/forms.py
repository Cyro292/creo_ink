from django import forms
from .utils import get_lower_permission_list, get_invite_link
from django.contrib.auth.hashers import make_password
from . import models


class BoardForm(forms.ModelForm):

    class Meta:
        model = models.Board
        fields = ['name', 'password']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        self.cleaned_data['password'] = make_password(password)
        return self.cleaned_data['password']


class CreateGuestUserForm(forms.Form):
    username = forms.CharField(max_length=64)


def make_change_board_permission_form(board, user_permission):

    class ChangeBoardPermissionForm(forms.Form):
        permission = forms.ChoiceField(
            choices=get_lower_permission_list(user_permission))

        user = forms.ModelMultipleChoiceField(queryset=board.users.all())

    return ChangeBoardPermissionForm


def make_create_invitaion_link_form(init_token):
    class InvitationLinkForm(forms.Form):
        url = forms.URLField(max_length=128, widget=forms.TextInput(
            attrs={'readonly': 'readonly'}), initial=get_invite_link(token=init_token))
        max_usages = forms.IntegerField(min_value=1, max_value=100, initial=1)

    return InvitationLinkForm
