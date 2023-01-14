from django.db import models
from superuser.models import Department

# Create your models here.
class Tickets(models.Model):

    PRIORITY = [
        ('high' , 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]

    STATUS = [
        ('open' , 'Open'),
        ('closed', 'Closed'),
        ('on_hold' , 'On Hold'),
    ]

    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    subject = models.CharField(max_length=300)
    description = models.TextField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=300)
    phone = models.CharField(max_length=15,blank=True)
    priority = models.CharField(default='medium' , choices=PRIORITY , blank=True, max_length=200)
    status = models.CharField(default='open', choices=STATUS , blank=True, max_length=200)
    


