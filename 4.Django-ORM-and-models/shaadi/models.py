from typing import Iterable, Optional
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
fs= FileSystemStorage(settings.MEDIA_ROOT)

# Create your models here.
class Profile(models.Model):
    gender_choices=[
        ('M','Male'),
        ('F','Female'),
    ]

    name=models.CharField(max_length=100,default='Unnamed')
    profile_pic=models.ImageField(null=True,blank=True)
    age=models.IntegerField()
    gender=models.CharField(max_length=1, choices=gender_choices)
    occupation=models.CharField(max_length=100,null=True,blank= True)
    birth_date=models.DateField(null=True)
    is_married=models.BooleanField(default=False)
    email=models.EmailField(unique=True,null=True)

    # hm yahan yeh chahty k jb b koi data save ho to printf ka msg console pe print hojaye
    def save(self, *args, **kwargs):
        print(f"Data updated for {self.name}")
        super().save(*args, **kwargs)

    # jb hm ne apni profile class bnai to data save krany pe profileobject(1) likha arha tha us ki jaga agr hmaein bndy ka name chahiye to yeh karein gy
    def __str__(self):
        return self.name