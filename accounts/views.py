from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated , AllowAny
from .serializers import UserViewSerializer , SignUpSerializer
from .models import Account
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status


# Create your views here.
class UserView(generics.RetrieveAPIView):
    permission_classes = []
    serializer_class = UserViewSerializer
    queryset = Account.objects.all()


class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    permission_classes = [AllowAny]


    def post(self , request : Request):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            response = {
                'message': "User Created Successfully",
            }
            return Response(data=response,status=status.HTTP_201_CREATED)
        else:
            print('serializer is not valid')
            print(serializer.errors)
            return Response(data==serializer.errors , status=status.HTTP_400_BAD_REQUEST)