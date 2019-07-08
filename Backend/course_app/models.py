from django.db import models
# from teacher.models import teacher as t_model
# from fields.models import fields
from users.models import CustomUser as t_model



# Create your models here.

class course (models.Model) : 
    name=models.TextField(null=False,max_length=50,default="no_Name")
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
    user_counter=models.IntegerField(default=0)
    picture=models.ImageField(null=True,blank=True,upload_to="folanja/",default="folanja/images.png")
   
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


class who_has_what(models.Model):
    grade=models.IntegerField(null=True,blank=True)
    last_pass_section=models.IntegerField(default=0)
    course_completed=models.BooleanField(default=False)
    # course_finished_time=models.TimeField(null=True,blank=True)
    course_finished_time=models.CharField(null=True,blank=True,max_length=50)
    course_user=models.ForeignKey(t_model,on_delete=models.CASCADE,related_name='fk_student',default=0)
    course_name=models.ForeignKey(course,on_delete=models.CASCADE,related_name='fk_course',default=0)
    grade=models.TextField(null=True,blank=True,default="")
    total_grade=models.IntegerField(null=True,blank=True,default=-1)

class section(models.Model):
    part=models.IntegerField(default=0,null=False,blank=False)
    name=models.TextField(max_length=100,null=True,blank=True,default="")
    movie_id=models.IntegerField(null=True,blank=True)
    file=models.FileField(null=True,blank=True,upload_to="anja/")#,defult="anja/nofile.txt")
    course=models.ForeignKey(course,on_delete=models.CASCADE,related_name='fkcourse',default=0)

class question_exam(models.Model):
    number=models.IntegerField(default=-1,null=False,blank=False)
    question=models.TextField(max_length=300,null=True,blank=True)
    choice1=models.TextField(max_length=200,null=True,blank=True)
    choice2=models.TextField(max_length=200,null=True,blank=True)
    choice3=models.TextField(max_length=200,null=True,blank=True)
    choice4=models.TextField(max_length=200,null=True,blank=True)
    true_choice=models.IntegerField(default=-1,null=False,blank=False)
    which_section=models.ForeignKey(section,on_delete=models.CASCADE,related_name='fk_section',default=0)


