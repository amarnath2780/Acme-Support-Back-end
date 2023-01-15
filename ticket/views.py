from django.shortcuts import render
from .models import Tickets
from .serializers import TicketSerializer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from accounts.models import Account

# Create your views here.

class AdminTicketView(ReadOnlyModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Tickets.objects.all()
    serializer_class = TicketSerializer



class CreateTicketsView(APIView):
    permission_classes =[]
    def post(self,request:Request):

        serializer = TicketSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'Message' : 'Department Successfully Created'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'Message' : serializer.errors},status=status.HTTP_400_BAD_REQUEST)

class UpdateTicketView(APIView):
    permission_classes = []
    def put(self,request:Request,id):
        try:
            ticket = Tickets.objects.get(id=id)
        except:
            return Response({'Message' : 'Data Not Found'} , status=status.HTTP_400_BAD_REQUEST)
        
        serializer = TicketSerializer(ticket , data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'Message' : 'Ticket Successfully Updated'}, status=status.HTTP_200_OK)
        else:
            return Response({'Message' : serializer.errors},status=status.HTTP_400_BAD_REQUEST)

class UserTicketView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request:Request,id):

        user = Account.objects.get(id=id)
        email = user.email
        try:
            ticket = Tickets.objects.filter(email=email)
        except:
            return Response({'Message' : 'Data Not Found'} , status=status.HTTP_400_BAD_REQUEST)
        
        serializer = TicketSerializer(ticket , many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
