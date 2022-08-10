from encodings import search_function
from fileinput import close
from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser

# Create your views here.

class AllTicket(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

class TicketList(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'priority','title']
    permission_classes = [IsAuthenticated]

class TicketDelete(generics.DestroyAPIView,mixins.CreateModelMixin):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAdminUser]

    def get_object(self):
        tickets = self.get_queryset()
        ticketid = self.request.data.get('ticketID')
        obj = tickets.get(id = ticketid )
        return obj

@api_view(['POST'])
@permission_classes([IsAdminUser])
def delete_ticket(request):
    ticketid = request.data.get('ticketID')
    obj = Ticket.objects.get(id = ticketid)

    if obj:
        obj.delete()
        return Response(status= status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])  
@permission_classes([IsAuthenticated])  
def ticket_close(request):
    ticketid = request.data.get('ticketID')
    obj = Ticket.objects.get(id = ticketid)
    user = request.user
    ticketAssigned = obj.assignedTo
    if user.is_staff or user == ticketAssigned:
        obj.status = 'close'
        obj.save()
        return Response({"message": "Ticket succesfully closed"},status= status.HTTP_200_OK)
    else:
        return Response({"message": "You arent Authorized for this"},status = status.HTTP_401_UNAUTHORIZED)

    


@api_view(['POST']) 
@permission_classes([IsAdminUser])   
def ticket_create(request):
    serializer = TicketCreateSerializer(data= request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        title = data['title']
        descrp = data['description']
        assign = data['assigned']
        user = User.objects.get(username = assign)
        priority = data['priority']
        ticket = Ticket(title = title,status = 'open',description = descrp,assignedTo = user,priority = priority)
        ticket.save()
        resp = {'id': ticket.id}
        return Response(resp)
    else:
        return Response(serializer.errors)





 




    

    
    

