from rest_framework import viewsets,generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from lopo import models
from lopo import serializer
import json
import requests
from django.shortcuts import render
from django.http import HttpResponse






@api_view(['GET', 'POST'])
def snippet_list(request):
     """
     List all code snippets, or create a new snippet.
     """
     if request.method == 'GET':
         queryset = models.Note.objects.all()
         serializer_class = serializer.NoteSerialiser
        return HttpResponse("Salam")

         return Response("salam")
    if request.method == 'POST':
         token="8061df45098379e19114ab01f4a9eb27"
         queryset = models.Note.objects.all()
         serializer_class = serializer.NoteSerialiser
         url = "https://www.aparat.com/etc/api/uploadpost/luser/amirmansoubi828/username/amirmansoubi828/ltoken/8061df45098379e19114ab01f4a9eb27/uploadid/3805653/atrty/1562794979/avrvy/977508/key/3a189c6866d86c31c4f173edaae2e2be83636a5d/"
        return HttpResponse("Salam")
