from django.shortcuts import render
from rest_framework import viewsets,generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from lopo import models
from lopo import serializer
import json
import requests
from django.http import HttpResponse


@api_view(['GET', 'POST'])
def snippet_list(request):
     
     List all code snippets, or create a new snippet.
     """
     if request.method == 'GET':
         queryset = models.Note.objects.all()
         serializer_class = serializer.NoteSerialiser

         return Response("salam")

