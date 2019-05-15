from rest_framework import generics
from .serializers import TeacherInfoSerializer,WhatPersonHave,TeacherSerializer,StudentSerializer
import json
import os
from django.http import HttpResponse,JsonResponse
from django.core import  serializers
from . import models
from . import serializers
from course_app.models import course,question_exam
from course_app.models import who_has_what,section
from users.models import CustomUser
from datetime import datetime
class StudentListView(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.filter(student=True)
    serializer_class = serializers.StudentSerializer


class TeacherListView(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.filter(teacher=True)
    serializer_class = serializers.TeacherSerializer

class TeacherDetailsAPIView(generics.RetrieveAPIView):
    #session = Session.objects.get(session_key=session_key)
    lookup_field = 'id'
    queryset = CustomUser.objects.all()
    serializer_class = TeacherInfoSerializer

class JoinTable(generics.ListAPIView):
    serializer_class =  WhatPersonHave

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        choosed_id = self.kwargs['choosed_id']
        return course.objects.filter(course_teacher=choosed_id)


def register(request):
    if request.method=="POST":
        try:
            json_data=request.body
        except:
            message="bad urllll"
            return HttpResponse(message)
        
        data=json.loads(json_data)

        try :
            current_user = request.user
            name=current_user.name
        except:
            message="not logged in"
            return HttpResponse(message)
        
        if current_user.student==True:
            pass
        else:
            message="user is not a student"
            return HttpResponse(message)
        try:####################should be complete############
            is_course_exist=course.objects.filter(id=data["id"] ).exists()
           
            if(is_course_exist==False):
                message="not eanble course"
                return HttpResponse(message)
            current_course=course.objects.filter(id=data["id"] )[0]
            try:
                
                is_exist=who_has_what.objects.filter(course_user=current_user , course_name=current_course ).exists()
    
                if(is_exist==True):
                    message="registered before"
                    return HttpResponse(message)
                
            except:
                    message="bad request"
                    return HttpResponse(message)
                    
            obj=who_has_what()
            obj.course_user=current_user
            obj.course_name=current_course
            obj.save()
            current_course.user_counter+=1
            current_course.save()
            message=" registered"
            return HttpResponse(message)
        except:
            message="not_enough_data"
            return HttpResponse(message)
       
    else :
        message="bad request"
        return HttpResponse(message)

def multiple_section(request):
    if request.method=='GET':
        if 's' in request.GET:
            requested_id=int(request.GET['s'])
        else:
            message="bad request"
            return HttpResponse(message)
        try:
            current_user=request.user
        except:
            message="not available user"
            return HttpResponse(message)
        try:
            # who_has_what

            is_course_exist=course.objects.filter(id=requested_id).exists()

            if(is_course_exist==False):
                message="not eanble course"
                return HttpResponse(message)
            current_course=course.objects.filter(id=requested_id)[0]
            is_registered=who_has_what.objects.filter(course_user=current_user,course_name=current_course).exists()

            if(is_registered==False):
                message="not registered"
                return HttpResponse(message)
          
            whw_obj=who_has_what.objects.filter(course_user=current_user,course_name=current_course)[0]
          
            last_pass_section=whw_obj.last_pass_section
            
            course_completed=whw_obj.course_completed
          
            enable_num=last_pass_section+1
            if(course_completed):
                enable_num-=1
            try:
                is_exist=section.objects.filter(course=current_course).exists()
                query=section.objects.filter(course=current_course)
            except:
                message="bed request!!!"
                return HttpResponse(message) 
            
            dict={}
            try:
             
                for i in range(len(query)):
                    obj=query[i]
                    if(obj.part<=enable_num):
                        ii=obj.part-1
                       
                        temp={}
                        #temp["grade"]=.....##########################
                        try:
                            grade_=int((whw_obj.grade.split("_")[ii+1]))
                        except:
                            grade_=-1
                        temp["grade"]=grade_
                        temp["part"]=obj.part
                        temp["name"]=obj.name
                        temp["movie"]=obj.movie
                        
                        try:

                            r1=request.path
                            r2=request.build_absolute_uri('/')
                            #r3=r2[:-1]+r1
                            r3=r2[:-1]
                          
                            file_=str(obj.file.url)
                            r3+=file_
                            temp["file"]=r3
                            
                        except:
            
                            temp["file"]=""    
                        dict[obj.part]=temp
                print(1111111111)        
                #add general info:
                temp={}
                temp["name"]=current_course.name
                temp["ref"]=current_course.ref
                temp["course_is_complte"]=whw_obj.course_completed
                temp["course_total_grade"]=whw_obj.total_grade
                temp[ "course_finished_time"]=whw_obj.course_finished_time
                dict[" general_info"]=temp
            except:
                message="404"
                return HttpResponse(message)
          
            
            return JsonResponse(dict)

        except:
            message="404"
            return HttpResponse(message)
    message="404"
    return HttpResponse(message)

def test(request):
    
    if request.method=="POST":
        try:
            json_data=request.body
        
        except:
            message="bad url"
            return HttpResponse(message)

        data=json.loads(json_data)

        try :
            current_user = request.user
            name=current_user.name
        except:
            message="not logged in"
            return HttpResponse(message)
        
        if current_user.student==True:
            pass
        else:
            message="user is not a student"
            return HttpResponse(message)
        
        try:
            is_exist=course.objects.filter(id=data["course_id"]).exists()
            if(is_exist==False):
                message="not find course"
                return HttpResponse(message)
            current_course=course.objects.filter(id=data["course_id"])[0]
        except:
            message="not enough data"
            return HttpResponse(message)
        
        try:
            is_registered=who_has_what.objects.filter(course_user=current_user,course_name=current_course).exists()

            if(is_registered==False):
                message="not registered"
                return HttpResponse(message)
        
            whw_obj=who_has_what.objects.filter(course_user=current_user,course_name=current_course)[0]
        except:
            message="not enough data"
            return HttpResponse(message)

        try: 
            part_num=data["part"]
            is_exist=section.objects.filter(part=part_num , course=current_course).exists()
            if(is_exist==False):
                message="not find session"
                return HttpResponse(message)
            current_section=section.objects.filter(part=part_num , course=current_course)[0]
        except:
            message="not enough data"
            return HttpResponse(message)

        try:
            counter=len(data)
            counter-=2
            true_counter=0
            for i in range(1,counter+1):
                num=i
                
                q_obj=question_exam.objects.filter(whitch_section=current_section,number=num)[0]
                choice=data[str(num)]
                true_choice=q_obj.true_choice
                
                if(choice==true_choice):
                    true_counter+=1
            c=int(true_counter*100/counter)
          
            if(c>70):
                if(whw_obj.last_pass_section+1==current_section.part):
                    whw_obj.last_pass_section+=1
                    whw_obj.grade+="_"
                    c=true_counter*100/counter
                    whw_obj.grade+=str(int(c))
                    number_of_sections=len(section.objects.filter(course=current_course))
                    if(number_of_sections==current_section.part):
                        whw_obj.course_completed=True
                        arr=whw_obj.grade
                        arr=arr.split("_")
                        summ=0
                        for j in arr:
                            if(not j==""):
                                summ+=int(j)
                        j=summ/number_of_sections
                        j=int(j)
                        whw_obj.total_grade=j

                        whw_obj. course_finished_time= datetime.now()

                        message="passed!!!"+" your grade is:"+str(int(c))+"\n"+"course is complete"+"your total grade is:"+str(j)
                    else:
                        message="passed!!!"+" your grade is:"+str(int(c))
                    whw_obj.save()

                    return HttpResponse(message)

                if(whw_obj.last_pass_section+1>current_section.part):

                    message="passed before!!!"
                    return HttpResponse(message)

                else:
                    message="not excepted session!!!"
                    return HttpResponse(message)
                
            else:
                message="failed!!!"+"your geade is:"+str(c)
                return HttpResponse(message)
        except:
            message="404"
            return HttpResponse(message)
    else:
        message="bad request"
        return HttpResponse(message)
'''
{
	"course_id":31,
	"part":1,
	"1":1,
	"2":2
}

{
	"course_id":31,
	"part":2,
	"1":2,
	"2":2
}

'''
        
        
