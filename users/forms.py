from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import Profile


class ChangeProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name','email','short_intro','bio','loacation','img')




