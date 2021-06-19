from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.GoToCalendar, name='GoToCalendar'),
    #
    path('store/', views.GoToCalendarResults, name='GoToCalendarResults'),
    #
    path('results/', views.GoToResults, name='results'),
    path('results/send_mail_plain_with_stored_file/', views.send_mail_plain_with_stored_file, name='plain_email'),
]