from rest_framework import generics

from django.http import HttpResponse
from aboutus_app.models import aboutus,contactus,news
# from  .serializers import CreateSerializer,ListSerializer,EditSerializer
from  .serializers import ListSerializer,contactSerializer,newsSerializer
import json
from rest_framework.decorators import api_view

# class CreateAPIview(generics.CreateAPIView):
#     queryset = aboutus.objects.all()
#     serializer_class = CreateSerializer

# class EditAPIview(generics.RetrieveUpdateAPIView):#     CreateAPIView):
#     lookup_field = 'id'
#     queryset = aboutus.objects.all()
#     serializer_class = EditSerializer

class ListAPIview(generics.ListAPIView):
    queryset = aboutus.objects.all()
    serializer_class = ListSerializer


class contactAPIview(generics.CreateAPIView):
    queryset = contactus.objects.all()
    serializer_class = contactSerializer



class newsAPIview(generics.ListAPIView):
    queryset = news.objects.all()
    serializer_class = newsSerializer

# @api_view(['GET', 'POST'])
# def CreateAPIview(request):
#     if request.method=="POST" :
        
#         serializer = CreateSerializer(data=request.data)
    
#         try :
#             current_user = request.user
#         except:
#             message="not logged in"
#             return HttpResponse(message)
        
#         # if current_user.is_superuser:
#         #     pass
#         # else:
#         #     message="access denied"
#         #     return HttpResponse(message)



#         if serializer.is_valid():
            
#             serializer.save()
#             message="ok"
#             return HttpResponse(message)
        
#         message="nokey"
#         return HttpResponse(message)

# @api_view(['GET', 'POST'])
# def EditAPIview(request):
#      if request.method=="POST" :
        
#         serializer = EditSerializer(data=request.data)
        

#         try :
#             current_user = request.user
#         except:
#             message="not logged in"
#             return HttpResponse(message)
#         if current_user.is_superuser:
#             pass
#         else:
#             message="access denied"
#             return HttpResponse(message)

#         if serializer.is_valid():
            
#             serializer.save()
#             message="ok"
#             return HttpResponse(message)
        
#         message="nokey"
#         return HttpResponse(message)