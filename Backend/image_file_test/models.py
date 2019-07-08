from django.db import models




# Create your models here.

class image_file(models.Model) : 
    name=models.TextField(null=False,max_length=50,default="no_Name")
    # file=models.FileField(null=True,blank=True,upload_to="folanja/temp_file_dir/")
    picture=models.FileField(null=True,blank=True,upload_to="folanja/temp_image_dir/",default="folanja/images.png")

class movie_link(models.Model):
    discription=models.TextField(null=False,max_length=50,default="no_Name")
    movie=models.FileField(null=False,max_length=50,default="no_Name")
    section_id=models.IntegerField(null=True,blank=True)
    