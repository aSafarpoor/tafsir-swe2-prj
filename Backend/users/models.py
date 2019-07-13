from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    #name = models.CharField(blank=True, max_length=255)
    #shomare_shenasname=models.TextField(unique=True,null=False,max_length=10,help_text="shomare shenasname",default = "")
    teacher = models.BooleanField(null = False, default = False)
    student = models.BooleanField(null = False, default = True)
    introduction=models.TextField(null=True,max_length=500,blank=True)
    case_history=models.TextField(null=True,max_length=500,blank=True)
    first_name=models.TextField(null=False,max_length=50,blank=True)
    last_name=models.TextField(null=False,max_length=50,blank=True)
    full_name=models.TextField(null=False,max_length=70,blank=True)
    email=models.EmailField(null=False)
    phone_number =models.TextField(null=True,blank=True,max_length=15, default = "0")
    job =models.TextField(null=True,blank=True,max_length=150)
    job_history=models.TextField(null=True,blank=True,max_length=3000)
    job_location=models.TextField(null=True,blank=True,max_length=250)
    home_location=models.TextField(null=True,blank=True,max_length=250)
    major=models.TextField(null=True,blank=True,max_length=150)
    degree=models.TextField(null=True,blank=True,max_length=150)
    points=models.IntegerField(default=0)
    male = 'male'
    female = 'female'
    gender_CHOICES = (
        (male, 'male'),
        (female, 'female'),
    )
    single='single'
    married='married'
    MS_CHOICES = (
        (single, 'single'),
        (married, 'married'),
    )
    Hawzah='Hawzah'
    University='University'
    ET_CHOICES = (
        (Hawzah, 'Hawzah'),
        (University, 'University'),
    )
    gender=models.CharField(max_length=20,null=True,blank=True,choices=gender_CHOICES)
    maritial_status=models.CharField(blank=True,null=True,max_length=20 ,choices=MS_CHOICES)
    education_type=models.CharField(null=True,blank=True,max_length=20 ,choices=ET_CHOICES)
    course_counter=models.IntegerField(default=0)
    picture=models.ImageField(null=True,blank=True,upload_to="folanja/",default="folanja/images.png")




    def __str__(self):
        return self.email
