from rest_framework import serializers
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('text', 'views')

    def validate_views(self, value):
        if value != 0:
            raise serializers.ValidationError("views amount cannot be changed")
        return value
    
    def validate_text(self, value):
        if len(value) <= 0:
            raise serializers.ValidationError("message should be non-empty")
        return value
