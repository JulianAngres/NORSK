from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


#class UserRegisterForm(UserCreationForm):
#    email = forms.EmailField()

#    class Meta:
#        model = User
#        fields = ['username', 'email', 'password1', 'password2']

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True, help_text='Enter a valid email adress')

    class Meta:
        model = User
        fields = (
            'username', 
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )