from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    re_password = forms.CharField(widget=forms.PasswordInput())

    def clean_username(self):
        user_input = self.cleaned_data.get('username')
        user_is_exists = User.objects.filter(username=user_input).exists()

        if user_is_exists:
            raise forms.ValidationError("This username is exists please enter the outher username")
        
        return user_input
    
    def clean_email(self):
        email_input = self.cleaned_data.get('email')
        email_is_exists = User.objects.filter(email=email_input).exists()

        if email_is_exists:
            raise forms.ValidationError("This gmail is exists please enter the outher email")
        
        return email_input
    

class UserProfile(forms.Form):
    birth_date = forms.DateTimeField(widget=forms.DateTimeInput())
    avatar = forms.ImageField(required=False)
    city = forms.CharField(max_length=100, required=False)
    phone_number = forms.CharField(max_length=100, required=False)

