from django import forms
from django.forms import ModelForm
from .models import User


class StudentRegistration(ModelForm):

    class Meta:
        model = User
        fields = ['name','email','password']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','id':'nameid'}),
            'email':forms.EmailInput(attrs={'class':'form-control','id':'emailid'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','id':'passwordid'}),
        }