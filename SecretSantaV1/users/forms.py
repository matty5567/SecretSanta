from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Profile
from django.contrib.auth.admin import UserAdmin




from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('WishListItem1', 'WishListItem2', 'WishListItem3')


class ContactForm(forms.Form):
    question = forms.CharField(widget=forms.Textarea)
