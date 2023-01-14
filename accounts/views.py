from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import UserViewSerializer
from .models import Account


# Create your views here.
class UserView(generics.RetrieveAPIView):
    permission_classes = []
    serializer_class = UserViewSerializer
    queryset = Account.objects.all()