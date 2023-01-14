from django.shortcuts import render
from .models import Department
from .serializers import DepartmentSerializer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.

class ViewAllDepartments(ReadOnlyModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAdminUser]


class CreateDepartment(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request:Request):

        serializer = DepartmentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'Message' : 'Department Successfully Created'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'Message' : serializer.errors},status=status.HTTP_400_BAD_REQUEST)


class UpdateDepartment(APIView):
    permission_classes = [IsAdminUser]
    def put(self, request:Request):

        id = request.query_params['id']

        try:
            department = Department.objects.get(id=id)
        except:
            return Response({'Message' : 'Data Not Found'} , status=status.HTTP_400_BAD_REQUEST)
        
        serializer = DepartmentSerializer(department, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'Message' : 'Department Successfully Updated'}, status=status.HTTP_200_OK)
        else:
            return Response({'Message' : serializer.errors},status=status.HTTP_400_BAD_REQUEST)
            

class DeleteDepartment(APIView):
    def get(slef, request, id):
        try:
            department = Department.objects.get(id=id)
        except:
            return Response({'Message' : 'Data Not Found'} , status=status.HTTP_400_BAD_REQUEST)
        department.delete()
        return Response({'Message' : 'Department Successfully Deleted'}, status=status.HTTP_200_OK)