from django.db import models
# from teacher.models import teacher as t_model
# from fields.models import fields
from users.models import CustomUser as t_model

# Create your models here.

class course (models.Model) : 
    name=models.TextField(null=False,max_length=50)
    summary=models.TextField(null=True,max_length=250)
    pre_movie=models.TextField(null=True,blank=True)
    Headlines=models.TextField(null=True,blank=True,max_length=450)
    user_number=models.IntegerField(default=0)
    course_section_number=models.IntegerField(null=True,blank=True,default=0)
    total_time_of_course=models.IntegerField(null=True,blank=True,default=0)
    ref=models.TextField(null=True,max_length=450,blank=True)
    price=models.IntegerField(default=0,null=True,blank=True)
    all_text_content=models.TextField(null=True,blank=True)
    exam=models.TextField(null=True,blank=True)
    course_teacher=models.ForeignKey(t_model,on_delete=models.CASCADE,related_name='fk_teacher',default=0)
    course_main_field=models.TextField(null=True,blank=True,max_length=100)
    #course_main_field=models.ForeignKey(fields,on_delete=models.CASCADE,null=True,blank=True,related_name='fk_fields1')


from django.db.models import signals
def create_remove(sender, **kwargs):
    for to in t_model.objects.all():
        counter=0
        for co in sender.objects.all():
            if(to==co.course_teacher):
                counter+=1
        to.course_counter=counter
        to.save()


signals.post_save.connect(create_remove, sender=course)
signals.post_delete.connect(create_remove,sender=course)