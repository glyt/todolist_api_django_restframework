from rest_framework import serializers
from todo.models import Todo


# Retrieve/Update/Delete/Destroy
class TodoSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    datecompleted = serializers.ReadOnlyField()

    class Meta:
        model = Todo
        fields = ['id', 'title', 'memo', 'created', 'datecompleted', 'important']


# Complete
class TodoCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id']
        read_only_fields = ['title', 'memo', 'created', 'datecompleted', 'important']