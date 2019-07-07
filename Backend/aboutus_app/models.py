from django.db import models
# from teacher.models import teacher as t_model
# from fields.models import fields
from users.models import CustomUser as t_model



# Create your models here.

class aboutus (models.Model) : 
    title=models.TextField(null=False,max_length=50,default="no_Name")
    explanation=models.TextField(null=False,max_length=500,default="no_Name")
    # file=models.FileField(null=True,blank=True,upload_to="folanja/aboutus",default="folanja/images.png")
     
   
