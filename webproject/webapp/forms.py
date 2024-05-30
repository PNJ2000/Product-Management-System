from django import forms
from django.contrib.auth.models import User
from .models import CustomUser, Users

class CustomForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput, required=False)
    class Meta:
        model=CustomUser
        fields=['add','dob','phone_no']
        widgets={
            'add':forms.TextInput(attrs={'class':"form-control"}),
            'dob':forms.TextInput(attrs={'class':"form-control"}),
            'phone_no':forms.TextInput(attrs={'class':"form-control"}),    
        }

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['name', 'price', 'product']
        widgets = { 'name': forms.TextInput(attrs={ 'class': 'form-control'}),
            'product': forms.TextInput(attrs={ 'class': 'form-control'}),
            'price': forms.TextInput(attrs={ 'class': 'form-control'}),
        }


def __init__(self, *args, **kwargs):
        user_instance = kwargs.pop('user_instance', None)
        super(CustomForm, self).__init__(*args, **kwargs)
        if user_instance:
            self.user_instance = user_instance
            self.fields['username'] .initial = user_instance.username
            self.fields['password'].widget.attrs['placeholder'] = 'Enter new password'








