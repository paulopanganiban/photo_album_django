from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() # default | required=True
    
    # specify which model we want to interact/edit
    class Meta:
        model = User
        # input to be shown in order 
        # User.username
        fields = ['username', 'email', 'password1', 'password2']