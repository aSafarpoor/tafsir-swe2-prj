from rest_framework import generics
from course_app.models import course,section,question_exam
from image_file_test.models import image_file as imfi 
from image_file_test.models import movie_link
#from serializers import CourseListSerializer

from django.core import serializers

from  .serializers import CreateMember,MyImageModelSerializer,tempModelSerializer

import requests
import json
from django.http import HttpResponse,JsonResponse
import base64

from rest_framework import generics
from course_app.models import course,section,question_exam
#from serializers import CourseListSerializer

import json
from django.http import HttpResponse




class create1(generics.CreateAPIView):
    queryset = imfi.objects.all()
    serializer_class = CreateMember

class ListAPIview(generics.ListAPIView):
    queryset = imfi.objects.all()
    serializer_class = CreateMember




from rest_framework.decorators import api_view
@api_view(['GET', 'POST'])
def create0(request):
    if request.method=="POST" :
        
        serializer = MyImageModelSerializer(data=request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            
            message="ok"
            return HttpResponse(message)
        
        message="nokey"
        return HttpResponse(message)
    else:
        message="bad request"
        return HttpResponse(message)

def get_movie_id(request):
    if request.method=='GET':
        
        try:
            json_data=request.body
        except:
            message="bad urllll"
            return HttpResponse(message)
        '''
        try :
            current_user = request.user
        except:
            message="not logged in"
            return HttpResponse(message)
        
        if(current_user.teacher==False):
            message="not teacher"
            return HttpResponse(message)
        '''
        obj=movie_link()        
        obj.save()
        obj_id=obj.id
        dict={}
        dict["id"]=obj_id

        return JsonResponse(dict)
    message="bad request"
    return HttpResponse(message)



@api_view(['GET', 'POST'])
def call(request):
    if request.method=="POST" :
        
        '''
        try :
            current_user = request.user
        except:
            message="not logged in"
            return HttpResponse(message)
        
        if(current_user.teacher==False):
            message="not teacher"
            return HttpResponse(message)
        '''
        serializer = tempModelSerializer(data=request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            
            message="ok"
            return HttpResponse(message)
        
        message="nokey"
        return HttpResponse(message)
    else:
        message="bad request"
        return HttpResponse(message)




'''

@api_view(['GET', 'POST'])
def call(request):
    if request.method=='POST' or request.method=='GET':
        
        # print(request.data)

             
        try :
            current_user = request.user
        except:
            message="not logged in"
            return HttpResponse(message)
        
        if(current_user.teacher==False):
            message="not teacher"
            return HttpResponse(message)
        
        
        if False :
            pass
        else:
            # msg=serializer.save()
            # print("Fukkkkkkkkkkkkkkkkkkkkkkkkkk")
            msg=request.data
            # msg=msg[0]
            print(msg)
            print("\n\n")
            
            try :  
                token="8061df45098379e19114ab01f4a9eb27"
                address="https://www.aparat.com/etc/api/uploadform/luser/amirmansoubi828/ltoken/"+token
                response = requests.get(address)
                data=json.loads(response.content)
                frm_id=data["uploadform"]["frm-id"]
            
            except:
                response = requests.get("https://www.aparat.com/etc/api/login/luser/amirmansoubi828/lpass/79e9feb0135e82cab14fed182ef0891b9920d641")
                data=json.loads(response.content)
                token=data["login"]["ltoken"]
                address="https://www.aparat.com/etc/api/uploadform/luser/amirmansoubi828/ltoken/"+token


            

            # response = requests.get(address)
            # data=json.loads(response.content)
            # frm_id=data["uploadform"]["frm-id"]
            
            # msg["frm-id"]=frm_id

            # print(data)
            
            final_url="https://www.aparat.com/etc/api/uploadpost/luser/amirmansoubi828/username/amirmansoubi828/ltoken/8061df45098379e19114ab01f4a9eb27/uploadid/9331616/atrty/1562619001/avrvy/977508/key/05f962bbdb0e2fd7455bf6a712416a3b75bf54e7/"


            
           
            response = requests.post(final_url, data=msg)
            print("\n\n")
            print(str(response.content))
            print("\n\n")
                
        message="ok"
        return HttpResponse(message)
            
            # message="nokey"
            # return HttpResponse(message)
    else:
        message="bad request"
        return HttpResponse(message)


'''