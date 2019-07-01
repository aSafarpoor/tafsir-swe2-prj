from rest_framework import viewsets,generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from lopo import models
from lopo import serializer
import json
import requests
from django.shortcuts import render
from django.http import HttpResponse




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

# @api_view(['GET', 'POST'])
# def snippet_list(request):
#      """
#      List all code snippets, or create a new snippet.
#      """
#      if request.method == 'GET':
#          queryset = models.Note.objects.all()
#          serializer_class = serializer.NoteSerialiser
#         return HttpResponse("Salam")
#
#          return Response("salam")
#     if request.method == 'POST':
#          token="8061df45098379e19114ab01f4a9eb27"
#          queryset = models.Note.objects.all()
#          serializer_class = serializer.NoteSerialiser
#          url = "https://www.aparat.com/etc/api/uploadpost/luser/amirmansoubi828/username/amirmansoubi828/ltoken/8061df45098379e19114ab01f4a9eb27/uploadid/3805653/atrty/1562794979/avrvy/977508/key/3a189c6866d86c31c4f173edaae2e2be83636a5d/"
#         return HttpResponse("Salam")
