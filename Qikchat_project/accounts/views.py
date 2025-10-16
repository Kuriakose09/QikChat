from django.shortcuts import render

# Create your views here.
# import viewsets
from rest_framework import viewsets

# import local data
from .serializers import UserSerializer
from .serializers import UserprofileSerializer
from .models import Userprofile

#for registration
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions


# create a viewset
class UserprofileViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Userprofile.objects.all()
    
    # specify serializer to be used
    serializer_class = UserprofileSerializer

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer