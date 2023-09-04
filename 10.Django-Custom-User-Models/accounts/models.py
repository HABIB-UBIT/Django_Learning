from django.db import models
from django.contrib.auth.models import AbstractUser    ### It is same a UserModel which is in-built in django but in models file we name is as an AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    Gender_Choices=[
    ('M', 'Male'),
    ('F', 'Female')
]
    gender= models.CharField(max_length=1,choices=Gender_Choices)
