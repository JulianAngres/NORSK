from django.urls import path
from core.views import SignUpView, ActivateAccount
from . import views
from x_app import views as x_app_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', x_app_views.loginPage, name='login'),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
    path('register/', views.SignUpView.as_view(), name='register'),
    path('pleese_verify/', views.pleese_verify, name='pleese_verify'),
    path('success_verifiation/', views.success_verification, name='success_verification'),
]