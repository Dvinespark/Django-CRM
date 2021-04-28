from django import forms
from .models import Lead


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
