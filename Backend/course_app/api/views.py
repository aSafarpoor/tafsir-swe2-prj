from rest_framework import generics
from course_app.models import course,section,question_exam
#from serializers import CourseListSerializer
from  .serializers import CourseListSerializer
import json
from django.http import HttpResponse
import requests
from django.shortcuts import render


class CourseListAPIview(generics.ListAPIView):
    queryset = course.objects.all()
    serializer_class = CourseListSerializer
'''class SectionListAPIview(generics.ListAPIView):
    queryset = section.objects.all()
    serializer_class = SectionListSerializer
'''


def create(request):
    # print("\nhellooooo\n\n\n")
    if request.method=="POST":
        try:
            json_data=request.body
        except:
            message="bad urllll"
            return HttpResponse(message)
        
        data=json.loads(json_data)
        # print("\n\n\n\ndata is:",data,"\n\n\n\n")

        try :
            current_user = request.user
            # name=current_user.name
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
            number_of_sections=data["number_of_sections"]
            course_obj=course()
            course_obj.name=data["name"]
            course_obj.summary=data["summary"]
            course_obj.pre_movie=data["pre_movie"]
            course_obj.Headlines=data["Headlines"]
            course_obj.course_section_number=number_of_sections
            course_obj.total_time_of_course=data["total_time_of_course"]
            course_obj.ref=data["ref"]
            course_obj.price=int(data["price"])
            course_obj.course_teacher=current_user
            course_obj.course_main_field=data["course_main_field"]
            course_obj.save()
            for i in range(1,number_of_sections+1):
                section_dict=data[str(i)]
                #print(section_dict)
                section_obj=section()
                section_obj.part=i
                section_obj.name=section_dict["name"]
                section_obj.movie=section_dict["movie"]
                section_obj.file=section_dict["file"]
                section_obj.course=course_obj
                section_obj.save()
                num=section_dict["number_of_exam_question"]
                for j in range(1,num+1):
                    
                    info=section_dict[str(j)]
                    
                    q_obj=question_exam()
                    
                    q_obj.number=j#str(j)
                    
                    q_obj.question=info["question"]
                    q_obj.choice1=info["choice1"]
                    
                    q_obj.choice2=info["choice2"]
                    q_obj.choice3=info["choice3"]
                    q_obj.choice4=info["choice4"]
                    q_obj.true_choice=info["true_choice"]
                    q_obj.which_section=section_obj
                    q_obj.save()
                    
            message="created"
            return HttpResponse(message)
        except:
            message="not_enough_data"
            return HttpResponse(message)
       
    else :
        message="bad request"
        return HttpResponse(message)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
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


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
'''{
    "name": "xddsssssqqqha",
    "summary": "yad midahad",
    "pre_movie": "",
    "Headlines": "",
    "ref": "",
    "price": 123,
    "course_main_field": "",
    "number_of_sections":1,
    "total_time_of_course":0,
    "1":{
 			    "name":"jalase 1",
			    "movie":"",
			    "file":"",
			    "number_of_exam_question":2,
			    "1":{
				    	"question":"soal1",
						"choice1":"11",
						"choice2":"22",
						"choice3":"33",
						"choice4":"44",
						"true_choice":1
					},
				"2":{
				    	"question":"soal2",
						"choice1":"11",
						"choice2":"22",
						"choice3":"33",
						"choice4":"44",
						"true_choice":2
					}   
    	}
    
}'''
####################################

def call_aparat(self):

    try :
        token="8061df45098379e19114ab01f4a9eb27"
        address="https://www.aparat.com/etc/api/uploadform/luser/amirmansoubi828/ltoken/"+token
        response = requests.get(address)
        data = response.json()
        #data=json.loads(response.content)
        frm_id=data["uploadform"]["frm-id"]
        print(frm_id)


    except:
        response = requests.get("https://www.aparat.com/etc/api/login/luser/amirmansoubi828/lpass/79e9feb0135e82cab14fed182ef0891b9920d641")
        data=json.loads(response.content)
        token=data["login"]["ltoken"]
        address="https://www.aparat.com/etc/api/uploadform/luser/amirmansoubi828/ltoken/"+token
        response = requests.get(address)
        data = response.json()
        #data=json.loads(response.content)
        frm_id=data["uploadform"]["frm-id"]


    with open("sample.mp4",'rb') as f:
        data = {"data[title]":"new title" ,"data[category]":3,"data[tags]":"تست-ای پی آی-آپارات","data[comments]":"no","data[descr]" : "123" , "frm-id":frm_id}
        files = {"video":("sample.mp4", f, 'video/mp4')}
        url = "https://www.aparat.com/etc/api/uploadpost/luser/amirmansoubi828/username/amirmansoubi828/ltoken/8061df45098379e19114ab01f4a9eb27/uploadid/1373380/atrty/1562881324/avrvy/977508/key/6df83cab000f4b24907277a0473237c31380ebe1/"
        req = requests.post(url, files=files, data=data)
        print(url)
        print("fffffffffff")
        print(req)
        req.json()
        return HttpResponse("Salam")


def edit(request):
    
    if request.method=="POST":
        try:
            json_data=request.body
        except:
            message="bad urllll"
            return HttpResponse(message)
        
        data=json.loads(json_data)

        try :
            current_user = request.user
            # name=current_user.name
        except:
            message="not logged in"
            return HttpResponse(message)
        
        if current_user.teacher==True:
            pass
        else:
            message="user is not a teacher"
            return HttpResponse(message)
        try:
            is_exist=course.objects.filter(name=data["old_name"] , course_teacher=current_user).exists()
            if(is_exist==True):
                pass

            else:
                message="ont exist course with same name for this user"
                return HttpResponse(message)

            number_of_sections=data["number_of_sections"]
            
            course_obj=course.objects.filter(name=data["old_name"] , course_teacher=current_user)[0]
            course_obj.name=data["new_name"]
            course_obj.summary=data["summary"]
            course_obj.pre_movie=data["pre_movie"]
            course_obj.Headlines=data["Headlines"]
            
            course_obj.course_section_number=data["course_section_number"]
            
            course_obj.total_time_of_course=data["total_time_of_course"]
            
            course_obj.ref=data["ref"]
            course_obj.price=int(data["price"])
            course_obj.course_teacher=current_user
            course_obj.course_main_field=data["course_main_field"]
            
            course_obj.save()

            for i in range(1,number_of_sections+1):
                section_dict=data[str(i)]
                

                is_exist=section.objects.filter(part=i,course=course_obj).exists()

                if(is_exist==False):
                    message="not find session"
                    return HttpResponse(message)

                section_obj=section.objects.filter(part=i , course=course_obj)[0]

                section_obj.part=i

                section_obj.name=section_dict["name"]
                section_obj.movie=section_dict["movie"]
                section_obj.file=section_dict["file"]

                section_obj.course=course_obj
                section_obj.save()
                num=section_dict["number_of_exam_question"]
             

                for j in range(1,num+1):
                    info=section_dict["q_num_"+str(j)]
             
                    is_exist=question_exam.objects.filter(which_section=section_obj,number=j).exists()
                    if(is_exist==False):
                        continue
                    else:
                        q_obj=question_exam.objects.filter(which_section=section_obj,number=j)[0]
                        
                        q_obj.number=j#str(j)
                        
                        q_obj.question=info["question"]
                        q_obj.choice1=info["choice1"]
                        
                        q_obj.choice2=info["choice2"]
                        q_obj.choice3=info["choice3"]
                        q_obj.choice4=info["choice4"]
                        q_obj.true_choice=info["true_choice"]
                        q_obj.which_section=section_obj
                        q_obj.save()
                    
            message="edited"
            return HttpResponse(message)
        except:
            message="not_enough_data"
            return HttpResponse(message)
       
    else :
        message="bad request"
        return HttpResponse(message)    


'''
#api example for edition
{
    "1": {
        "part": 1,
        "name": "jalase 10",
        "movie": "",
        "file": "http://127.0.0.1:8000/media/anja/homayounshajaria-vataneman.mp3",
		"number_of_exam_question":2,
        "q_num_1": {
            "number": 1,
            "question": "soal1",
            "choice1": "111",
            "choice2": "22",
            "choice3": "33",
            "choice4": "44",
            "true_choice": 3
        },
        "q_num_2": {
            "number": 2,
            "question": "soal2",
            "choice1": "11",
            "choice2": "22",
            "choice3": "33",
            "choice4": "44",
            "true_choice": 2
        }
    },
    "2": {
        "part": 2,
        "name": "jalase 1",
        "movie": "",
        "file": "http://127.0.0.1:8000/media/anja/Tafseer_of_Sura_Maidah_5_Verse_103.pdf.pdf",
        "number_of_exam_question":2,
        "q_num_1": {
            "number": 1,
            "question": "soal1",
            "choice1": "11",
            "choice2": "22",
            "choice3": "33",
            "choice4": "44",
            "true_choice": 2
        },
        "q_num_2": {
            "number": 2,
            "question": "soal2",
            "choice1": "11",
            "choice2": "22",
            "choice3": "33",
            "choice4": "44",
            "true_choice": 2
        }
    },
    "number_of_sections":2,
    "old_name": "salaaaam",
    "new_name":"salaaaam",
    "summary": "yad midahad khiyli",
    "pre_movie": "",
    "Headlines": "",
    "course_section_number": 0,
    "total_time_of_course": 0,
    "ref": "",
    "price": 123,
    "course_main_field": ""
    
}
'''
