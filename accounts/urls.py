from django.urls import path
from .views import (
    home, 
    login_user, 
    logout_user, 
    user_sign_up,
    UserPasswordResetView,
    UserPasswordResetDoneView,
    UserPasswordResetConfirmView,
    UserPasswordResetCompleteView,
    admin_panel,
    update_profile
)
urlpatterns = [
    path('', home, name='home'),
    path('accounts/login/', login_user, name='login'),
    path('accounts/logout/', logout_user, name='logout'),
    path('accounts/register/', user_sign_up, name='register'),
    path('admin_panel/', admin_panel, name='dashboard'),
    path('admin_panel/profile/edit/', update_profile, name='edit'),

    # password reset urls
    path('accounts/password_reset/', UserPasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/password_reset/confirm/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password_reset/complete/', UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]