from typing_extensions import Required
from rest_framework import serializers
from django.contrib.auth.models import User


class RegistartionSerializer(serializers.ModelSerializer):
    ROLE = ['admin','employee']
    role = serializers.ChoiceField(choices=ROLE)
    class Meta:
        model = User
        fields = ['username','password','role']

    def validate_role(self,value):
        if value not in ['admin','employee']:
            raise serializers.ValidationError({'error': 'Given role is not defined'})
        return value


