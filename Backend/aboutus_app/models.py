from django.db import models
# from teacher.models import teacher as t_model
# from fields.models import fields
from users.models import CustomUser as t_model



# Create your models here.

class aboutus (models.Model) : 
    title=models.TextField(null=False,max_length=50,default="no_Name")
    explanation=models.TextField(null=False,max_length=500,default="no_Name")
    instagram=models.URLField(null=True,blank=True)
    telegram=models.URLField(null=True,blank=True)
    address=models.TextField(null=False,max_length=500,default="no_Name")
    phone=models.TextField(null=False,max_length=50,default="no_Name")
    map_link=models.URLField(null=True,blank=True)
    # file=models.FileField(null=True,blank=True,upload_to="folanja/aboutus",default="folanja/images.png")

class news(models.Model) :
    title=models.TextField(null=False,max_length=50,default="no_Name")
    explanation=models.TextField(null=False,max_length=5000,default="no_Name")
    picture=models.ImageField(null=True,blank=True,) 
   
class contactus(models.Model) :
    explanation=models.TextField(null=False,max_length=1000,default="no_Name")
     
   