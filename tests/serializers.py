from rest_framework import serializers

from .models import *

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('id', 'title', 'details', 'created', 'due_date', 'completed')
    