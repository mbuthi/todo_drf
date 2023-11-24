from rest_framework import serializers
from .models import *

class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ("id", "title", "description", "is_completed")
        