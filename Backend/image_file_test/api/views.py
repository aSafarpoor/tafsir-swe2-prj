from rest_framework import generics
from course_app.models import course,section,question_exam
from image_file_test.models import image_file as imfi
#from serializers import CourseListSerializer
from  .serializers import CreateMember,MyImageModelSerializer

import json
from django.http import HttpResponse
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

