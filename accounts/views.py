from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.serializers import AccountSerializer


class UserRegister(APIView):
    def post(self, request):
      
        data = request.data

        if User.objects.filter(username=data["username"]).exists():
            return Response({"message": "User already exists"}, status=status.HTTP_409_CONFLICT)

        user = User.objects.create_user(**data)
        serializer = AccountSerializer(user)
        response = {**serializer.data, "is_superuser": user.is_superuser, "is_staff": user.is_staff}
        
        return Response(response, status=status.HTTP_201_CREATED)
    


class UserLogin(APIView):
    def post(self, request):
      
        data = request.data
        user = authenticate(username=data["username"], password=data["password"])
        if user:
            
            token = Token.objects.get_or_create(user=user)[0]
            
            return Response({"token": token.key})
        else:
            return Response({"message": "You are not registered, please create an account."}, status=status.HTTP_401_UNAUTHORIZED)
        

    

