from django.urls import path

from user.views import *

app_name = 'user'
urlpatterns = [
    path('index', index, name='index'),
    path('login', login, name='login'),
    path('user', user, name='user'),
    path('contact', contact, name='contact'),
    path('my-system', mySystem, name='my-system'),
    path('single-course', singleCourse, name='single-course'),
]