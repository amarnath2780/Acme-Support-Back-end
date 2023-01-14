from django.contrib import admin
from .models import Tickets

# Register your models here.

@admin.register(Tickets)
class TicketsAdmin(admin.ModelAdmin):
    list_display = ['id','subject','name', 'email', 'priority']