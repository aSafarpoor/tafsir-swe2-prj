import time
from rest_framework import generics
from .serializers import TeacherInfoSerializer,WhatPersonHave,TeacherSerializer,StudentSerializer
import json
import os
from django.http import HttpResponse,JsonResponse
from django.core import  serializers
from . import models
from . import serializers
from course_app.models import course,question_exam,file_pull
from course_app.models import who_has_what,section
from users.models import CustomUser
from datetime import datetime
from rest_auth.views import LoginView
from raw_certificate_maker_should_be_embeded.certificate import make_certificate 
import datetime
from persiantools.jdatetime import JalaliDate
from PIL import Image

from rest_framework.authtoken.models import Token


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
        choosed_id = self.kwargs['id']
        return course.objects.filter(course_teacher=choosed_id)




def ct(request):
    if request.method=='GET':
                      
        try:
            try :
                token=request.META["HTTP_TOKEN"]
                if(token[0]=="\""):
                    token=token[1:-1]
                
                obj = Token.objects.filter(key=token)[0]
        
                current_user = models.CustomUser.objects.filter(id=obj.user_id)[0]
            
            except:
                message="not logged in"
                return HttpResponse(message)

            is_course_exist=course.objects.filter(course_teacher=current_user).exists()
           
           
            if(is_course_exist==False):
                message="not eanble course"
                return HttpResponse(message)
            current_course=course.objects.filter(course_teacher=current_user)
            print(current_course)
            # dict={}
            tem=[]
            t=0
            for i in current_course:
                t+=1
                temp={}
                temp["name"]=i.name
                temp["summary"]=i.summary
                temp["course_section_number"]=i.course_section_number
                temp["total_time_of_course"]=i.total_time_of_course
                temp["course_teacher_fn"]=i.course_teacher.first_name
                temp["course_teacher_ln"]=i.course_teacher.last_name
                temp["course_main_field"]=i.course_main_field
                temp["user_counter"]=i.user_counter
                # temp["picture"]=
                try:
                    objmovie=file_pull.objects.filter(id=i.picture)[0]
                
                    r1=request.path
                    r2=request.build_absolute_uri('/')
                    #r3=r2[:-1]+r1
                    r3=r2[:-1]

                    file_=str(objmovie.file.url)
                    r3+=file_
                    temp["picture"]=str(r3)
                except:
                    pass

                # print(3333333333333333333355555555555555555555)
                tem.append(temp)
                
            # dict["0"]=tem
            # print(tem)
            # print(dict)
            # return JsonResponse(dict)


            dicto={}
            dicto["first"]=tem
            # dict["last_name"]=current_user.last_name
            # dict["email"]=current_user.email
            print(dicto)
            return JsonResponse(dicto)
            # return JsonResponse(['a', 'b'], safe=False)


        except Exception as e:
            print(e )
            message="404"
            return HttpResponse(message)
   
    message="404"
    return HttpResponse(message)





def user_info(request):
    # print("start")  
    # print("header ",request.headers)
    

    # print(request.method," ddddddddddddddddddddddddddd ")
    
    if request.method=="GET" or request.method=="OPTIONS":
        # try:
        #     json_data=request.body
        # except:
        #     message="bad urllll"
        #     return HttpResponse(message)
        # print(json_data)
        try :
            token=request.META["HTTP_TOKEN"]
            if(token[0]=="\""):
                token=token[1:-1]
            
            obj = Token.objects.filter(key=token)[0]
    
            current_user = models.CustomUser.objects.filter(id=obj.user_id)[0]
        
        except:
            message="not logged in"
            return HttpResponse(message)
        
        dict={}
        dict["first_name"]=current_user.first_name
        dict["last_name"]=current_user.last_name
        dict["email"]=current_user.email
        print(dict)
        return JsonResponse(dict)
    
    message="bad request"
    return HttpResponse(message)


def user_courses(request):
   
    if request.method=="GET" or request.method=="OPTIONS":
        try :
            token=request.META["HTTP_TOKEN"]
            if(token[0]=="\""):
                token=token[1:-1]
            
            obj = Token.objects.filter(key=token)[0]
    
            current_user = models.CustomUser.objects.filter(id=obj.user_id)[0]
        # try:
        #     current_user=request.user
        except:
            message="not logged in"
            return HttpResponse(message)
        dict={}
        dict["name"]=""
        query=who_has_what.objects.filter(course_user=current_user)
        t=0
        for i in query:
            t+=1
            #temp={}
            #temp["id"]=i.course_name.id
            dict["name"]+=str(i.course_name.name)+"***"
	    
           
        return JsonResponse(dict)
    
    message="bad request"
    return HttpResponse(message)






def register(request):
    if request.method=="POST" or request.method=="OPTIONS":
        try:
            json_data=request.body
        except:
            message="bad urllll"
            return HttpResponse(message)
        print(json_data)
        data=json.loads(json_data)
        print(data)
        try :
            token=request.META["HTTP_TOKEN"]
            if(token[0]=="\""):
                token=token[1:-1]
            
            obj = Token.objects.filter(key=token)[0]
    
            current_user = models.CustomUser.objects.filter(id=obj.user_id)[0]
            # current_user = request.user
        #    name=current_user.name
        
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
            message="bad     request"
            return HttpResponse(message)
        try:
            # current_user=request.user
            token=request.META["HTTP_TOKEN"]
            if(token[0]=="\""):
                token=token[1:-1]
            
            obj = Token.objects.filter(key=token)[0]
    
            current_user = models.CustomUser.objects.filter(id=obj.user_id)[0]
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
            # print(222222222222222222222222222222)
            # print(query)
            try:
                session_list=[]
                # print(query)
                for i in range(len(query)):
                    
                    obj=query[i]
                    # if(obj.part-1<=enable_num):
                    if(True):
                        ii=obj.part-1
                        
                        temp={}
                        #temp["grade"]=.....##########################
                        try:
                            grade_=int((whw_obj.grade.split("_")[ii+1]))
                        except:
                            grade_=-1
                        if(obj.part-1<=enable_num):
                            temp["is_valid"]=True
                        else:
                            temp["is_valid"]=False
                        temp["grade"]=grade_
                        temp["part"]=obj.part
                        temp["id"]=obj.id
                        temp["name"]=obj.name
                        temp["detail"]=obj.detail
                        try:
                            if(obj.part-1<=enable_num):
                               
                                objmovie=file_pull.objects.filter(id=obj.movie_id)[0]
                                
                                try:
                                    r1=request.path
                                    r2=request.build_absolute_uri('/')
                                    #r3=r2[:-1]+r1
                                    r3=r2[:-1]

                                    file_=str(objmovie.file.url)
                                    r3+=file_
                                    temp["movie"]=r3
                                except:
                                    pass


                            
                        except:
                            # print("zzzzzzzzzzzzzzzz")
                            temp["movie"]=""
                        try:
                            if(obj.part-1<=enable_num):
                                objmovie=file_pull.objects.filter(id=obj.file)[0]
            
                                r1=request.path
                                r2=request.build_absolute_uri('/')
                                #r3=r2[:-1]+r1
                                r3=r2[:-1]

                                file_=str(objmovie.file.url)
                                r3+=file_
                                temp["file"]=r3

                        
                        except:

                            temp["file"]=""
                        #dict[obj.part]=temp
                        session_list.append(temp)

                dict["sessions"]=session_list
                
                #add general info:
                temp={}
                # print("heloooooooooo")
                temp["name"]=current_course.name
                # temp["ref"]=current_course.ref
                temp["course_is_complte"]=whw_obj.course_completed
                temp["course_total_grade"]=whw_obj.total_grade
                temp[ "course_finished_time"]=whw_obj.course_finished_time
                dict["general_info"]=temp
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
        print(data)

        try :
            # current_user = request.user
            token=request.META["HTTP_TOKEN"]
            if(token[0]=="\""):
                token=token[1:-1]
            
            obj = Token.objects.filter(key=token)[0]
    
            current_user = models.CustomUser.objects.filter(id=obj.user_id)[0]
           
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
            ans=data["answers"]
            counter=len(data)
            # counter-=2

            # print("data is: ",data)
            cur_time=int(time.time()*1000000)
            if(cur_time-int(whw_obj.last_time_question_req)>counter*80*1000000):
                message="too late :("
                return HttpResponse(message)
            
            true_counter=0
            for i in range(1,counter+1):
                num=i
                try:
                    q_obj=question_exam.objects.filter(which_section=current_section,number=num)[0]
                    
                    choice=ans[num]
                    true_choice=q_obj.true_choice
                    
                    if(choice==true_choice):
                        true_counter+=1
                except:
                    pass
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

                        # whw_obj. course_finished_time= datetime.now()
                        whw_obj.course_finished_time=str(JalaliDate.today())

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






def get_own_course_info(request):
    if request.method=='GET':
        if 's' in request.GET:
            requested_id=int(request.GET['s'])
        else:
            message="bad request"
            return HttpResponse(message)
        try:
            # current_user=request.user
            token=request.META["HTTP_TOKEN"]
            if(token[0]=="\""):
                token=token[1:-1]
            
            obj = Token.objects.filter(key=token)[0]
    
            current_user = models.CustomUser.objects.filter(id=obj.user_id)[0]
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


            if(current_course.course_teacher==current_user):
                pass

            else:
                message="not owner"
                return HttpResponse(message)
            #enable num is always enable

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
                    if(True):
                        ii=obj.part-1

                        temp={}

                        temp["part"]=obj.part
                        temp["name"]=obj.name
                        
                       
            
                        try:
                            objmovie=file_pull.objects.filter(id=obj.movie)[0]
                            r1=request.path
                            r2=request.build_absolute_uri('/')
                            #r3=r2[:-1]+r1
                            r3=r2[:-1]

                            file_=str(objmovie.file.url)
                            r3+=file_
                            temp["movie"]=r3
                        except:
                            pass

                        try:
                            
                            # objmovie=file_pull.objects.filter(id=obj.file)[0]
                            # temp["file"]=objmovie
                            objmovie=file_pull.objects.filter(id=obj.file)[0]
                            r1=request.path
                            r2=request.build_absolute_uri('/')
                            #r3=r2[:-1]+r1
                            r3=r2[:-1]

                            file_=str(objmovie.file.url)
                            r3+=file_
                            temp["file"]=r3
                            
                        except:

                            temp["file"]=""

                        #each section has some question_exams:

                        try:
                            is_exist=question_exam.objects.filter(which_section=obj).exists()
                            q_query=question_exam.objects.filter(which_section=obj)
                        except:
                            pass


                        for i in range(len(q_query)):
                            q_object=q_query[i]

                            ii=q_object.number

                            q_temp={}

                            q_temp["number"]=ii
                            q_temp["question"]=q_object.question
                            q_temp["choice1"]=q_object.choice1
                            q_temp["choice2"]=q_object.choice2
                            q_temp["choice3"]=q_object.choice3
                            q_temp["choice4"]=q_object.choice4
                            q_temp["true_choice"]=q_object.true_choice

                            question_num="q_num_"+str(ii)
                            temp[question_num]=q_temp


                        dict[obj.part]=temp

                #add general info:
                temp={}
                temp["name"]=current_course.name

                temp["summary"]=current_course.summary
                # temp["pre_movie"]=current_course.pre_movie
                # temp["Headlines"]=current_course.Headlines

                temp["course_section_number"]=current_course.course_section_number
                temp["total_time_of_course"]=current_course.total_time_of_course
                
                temp["course_main_field"]=current_course.course_main_field



                try:
                    objmovie=file_pull.objects.filter(id=current_course.picture)[0]
                
                    r1=request.path
                    r2=request.build_absolute_uri('/')
                    #r3=r2[:-1]+r1
                    r3=r2[:-1]

                    file_=str(objmovie.file.url)
                    r3+=file_
                    temp["picture"]=r3
                except:
                    pass

                dict["general_info"]=temp
            except:
                message="404"
                return HttpResponse(message)

            return JsonResponse(dict)

        except:
            message="404"
            return HttpResponse(message)
    message="404"
    return HttpResponse(message)



def get_own_course_info2(request):
    if request.method=='GET':
        if 's' in request.GET:
            requested_id=int(request.GET['s'])
        else:
            message="bad request"
            return HttpResponse(message)
        try:
            # current_user=request.user
            token=request.META["HTTP_TOKEN"]
            if(token[0]=="\""):
                token=token[1:-1]
            
            obj = Token.objects.filter(key=token)[0]
    
            current_user = models.CustomUser.objects.filter(id=obj.user_id)[0]
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


            if(current_course.course_teacher==current_user):
                pass

            else:
                message="not owner"
                return HttpResponse(message)
            #enable num is always enable

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
                    if(True):
                        ii=obj.part-1

                        temp={}

                        temp["part"]=obj.part
                        temp["name"]=obj.name
                       
                        try:
                            objmovie=file_pull.objects.filter(id=obj.file)[0]
                            r1=request.path
                            r2=request.build_absolute_uri('/')
                            #r3=r2[:-1]+r1
                            r3=r2[:-1]

                            file_=str(objmovie.file.url)
                            r3+=file_
                            temp["file"]=r3
                        
                        except:

                            temp["file"]=""

                        #each section has some question_exams:

                        try:
                            is_exist=question_exam.objects.filter(which_section=obj).exists()
                            q_query=question_exam.objects.filter(which_section=obj)
                        except:
                            q_query=[]


                        for i in range(len(q_query)):
                            q_object=q_query[i]

                            ii=q_object.number

                            q_temp={}

                            q_temp["number"]=ii
                            q_temp["question"]=q_object.question
                            q_temp["choice1"]=q_object.choice1
                            q_temp["choice2"]=q_object.choice2
                            q_temp["choice3"]=q_object.choice3
                            q_temp["choice4"]=q_object.choice4
                            q_temp["true_choice"]=q_object.true_choice

                            question_num="q_num_"+str(ii)
                            temp[question_num]=q_temp


                        dict[obj.part]=temp

                temp={}
                temp["name"]=current_course.name

                temp["summary"]=current_course.summary
                
                temp["course_section_number"]=current_course.course_section_number
                temp["total_time_of_course"]=current_course.total_time_of_course
                
                temp["course_main_field"]=current_course.course_main_field


                try:
                    objmovie=file_pull.objects.filter(id=current_course.picture)[0]
                
                    r1=request.path
                    r2=request.build_absolute_uri('/')
                    #r3=r2[:-1]+r1
                    r3=r2[:-1]

                    file_=str(objmovie.file.url)
                    r3+=file_
                    temp["picture"]=r3
                except:
                    pass

                dict["general_info"]=temp
            except:
                message="404"
                return HttpResponse(message)

            return JsonResponse(dict)

        except:
            message="404"
            return HttpResponse(message)
    message="404"
    return HttpResponse(message)

def course_counter(request):
    if request.method=='GET':
        try:
            token=request.META["HTTP_TOKEN"]
            if(token[0]=="\""):
                token=token[1:-1]
            
            obj = Token.objects.filter(key=token)[0]
    
            current_user = models.CustomUser.objects.filter(id=obj.user_id)[0]
        except:
            message="not available user"
            return HttpResponse(message)

        try:
            dict={}
            is_exist=who_has_what.objects.filter(course_user=current_user).exists()

            if(is_exist==False):
                dict["registered"]=[]
                dict["passed"]=[]
                dict["registered_count"]=0
                dict["passed_count"]=0

            else:
                reg_list=[]
                passed_list=[]
                query=who_has_what.objects.filter(course_user=current_user)
                for obj in query:
                    if(obj.course_completed==True):
                        reg_list.append(obj.course_name.name)
                        passed_list.append(obj.course_name.name)
                    else:
                        reg_list.append(obj.course_name.name)

                dict["registered"]=reg_list
                dict["passed"]=passed_list
                dict["registered_count"]=len(reg_list)
                dict["passed_count"]=len(passed_list)


            return JsonResponse(dict)
        except:

            message="404"
            return HttpResponse(message)
    message="404"
    return HttpResponse(message)




def create(request):

    if request.method=="POST":
        try:
            json_data=request.body
        except:
            message="bad urllll"
            return HttpResponse(message)
        data=json.loads(json_data.decode())
        try:
            user_obj=CustomUser()
            
            user_obj.first_name=data["first_name"]
            
            user_obj.save()
            message="created"
            
            return HttpResponse(message)
        except:
            
            message="not_enough_data"
            return HttpResponse(message)

    else :
        message="bad request"
        return HttpResponse(message)



def ask_crtification(request):
    if request.method=='GET':
        if 's' in request.GET:
            course_id=int(request.GET['s'])
        try:
            token=request.META["HTTP_TOKEN"]
            if(token[0]=="\""):
                token=token[1:-1]
            
            obj = Token.objects.filter(key=token)[0]
    
            current_user = models.CustomUser.objects.filter(id=obj.user_id)[0]
            # current_user=request.user
            print(current_user)
        except:
            message="not available user"
            return HttpResponse(message)
        
        if(current_user.student==False):
            message="not student"
            return HttpResponse(message)

        try:
            is_exist=course.objects.filter(id=course_id).exists()
            if(is_exist==False):
                message="not find course"
                return HttpResponse(message)
            current_course=course.objects.filter(id=course_id)[0]
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
            if(whw_obj.course_completed):
                first_name=current_user.first_name
                # pic=current_user.picture
                last_name=current_user.last_name

                passed_day=whw_obj.course_finished_time
                # print(passed_day)
                course_name=current_course.name
      
                teacher_name=current_course.course_teacher.full_name
                print("complete informations")
                adrs=make_certificate(first_name,last_name,passed_day,course_name,teacher_name)
               
                domain = request.get_host()
                adrs=domain+"/"+adrs
                dict={}
                dict["certificate"]=adrs
                print(dict)
                return JsonResponse(dict)
                
            else:
                message="course not finished yet"
                return HttpResponse(message)
        except:
            message="bad happend"
            return HttpResponse(message)
    else:
        message="bad request"
        return HttpResponse(message)


from django_csrf_protect_form import csrf_protect_form

@csrf_protect_form
def return_section_test(request):

    if request.method=='GET' or request.method=='OPTIONS':
        print("zadsfgb")
        if 's' in request.GET:
            section_id=int(request.GET['s'])
        else:
            message="bad request"
            return HttpResponse(message)
        try:
            token=request.META["HTTP_TOKEN"]
            print(token)            
            if(token[0]=="\""):
                token=token[1:-1]
            
            obj = Token.objects.filter(key=token)[0]
    
            current_user = models.CustomUser.objects.filter(id=obj.user_id)[0]
           
        except:
            message="not available user"
            return HttpResponse(message)
        try:
            # who_has_what
            is_section_exist=section.objects.filter(id=section_id).exists()
            
            if(is_section_exist==False):
                message="not eanble course"
                return HttpResponse(message)
            
            current_section=section.objects.filter(id=section_id)[0]
            current_course=current_section.course
            try:
              

                is_registered=who_has_what.objects.filter(course_user=current_user,course_name=current_course).exists()

                if(is_registered==False):
                    message="not registered"
                    return HttpResponse(message)
                
                whw_obj=who_has_what.objects.filter(course_user=current_user,course_name=current_course)[0]
            except:
                message="not enough data"
                return HttpResponse(message)
           
            last_pass_section=whw_obj.last_pass_section

            course_completed=whw_obj.course_completed
            
            enable_num=last_pass_section+1
            if(course_completed):
                enable_num-=1
            try:
                # is_exist=question_exam.objects.filter(section=current_section).exists()
                query=question_exam.objects.filter(which_section=current_section)
            except:
                message="bed request!!!"
                return HttpResponse(message)

            dict={}
            try:
                q_list=[]
               
                
                for i in range(len(query)):
                    obj=query[i]
                    print(current_section.part,enable_num,"    rrrrrrrrrrrrrrrrrrr")
                    if(current_section.part-1<=enable_num):
                     

                        temp={}
                        print(obj)

                        temp={}
                        temp["course_id"]=current_course.id 
                        temp["section_part"]=obj.which_section.part
                        temp["number"]=obj.number
                        temp["question"]=obj.question
                        temp["choice1"]=obj.choice1
                        temp["choice2"]=obj.choice2
                        temp["choice3"]=obj.choice3
                        temp["choice4"]=obj.choice4
                        q_list.append(temp)
             
                dict["q_list"]=q_list
                
            except:
                message="404"
                return HttpResponse(message)
    
            whw_obj.last_time_question_req=int(time.time()*1000000)
            whw_obj.save()
            return JsonResponse(dict)

        except:
            message="404"
            return HttpResponse(message)
    message="404"
    return HttpResponse(message)
