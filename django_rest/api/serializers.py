from rest_framework import serializers

from models import Task
from models import Info


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('title', 'description', 'completed')


class InfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Info
        fields = ('student_id', 'student_name', 'description')
