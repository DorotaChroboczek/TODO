from django.contrib import admin

from .models import *


@admin.register(MembersGroup)
class MembersGroupAdmin(admin.ModelAdmin):
    list_display = ('name_of_person', 'member')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('member', 'title',
                    'date', 'time',
                    'complete', 'created')


@admin.register(TaskBody)
class TaskBodyAdmin(admin.ModelAdmin):
    list_display = ('task', 'body')

