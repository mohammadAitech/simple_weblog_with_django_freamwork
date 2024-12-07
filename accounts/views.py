from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, RegisterForm, UserProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . models import Profile
from django.contrib.auth.views import (
    PasswordResetCompleteView,
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
)
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return render(request, 'index.html')

def login_user(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    form_login = LoginForm(request.POST or None)

    if form_login.is_valid():
        cd = form_login.cleaned_data
        user = authenticate(request, username=cd['username'], password=cd['password'])

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        
    else:
        form = LoginForm()
    return render(request, 'login.html', {"form":form})

@login_required
def logout_user(request):
    logout(request)
    return redirect("dashboard")

@login_required
def admin_panel(request):
    context = {
        'user' : request.user
    }
    return render(request, 'dashboard/admin.html',context)

@login_required
def update_profile(request):
    user_profile = get_object_or_404(Profile, user=request.user)
    form = UserProfile(initial={
        'birth_date':user_profile.birth_date,
        'city':user_profile.city,
        'phone_number':user_profile.phone_number,
        'avatar':user_profile.avatar
    })

    if request.method == 'POST':
        form = UserProfile(request.POST, request.FILES)
        if form.is_valid():
            birth_date = form.cleaned_data.get('birth_date')
            city = form.cleaned_data.get('city')
            phone_number = form.cleaned_data.get('phone_number')
            avatar = form.cleaned_data.get('avatar')
            user_profile.birth_date = birth_date
            user_profile.avatar = avatar
            user_profile.city = city
            user_profile.phone_number = phone_number
            user_profile.save()
            return redirect('dashboard')



    return render(request, 'dashboard/profile_dashboard_edit.html', {'form':form, 'user':request.user})

def user_sign_up(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    register_form = RegisterForm(request.POST or None)

    if register_form.is_valid():
        forms_data = register_form.cleaned_data

        User.objects.create_user(username=forms_data['username'], email=forms_data['email'], password=forms_data['password'], first_name=forms_data['first_name'], last_name=forms_data['last_name'])

        return redirect('dashboard')
    
    context = {
        "form": register_form
    }

    return render(request, 'auth/registration/register.html', context)

class UserPasswordResetView(PasswordResetView):
    template_name = 'auth/password_reset/password_reset.html'
    email_template_name = 'auth/password_reset/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')

class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'auth/password_reset/password_reset_done.html'

class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'auth/password_reset/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'auth/password_reset/password_reset_complete.html'