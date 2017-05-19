from django import forms
from django.contrib.auth.models import User
from models import Game

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')
class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('appid', 'name','version', 'company', 'news')


