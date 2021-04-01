from rest_framework import serializers

from .models import MembersGroup, Task


class MembersGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembersGroup
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
