from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='tasks'),

    path('task-list/', task_list, name='task_list'),
    path('task-detail/<str:pk>/', task_detail, name='task_detail'),
    path('task-create/', task_create, name='task_create'),
    path('task-update/<str:pk>/', task_update, name='task_update'),
    path('task-delete/<str:pk>/', task_delete, name='task_delete'),

    path('member-list/', member_list, name='member_list'),
    path('member-detail/<str:pk>/', member_detail, name='member_detail'),
    path('member-create/', member_create, name='member_create'),
    path('member-update/<str:pk>/', member_update, name='member_update'),
    path('member-delete/<str:pk>/', member_delete, name='member_delete'),
]

