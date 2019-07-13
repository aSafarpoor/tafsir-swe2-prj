from rest_framework.serializers import ModelSerializer
from image_file_test.models import image_file as imfi
from image_file_test.models import movie_link 
from drf_extra_fields.fields import Base64ImageField
import requests
import json

from moviepy.editor import *
import pygame

class CreateMember(ModelSerializer):
    class Meta:
        model = imfi
        fields = '__all__'


class MyImageModelSerializer(ModelSerializer):
    # picture=Base64ImageField()
    
    class Meta:
        model=imfi
        fields= ('name','picture')
    def create(self, validated_data):
        print("helloooo")
        try:
            picture=validated_data.pop('picture')
            print("sssssssssssssssssss")
            return imfi.objects.create(name=name,picture=picture)
        except:
            print("fuckkk   ")
            return imfi.objects.create(name=name)

'''

def call_aparat(movie,section_id):
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
        response = requests.get(address)
        data=json.loads(response.content)
        frm_id=data["uploadform"]["frm-id"]
    
    dat={}
    dat["video"]=movie

    dat["frm-id"]=frm_id
    dat["data[title]"]="title1"
    dat["data[category]"]="category1"
    dat["data[tags]"]="تست-ای \ی ای- اپارات"
    dat["data[comment]"]="no"
    dat["data[descr]"]="eeeeeeeeeeeee"
    r = json.dumps(dat)
    # print("\n\nbbbbbbbbbbbbbbbbbbbbb\n\n")
    # payload = {'number': 2, 'value': 1}





    headers = {'content-type': 'multipart/form-data'}

    response = requests.post(final_url, data=r,headers=headers)
    print("\n\n")
    print(str(response.content))
    print("\n\n")

   '''    

class tempModelSerializer(ModelSerializer):
    class Meta:
        model=movie_link
        fields= ('discription','movie','section_id')

    def create(self, validated_data):
        print("helloooo")
    
        movie=validated_data.pop('movie')
        section_id=validated_data.pop('section_id')
        # print(movie)
        # call_aparat(movie,section_id)
        #####
        '''try :  
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
            response = requests.get(address)
            data=json.loads(response.content)
            frm_id=data["uploadform"]["frm-id"]
        '''
        # formaction=data["uploadform"]["formAction"]
        # final_url=formaction

        dat={}
        # print(type(movie))
        # file = open("/home/ali/Videos/os_lab/1/insert.mp4","rb")
        dat["video"]=movie
        # print("\n\n")
        # print(type(movie))
        # # print("\n\n")
        dat["frm-id"]=20873  
        dat["data[title]"]="title1"
        dat["data[category]"]="category1"
        dat["data[tags]"]="تست-ای \ی ای- اپارات"
        dat["data[comment]"]="no"
        dat["data[descr]"]="eeeeeeeeeeeee"

        # print (dat)
        # r = json.dumps(dat)
        # print("\n\nbbbbbbbbbbbbbbbbbbbbb\n\n")
        # payload = {'number': 2, 'value': 1}
        # print(dat)
        final_url="https://www.aparat.com/etc/api/uploadpost/luser/amirmansoubi828/username/amirmansoubi828/ltoken/8061df45098379e19114ab01f4a9eb27/uploadid/3332608/atrty/1562744213/avrvy/977508/key/c1af3169a7ceecd955efe2897f2db1cdbe9dbc51/"
        
        # dat = json.dumps(dat)
        headers = {'content-type': 'multipart/form-data'}

        response = requests.post(final_url, data=dat,headers=headers)
        
        
        # response = requests.post(final_url, data=dat)
        print("\n\n")
        print(str(response.content))
        print("\n\n")

        #####
        discription="remove_it"
        # print("fuckkk   ")
        return movie_link.objects.create(discription=discription)



'''      
//////////////////////////////////////

        # data=json.loads(json_data)
        # data=(json_data)
        # section_id=23
        # msg=data["msg"]
           
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
            response = requests.get(address)
            data=json.loads(response.content)
            frm_id=data["uploadform"]["frm-id"]
        
        # msg["frm-id"]=frm_id

        # print(data)

        # return HttpResponse(str(data))
        formaction=data["uploadform"]["formAction"]
        # print("\n\n")
        # print(formaction)
        # print(type(formaction))
        # print('\n\n')   
        message=str(formaction)+"    "+str(frm_id)
        return HttpResponse(message)
    
        
        # base_url=formaction
        # final_url="/{0}/friendly/{1}/url".format(base_url,any_value_here)

        # payload = {'number': 2, 'value': 1}
        # response = requests.post(final_url, data=msg)
        # pritn(response)


/////////////////////////
'''