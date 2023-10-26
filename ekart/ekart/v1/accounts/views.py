import datetime
import jwt

from django.shortcuts import render
from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

from v1.accounts.serializers import auth
from v1.accounts import models as acc_models

# Create your views here.

class Signup(APIView):

    def post(self, request):
        serialiser = auth.UserSerializer(data=request.data)
        serialiser.is_valid()
        serialiser.save()
        return Response(serialiser.data)
    

class LoginView(APIView):

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if not user:
            raise AuthenticationFailed("username or password incorrect")
        
        payload = {
            "id" : user.id,
            "exp" :  datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            "iat": datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, "secret", algorithm="HS256")
        print(type(token), token)

        response = Response()

        response.set_cookie(key="jwt", value=token, httponly=True)    
        response.data = {
            "jwt": token
        }

        return response
    

class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get("jwt")
        print(token)
        if not token:
            raise AuthenticationFailed
        
        payload = jwt.decode(token, "secret", algorithms=["HS256"])
        
        try:
            user = acc_models.ProjectUser.objects.get(id=payload['id'])
        except:
            raise AuthenticationFailed


        return Response(auth.UserSerializer(user).data)


class LogoutView(APIView):

    def post(self, request):

        response = Response()
        response.delete_cookie(key="jwt")

        response.data = {
            "message": "succceessfully logged out"
        } 
        
        return response
        