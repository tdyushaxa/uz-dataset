from django import forms

from users.models import Profile


class ChangeProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name','email','short_intro','bio','loacation','img')