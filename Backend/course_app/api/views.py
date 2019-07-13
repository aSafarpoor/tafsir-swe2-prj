from rest_framework import generics
from course_app.models import course,section,question_exam,file_pull
#from serializers import CourseListSerializer
from  .serializers import CourseListSerializer,fileListSerializer
import json
from django.http import HttpResponse
from users.models import CustomUser

class CourseListAPIview(generics.ListAPIView):
    queryset = course.objects.all()
    serializer_class = CourseListSerializer
'''class SectionListAPIview(generics.ListAPIView):
    queryset = section.objects.all()
    serializer_class = SectionListSerializer
'''
class FileCreateAPIview(generics.CreateAPIView):
    queryset = file_pull.objects.all()
    serializer_class = fileListSerializer

def create(request):
    # print("\nhellooooo\n\n\n")

    if request.method=="POST" or request.method=="OPTIONS":
        try:
            json_data=request.body
        except:
            message="bad urllll"
            return HttpResponse(message)
        # print(json_data)
        data=json.loads(json_data)
        # print("\n\n",data,"\n\n")
        # data=data["value"]
        # print("\n\n",data,"\n\n")
        # print("\n\n\n\ndata is:",data,"\n\n\n\n")

        try :
            # current_user = request.user
            ###############################
            # current_user = CustomUser.objects.all()[0]
            token=request.META["HTTP_TOKEN"]
            if(token[0]=="\""):
                token=token[1:-1]
            
            obj = Token.objects.filter(key=token)[0]
    
            current_user = models.CustomUser.objects.filter(id=obj.user_id)[0]
            # current_course=course.objects.filter( )
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
            
            try:
                number_of_sections=data["number_of_sections"]
            except:
                pass
            course_obj=course()
            try:
                course_obj.name=data["name"]
            except:
                pass
            try:
                course_obj.summary=data["summary"]
            except:
                pass
            try:
                course_obj.user_counter=0
            except:
                pass
            
            try:
                course_obj.course_section_number=number_of_sections
            except:
                pass
            try:
                course_obj.total_time_of_course=data["total_time_of_course"]
            except:
                pass
            try:
                course_obj.course_teacher=current_user
            except:
                pass
            try:
                course_obj.course_main_field=data["course_main_field"]
            except:
                pass
            
            try:
                course_obj.picture=data["picture"]["picture"]
            except:
                pass

            try:
                course_obj.save()
            except Exception as e:
                print(type(e))


            for i in range(1,number_of_sections+1):
                try:
                    section_dict=data[str(i)]
                except:
                    pass
                try:
                    section_obj=section()
                except:
                    pass
                try:
                    section_obj.part=i
                except:
                    pass
                try:
                    section_obj.name=section_dict["name"]
                except:
                    pass
                try:
                    section_obj.movie=section_dict["movie"]
                except:
                    pass
                try:
                    section_obj.file=section_dict["file"]
                except:
                    pass
                try:
                    section_obj.detail=section_dict["detail"]
                except:
                    pass
                try:
                    section_obj.course=course_obj
                except:
                    pass
                section_obj.save()
                try:
                    num=section_dict["number_of_exam_question"]
                except:
                    pass
                for j in range(1,num+1):
                    
                    info=section_dict[str(j)]
                    
                    q_obj=question_exam()
                    
                    q_obj.number=j#str(j)
                    try:
                        q_obj.question=info["question"]
                    except:
                        pass
                    try:
                        q_obj.choice1=info["choice1"]
                    except:
                        pass                
                    try:
                        q_obj.choice2=info["choice2"]
                    except:
                        pass
                    try:
                        q_obj.choice3=info["choice3"]
                    except:
                        pass
                    try:
                        q_obj.choice4=info["choice4"]
                    except:
                        pass
                    try:
                        q_obj.true_choice=info["true_choice"]
                    except:
                        pass
                    try:
                        q_obj.which_section=section_obj
                    except:
                        pass
                    q_obj.save()
                    
            message="created"
            return HttpResponse(message)
        except:
            message="not_enough_data"
            return HttpResponse(message)
       
    else :
        print("type is ",request.method)
        print("\n",request.body)
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



def edit(request):
    
    if request.method=="POST":
        try:
            json_data=request.body
        except:
            message="bad urllll"
            return HttpResponse(message)
        
        data=json.loads(json_data)

        try :
            # current_user = request.user
            token=request.META["HTTP_TOKEN"]
            if(token[0]=="\""):
                token=token[1:-1]
            
            obj = Token.objects.filter(key=token)[0]
    
            current_user = models.CustomUser.objects.filter(id=obj.user_id)[0]
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
                try:
                    section_obj.movie=section_dict["movie"]
                except:
                    pass
                try:
                    section_obj.file=section_dict["file"]["file"]
                except:
                    pass
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








''''


from rest_framework.serializers import ModelSerializer
from image_file_test.models import image_file as imfi
from image_file_test.models import movie_link 
from drf_extra_fields.fields import Base64ImageField
import requests
import json
from course_app.models import file_pull

from rest_framework.decorators import api_view


class MyImageModelSerializer(ModelSerializer):
    class Meta:
        model=file_pull
        fields= ['file']
    def create(self, validated_data):
        print("helloooo")
        file=validated_data.pop('file')
        return file_pull.objects.create(file=file)




@api_view(['GET', 'POST'])
def get_file_view(request):
    if request.method=="POST" :
        
        serializer = MyImageModelSerializer(data=request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            # oid=serializer.id
            oid=123
            message=str(oid)
            return HttpResponse(message)
        
        message="nokey"
        return HttpResponse(message)
    else:
        message="bad request"
        return HttpResponse(message)



#  obj=movie_link()        
#         obj.save()
#         obj_id=obj.id



'''

