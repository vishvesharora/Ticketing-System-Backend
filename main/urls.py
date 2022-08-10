


from django.urls import path

from main.views import *

urlpatterns = [
   
    path('',TicketList.as_view() ),
    path('all',AllTicket.as_view()),
    path('delete',delete_ticket),
    path('markAsClosed',ticket_close),
    path('new',ticket_create),
]
