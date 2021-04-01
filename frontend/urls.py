from django.urls import path

from .views import *

app_name = 'frontend'

urlpatterns = [
    path('', user_list, name='user_list'),
]
