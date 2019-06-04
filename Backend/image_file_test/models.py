from django.db import models




# Create your models here.

class image_file(models.Model) : 
    name=models.TextField(null=False,max_length=50,default="no_Name")
    # file=models.FileField(null=True,blank=True,upload_to="folanja/temp_file_dir/")
    picture=models.ImageField(null=True,blank=True,upload_to="folanja/temp_image_dir/",default="folanja/images.png")
