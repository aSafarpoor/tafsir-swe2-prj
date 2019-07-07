from rest_framework import generics
from course_app.models import course,section,question_exam
from image_file_test.models import image_file as imfi
#from serializers import CourseListSerializer
from  .serializers import CreateMember,MyImageModelSerializer

import requests
import json
from django.http import HttpResponse,JsonResponse
import base64



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

def call(request):
    if request.method=='GET':
        
        try :
            current_user = request.user

        except:
            message="not logged in"
            return HttpResponse(message)

        '''check if akhoond'''
        '''
        if current_user.teacher==True:
            pass

        else:
            message='not teacher'
            return HttpResponse(message)
        '''     

        # response = requests.get("https://www.aparat.com/etc/api/login/luser/amirmansoubi828/lpass/79e9feb0135e82cab14fed182ef0891b9920d641")
        # data=json.loads(response.content)
        # print(data,'\n\n')
        # token=data["login"]["ltoken"]
       
        try :  
            token="8061df45098379e19114ab01f4a9eb27"
            address="https://www.aparat.com/etc/api/uploadform/luser/amirmansoubi828/ltoken/"+token
            response = requests.get(address)
            data=json.loads(response.content)
            frm_id=data["uploadform"]["frm-id"]
            dict={}
            dict["frm-id"]=frm_id
            return JsonResponse(dict)
        
        except:
            response = requests.get("https://www.aparat.com/etc/api/login/luser/amirmansoubi828/lpass/79e9feb0135e82cab14fed182ef0891b9920d641")
            data=json.loads(response.content)
            token=data["login"]["ltoken"]
            address="https://www.aparat.com/etc/api/uploadform/luser/amirmansoubi828/ltoken/"+token
            response = requests.get(address)
            data=json.loads(response.content)
            frm_id=data["uploadform"]["frm-id"]
            dict={}
            dict["frm-id"]=frm_id
            return JsonResponse(dict)
        



    else:
        message='bad request'
        return HttpResponse(message)