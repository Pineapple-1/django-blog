from django.forms import fields
from users.models import Profile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email: forms.EmailField(required = True)
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        

class userUpdatefrom(forms.ModelForm):
    email: forms.EmailField(required = True)
    class Meta:
        model = User
        fields = ['username','email']
        
        
class profileUpateform(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']