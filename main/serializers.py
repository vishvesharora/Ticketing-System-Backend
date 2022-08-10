from dataclasses import field, fields
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import *

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class TicketCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length = 30)
    description = serializers.CharField(max_length = 100)
    assigned = serializers.CharField(max_length = 100)
    priority = serializers.ChoiceField(choices= ['low','medium','high'],default = 'low')

   

