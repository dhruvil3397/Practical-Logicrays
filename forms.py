from django import forms
from .models import Get

class ContactForm(forms.ModelForm):
    class Meta:
        model = Get
        fields = ["name","email","mobile"]