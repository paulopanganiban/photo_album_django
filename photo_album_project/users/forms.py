from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() # default | required=True
    
    # specify which model we want to interact/edit
    class Meta:
        model = User
        # input to be shown in order 
        # User.username
        fields = ['username', 'email', 'password1', 'password2',]

class UserUpdateForm(forms.ModelForm):
    
    # specify which model we want to interact/edit
    class Meta:
        model = User
        # input to be shown in order 
        # User.username
        fields = ['first_name', 'last_name',]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image',]