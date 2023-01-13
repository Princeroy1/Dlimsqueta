from .models import Client
from django import forms
from django.forms.widgets import NumberInput
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class admindata(ModelForm):
    issue_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    valid_from=forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    valid_to=forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    class Meta:
        model = Client
        exclude = ('user_qr_code',)
        fields = '__all__'
class adminsignup(UserCreationForm):
    
    password1=forms.CharField( widget=forms.PasswordInput())
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat Password'
    }))
    class Meta:
        model=User
        fields=['username']