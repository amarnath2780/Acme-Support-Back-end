from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=200,unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)