from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated , AllowAny
from .serializers import UserViewSerializer , SignUpSerializer
from .models import Account
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from django.contrib.auth import authenticate
from .token import create_jwt_pair_tokens
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet

# Create your views here.
class UserView(generics.RetrieveAPIView):
    permission_classes = []
    serializer_class = UserViewSerializer
    queryset = Account.objects.all()

class AllUsersView(ReadOnlyModelViewSet):
    queryset  = Account.objects.all()
    serializer_class = UserViewSerializer

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


class LoginView(APIView):
    permission_classes =  [AllowAny]

    def post(self , request:Request):
        email = request.data.get('email')
        password = request.data.get('password') 
        user = authenticate(request, email=email, password=password)

        if user is not None:
            if user.is_verified == True:
                tokens = create_jwt_pair_tokens(user) 

                response = {
                    "message": "Login successfull",
                    "token": tokens,
                    "user" : {
                        "user_id":user.id,
                        "email":user.email,
                        "role":user.role,
                    }
                } 
                return Response(data=response, status=status.HTTP_200_OK)
            else:
                response = {
                    "message": "User is not Verified",
                } 
                return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={"message": "Invalid email or password!"}, status=status.HTTP_400_BAD_REQUEST)



class ViewUserView(APIView):

    def get(self,request:Request , id):
        
        try:
            user = Account.objects.get(id=id)
        except:
            return Response({'Message' : 'Data Not Found'} , status=status.HTTP_400_BAD_REQUEST)
        
        serializer = UserViewSerializer(user, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
