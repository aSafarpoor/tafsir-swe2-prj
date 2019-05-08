from rest_framework import generics
from course_app.models import course
#from serializers import CourseListSerializer
from  .serializers import CourseListSerializer
from  .serializers import CourseListSerializer,CourseCreateSerializer
import json

class CourseListAPIview(generics.ListAPIView):
    queryset = course.objects.all()
    serializer_class = CourseListSerializer


class CourseCreateAPIView(generics.CreateAPIView):
    # current_user = request.user
    # print (current_user.id)
    queryset = course.objects.all()
    serializer_class = CourseCreateSerializer
    #permission needed

from django.http import HttpResponse

def create(request):
    
    if request.method=="GET":
        json_data=request.GET['change']
        data=json.loads(json_data)
        message="start"
        current_user = request.user
        #print("\n\n\n",current_user.first_name,"\n\n\n")///ok///
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


############################################
'''
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


'''
f request.method == 'GET':
    do_something()
elif request.method == 'POST':
    do_something_else()
'''


'''

def Buy_Sell(request):
    if 'change' in request.GET:
        my_change=request.GET['change'].split('$')
        message="start"
        if request.session.has_key("username"):

            if request.session["usern	ame"] == my_change[0]:
                user_name=my_change[0]
                number_of_stock=int(my_change[1])
                new_money_person_have=int(my_change[2])
                stocks_name=my_change[3]

                un = Person.objects.get(username=user_name)
                bn = Bourse.objects.get(namad=stocks_name)


                is_exist = MemberShip.objects.filter(
                    bourse=stocks_name,person=user_name).exists()

                if(is_exist==False and number_of_stock!=0):
                    MemberShip.objects.create(bourse=bn,person=un,number_of_stocks_person_has=number_of_stock)
                    message='ok'

                else:
                    obj=MemberShip.objects.get(bourse=bn , person=un)
                    if(number_of_stock==0):
                        obj.delete()
                        message='bye_bye'
                    else:
                        obj.number_of_stocks_person_has=number_of_stock
                        obj.save()
                        message="ok!!"



                un.money=new_money_person_have
                un.save()
            else:
                message="bad username"

        else:
            message = "not login"
            
        return HttpResponse(message)


    return HttpResponse('bad request :D')
'''