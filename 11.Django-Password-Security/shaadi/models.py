from typing import Iterable, Optional
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
fs= FileSystemStorage(settings.MEDIA_ROOT)

# Create your models here.
class Religion(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name 
    
class Sect(models.Model):
    name=models.CharField(max_length=100)
    religion=models.ForeignKey(Religion, on_delete=models.CASCADE, related_name='sects')
    def __str__(self):
        return self.name 
    
class Caste(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Hobby(models.Model):
    name=models.CharField(max_length=100)
    class Meta:
        verbose_name_plural="hobbies"
    def __str__(self):
        return self.name

class FatherProfile(models.Model):
    name=models.CharField(max_length=100)
    occupation=models.CharField(max_length=100,null=True,blank= True)
    def __str__(self):
        return self.name
    
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
    religion=models.ForeignKey(Religion, on_delete=models.CASCADE, related_name='profiles',null=True)
    sect=models.ForeignKey(Sect, on_delete=models.CASCADE, related_name='profiles',null=True)
    caste=models.ForeignKey(Caste, on_delete=models.CASCADE, related_name='profiles',null=True)
    hobbies=models.ManyToManyField(Hobby, related_name='profiles')  ## null=True tha yahan
    father=models.OneToOneField(FatherProfile, on_delete=models.CASCADE, related_name='dependent',null=True)
    # yeh jb hoga jb hm 1 wala relation delete karein to us se refrenced jo jo object hoga us ki jaga undefined ajaye ga
    # religion=models.ForeignKey(Religion, on_delete=models.SET_DEFAULT, default= 'Undefined')







    # hm yahan yeh chahty k jb b koi data save ho to printf ka msg console pe print hojaye
    def save(self, *args, **kwargs):
        print(f"Data updated for {self.name}")
        super().save(*args, **kwargs)

    # jb hm ne apni profile class bnai to data save krany pe profileobject(1) likha arha tha us ki jaga agr hmaein bndy ka name chahiye to yeh karein gy
    def __str__(self):
        return self.name