from django import forms
from django.forms.widgets import TextInput


class ContactForm(forms.Form):
    full_name=forms.CharField(required=True)
    email=forms.EmailField(required=True)
    message=forms.CharField(required=True,widget=forms.Textarea,max_length=3000)