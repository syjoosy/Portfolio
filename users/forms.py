from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.shortcuts import render, redirect
from django import forms
from .models import Link as lilink
from django.contrib.auth.models import User


class Link(forms.Form):
    old = forms.CharField(widget=forms.TextInput(attrs={"class":"myfield"}))
    new = forms.CharField(widget=forms.TextInput(attrs={"class":"myfield"}))
    class Meta:
        model = lilink
        fields = ['old', 'new']

    def __init__(self, *args, **kwargs):
        super(Link, self).__init__(*args, **kwargs)



class UserOurRegistraion(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        admin_check = kwargs.pop('admin_check', False)
        super(UserOurRegistraion, self).__init__(*args, **kwargs)
        if not admin_check:
            del self.fields['password2']

    class Meta:

        model = User
        fields = ['username','email', 'password1', 'password2', ]



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileImage(forms.ModelForm):
    def __init__(self, *args, **kwards):
        super(ProfileImage, self).__init__(*args, **kwards)
        self.fields['img'].label = "Изображение профиля"

    class Meta:
        model = Profile
        fields = ['img']
