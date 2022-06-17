#from attr import attr, attrs, fields
from django import forms
#from matplotlib import widgets
from .models import User
#from django.core import validator



class studentRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','password']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'})
        }
