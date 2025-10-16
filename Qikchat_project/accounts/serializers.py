from django.contrib.auth.models import User
# import serializer from rest_framework
from rest_framework import serializers
# import model from models.py
from .models import Userprofile

# Create a model serializer 
class  UserprofileSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Userprofile
        fields = ('user','full_name', 'profile_picture','online_status', 'created_at')

# For creating users with passwords
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}