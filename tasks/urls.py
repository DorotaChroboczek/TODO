from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='tasks'),
    path('task-list/', task_list, name='task_list'),
    path('task-detail/<str:pk>/', task_detail, name='task_detail'),
    path('task-create/', task_create, name='task_create'),
    path('task-update/<str:pk>/', task_update, name='task_update'),
    path('task-delete/<str:pk>/', task_delete, name='task_delete'),
]
