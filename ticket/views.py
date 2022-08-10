
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializers import RegistartionSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def register(request):
    serializer = RegistartionSerializer(data = request.data) 
    if serializer.is_valid(raise_exception=True):
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        role = serializer.validated_data['role']
        data = {}
        user = None
        if role == 'admin':
            user = User(username = username,is_staff = True)
        else:
            user = User(username = username)
            
        user.set_password(password)
        user.save()
        token = Token.objects.get(user = user).key
        data['token'] = token
        data['username'] = username
        data['role'] = role
        return Response(data)
    
    else:
        return Response(serializer.errors)


