from django.contrib import admin
from main.models import Ticket
# Register your models here.
class TicketAdmin(admin.ModelAdmin):
    readonly_fields = ('createdAt',)



admin.site.register(Ticket,TicketAdmin)


