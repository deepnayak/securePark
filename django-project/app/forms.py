from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(ModelForm):
    class Meta: 
        model = Profile
        fields = ['name', 'contact']
        widgets = {
          'contact': forms.Textarea(attrs={'rows':2, 'cols':20}),
        }


# class VideoForm(ModelForm):
#     class Meta: 
#         model = DetectionVideo
#         fields = ['name', 'video']
        

    # def __init__(self, *args, **kwargs):
    #     initial = kwargs.get('initial', {})
    #     if hasattr(self, 'initial_values') and not kwargs.get('data'):
    #         for field_name, value in self.initial_values.items():
    #             if not getattr(kwargs.get('instance', None), field_name, None):
    #                 initial[field_name] = value
    #         kwargs.update({'initial': initial})
    #     super().__init__(*args, **kwargs)