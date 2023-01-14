from django.shortcuts import render
from .models import Department
from .serializers import DepartmentSerializer
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

# Create your views here.
class CreateDepartment(APIView):

    def post(self, request:Response):

        serializer = DepartmentSerializer(data=request.data)


        if serializer.is_valid():
            serializer.save()
            return Response({'Message' : 'Department Successfully Created'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'Message' : serializer.errors},status=status.HTTP_400_BAD_REQUEST)