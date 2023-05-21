from django import forms
from .models import *


class Myreg(forms.ModelForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=AuthMain
        fields='__all__'

class Mylogin(forms.Form):
    username=forms.CharField(required=True)
    password=forms.CharField(required=True,widget=forms.PasswordInput)