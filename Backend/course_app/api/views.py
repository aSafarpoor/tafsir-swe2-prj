from rest_framework import generics
from course_app.models import course
#from serializers import CourseListSerializer
from  .serializers import CourseListSerializer
import json
from django.http import HttpResponse

class CourseListAPIview(generics.ListAPIView):
    queryset = course.objects.all()
    serializer_class = CourseListSerializer



def create(request):
    
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
        
        #print("\n\n\n",current_user,"\n\n\n")
        if current_user.teacher==True:
            pass
        else:
            message="user is not a teacher"
            return HttpResponse(message)
        
        try:
            is_exist=course.objects.filter(name=data["name"] , course_teacher=current_user).exists()
            if(is_exist==True):
                message="exist course with same name for this user"
                return HttpResponse(message)
            course_obj=course()
            course_obj.name=data["name"]
            course_obj.summary=data["summary"]
            course_obj.pre_movie=data["pre_movie"]
            course_obj.Headlines=data["Headlines"]
            course_obj.course_section_number=0
            course_obj.total_time_of_course=0
            course_obj.ref=data["ref"]
            course_obj.price=int(data["price"])
            course_obj.course_teacher=current_user
            course_obj.course_main_field=data["course_main_field"]
            course_obj.save()
            message="created"
            return HttpResponse(message)
        except:
            message="not_enough_data"
            return HttpResponse(message)
       
    else :
        message="bad request"
        return HttpResponse(message)

def change(request):
    
    if request.method=="POST":
        try:
            json_data=request.body
        except:
            message="bad urllll"
            return HttpResponse(message)
        
        data=json.loads(json_data)
        message="start"
        
        try :
            current_user = request.user
            name=current_user.name
        except:
            message="not logged in"
            return HttpResponse(message)
        #print("\n\n\n",current_user.first_name,"\n\n\n")///ok///
        if current_user.teacher==True:
            pass
        else:
            message="user is not a teacher"
            return HttpResponse(message)
        
        try:
            is_exist=course.objects.filter(name=data["old_name"] , course_teacher=current_user).exists()
            if(is_exist==False):
                message="not exist"
                return HttpResponse(message)
            
            course_obj=course.objects.get(name=data["old_name"] , course_teacher=current_user)
            #print("\n\n\n",course_obj.name,"\n\n\n")
            course_obj.name=data["new_name"]
            course_obj.summary=data["summary"]
            course_obj.pre_movie=data["pre_movie"]
            course_obj.Headlines=data["Headlines"]
            course_obj.ref=data["ref"]
            course_obj.price=int(data["price"])
            course_obj.course_teacher=current_user
            course_obj.course_main_field=data["course_main_field"]
            course_obj.save()
            message="changed"
            return HttpResponse(message)
        except:
            message="not_enough_data"
            return HttpResponse(message)
       
    else :
        message="bad request"
        return HttpResponse(message)

def delete(request):
    if request.method=="POST":
        try:
            json_data=request.body
        except:
            message="bad urllll"
            return HttpResponse(message)
        
        data=json.loads(json_data)
        message="start"
        
        try :
            current_user = request.user
            name=current_user.name
        except:
            message="not logged in"
            return HttpResponse(message)
        #print("\n\n\n",current_user.first_name,"\n\n\n")///ok///
        if current_user.teacher==True:
            pass
        else:
            message="user is not a teacher"
            return HttpResponse(message)
        
        try:
            is_exist=course.objects.filter(name=data["name"] , course_teacher=current_user).exists()
            print("\n\n\n","llll","\n")
            if(is_exist==False):
                message="not exist"
                return HttpResponse(message)
            print("\n\n\n","ddd","\n")
            obj=course.objects.filter(name=data["name"] , course_teacher=current_user)[0]
            print("\n\n\n","vvv","\n")
            obj.delete()
            message="done"
            return HttpResponse(message)
        except:
            message="not_enough_data"
            return HttpResponse(message)
       
    else :
        message="bad request"
        return HttpResponse(message)

############################################
'''
#http://127.0.0.1:8000/api/v1/course/create/create/?make={%22name%22:%20%22aaaa%22,%22summary%22:%20%22as%22,%22pre_movie%22:%20%22%22,%22Headlines%22:%20%22%22,%22ref%22:%20%22%22,%22price%22:%20123,%22course_main_field%22:%20%22%22}
#http://127.0.0.1:8000/api/v1/course/change/?change={%22old_name%22:%20%22aaaa%22,%22new_name%22:%20%22bbb%22,%22summary%22:%20%22as%22,%22pre_movie%22:%20%22%22,%22Headlines%22:%20%22%22,%22ref%22:%20%22%22,%22price%22:%20123,%22course_main_field%22:%20%22%22}
#http://127.0.0.1:8000/api/v1/course/delete/?delete={%22name%22:%20%22bbb%22,%22summary%22:%20%22as%22,%22pre_movie%22:%20%22%22,%22Headlines%22:%20%22%22,%22ref%22:%20%22%22,%22price%22:%20123,%22course_main_field%22:%20%22%22}
{
    "name": "aa",
    "summary": "as",
    "pre_movie": "",
    "Headlines": "",
    "ref": "",
    "price": 123,
    "course_main_field": ""
}
'''
############################################
