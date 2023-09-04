from typing import Any, Dict
from django import forms
# from django.forms import ModelForm
from .models import Profile

## Inbuilt Validators in django
from django.core.validators import EmailValidator      # Validators must be given in list form
# To popup error messages
from django.core.exceptions import ValidationError
# example of custom validator and raising an error using validation error
def my_email_validator(email):
    if email.split('@')[1].split('.')[0] == 'hotmail':
        raise ValidationError("Email not acceptable")

class ContactForm(forms.Form):
    name=forms.CharField(max_length=100)
    email=forms.EmailField(validators=[EmailValidator(), my_email_validator])
    verify_email= forms.EmailField()
    message=forms.CharField(widget=forms.Textarea, max_length=256)

    def clean(self):
        cleaned_data= super().clean()
        name = cleaned_data.get('name')
        cleaned_data['email'] = cleaned_data.get('email')
        cleaned_data['verify_email'] = cleaned_data.get('verify_email')
        message = cleaned_data.get('message')

        if cleaned_data.get('email') != cleaned_data.get('verify_email'):
            raise forms.ValidationError('Email not matched')
        return cleaned_data

class ProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        # To display all fields
        fields = "__all__"
        # To display specific fields
        # fields = ['name','gender','occupation']

