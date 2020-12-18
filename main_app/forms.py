from django.forms import ModelForm
from .models import Goal
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class GoalForm(ModelForm):
    class Meta:
        model = Goal
        fields = '__all__'

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields =  ('username',)
      
    
