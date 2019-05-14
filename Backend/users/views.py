from rest_framework import generics
from .serializers import TeacherInfoSerializer,WhatPersonHave,TeacherSerializer,StudentSerializer
import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from . import models
from . import serializers
from course_app.models import course
from course_app.models import who_has_what,section
from users.models import CustomUser
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
            #print("\n\n","llllllllllllllllllllllllllll","\n",current_course.name,"\n\n")
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
            #print("\n\n",current_course.id,"\n\n")
            message=" registered"
            return HttpResponse(message)
        except:
            message="not_enough_data"
            return HttpResponse(message)
       
    else :
        message="bad request"
        return HttpResponse(message)
'''
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)
'''

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
            who_has_what

            is_course_exist=course.objects.filter(id=requested_id).exists()
            print("11111111111111111111")
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
            #print(enable_num)
            #print(current_course.id)
            try:
                is_exist=section.objects.filter(course=current_course).exists()
                query=section.objects.filter(course=current_course)
            except:
                message="bed request!!!"
                return HttpResponse(message) 
            
            dict={}
            try:
                print("query is: ",query)
                print("len is:",len(query))
                for i in range(len(query)):
                    obj=query[i]
                    if(obj.part<=enable_num):
                        temp={}
                        temp["part"]=obj.part
                        temp["name"]=obj.name
                        temp["movie"]=obj.movie
                        temp["file"]=obj.file

                        dict[obj.part]=temp
                        print("y")
                    else:
                        print("no")
                #add general info:
                temp={}
                temp["name"]=current_course.name
                temp["ref"]=current_course.ref
                dict[" general_info"]=temp
            except:
                message="404"
                return HttpResponse(message)
            print(dict)
            #     temp={}
                
        
            #     dict[part]=temp

            #send sth :)
            #should complete it 
            return HttpResponse(dict)            
            

     
     
        except:
            message="finaliii "
            return HttpResponse(message)
    message="hello"
    return HttpResponse(message)