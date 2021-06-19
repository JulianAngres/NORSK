"""NORSK URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from users import views as user_views
from store import views as store_views
from x_app import views as x_app_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.SignUpView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/',
        auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
        name='password_reset'),
    path('password_reset_done/',
        auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
        name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('password-reset_complete/', x_app_views.password_reset_complete, name='password_reset_complete'),
    path('', include('x_app.urls')),
    path('activate/<uidb64>/<token>/', user_views.ActivateAccount.as_view(), name='activate'),
    #
    path('login/calendar/', include('store.urls', namespace='calendar')),
    #
    path('pleese_verify', x_app_views.pleese_verify, name='pleese_verify'),
    path('success_verification', x_app_views.success_verification, name='success_verification'),
    #
    path('calendar/', store_views.GoToCalendar, name='calendar'),
    path('store/', store_views.GoToCalendarResults, name='store'),
    #
    path('results/', store_views.GoToResults, name='results'),
    path('results/send_mail_plain_with_stored_file/', store_views.send_mail_plain_with_stored_file, name='plain_email'),
]
