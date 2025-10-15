from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser

# Create your models here.

class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pics/')
    online_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.full_name

# class User_Profile(AbstractUser):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     Full_Name = models.CharField(max_length=100)
#     Profile_picture = models.ImageField()
#     Online_status = models.BooleanField()
#     Created_date = models.DateField()