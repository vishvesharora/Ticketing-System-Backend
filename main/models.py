from django.db import models
from django.contrib.auth.models import User


class Ticket(models.Model):
    STATUS_CHOICES = [('open','OPEN'),('close','CLOSE')]
    PRIORITY = [('low','LOW'),('medium','MEDIUM'),('high','HIGH')]
    title = models.CharField(max_length=40)
    status = models.CharField(choices= STATUS_CHOICES,max_length=30)
    priority = models.CharField(choices=PRIORITY,max_length=30,default='low')
    description = models.CharField(max_length=50)
    createdAt = models.DateTimeField(auto_now_add=True,verbose_name="createdAt")
    assignedTo = models.ForeignKey(User,to_field = 'username',on_delete=models.CASCADE,default = 4)

    def __str__(self) -> str:
        return self.title
    
