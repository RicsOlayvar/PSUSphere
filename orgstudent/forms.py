from django.forms import ModelForm
from django import forms
from orgstudent.models import Organization

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = "__all__"
