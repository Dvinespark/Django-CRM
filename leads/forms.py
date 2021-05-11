from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.forms import fields
from .models import Lead
from django.contrib.auth import get_user_model

User = get_user_model()


# This is a general type of form
class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)


# This if model form

class LeadModelForm(forms.ModelForm):
    
    class Meta:
        model = Lead
        fields = ("first_name", "last_name", "age", "agent")



class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ("username",)
        fields_classes = {'username': UsernameField}

        