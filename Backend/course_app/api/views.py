from rest_framework import generics
from course_app.models import course
#from serializers import CourseListSerializer
from  .serializers import CourseListSerializer
from  .serializers import CourseListSerializer,CourseCreateSerializer


class CourseListAPIview(generics.ListAPIView):
    queryset = course.objects.all()
    serializer_class = CourseListSerializer


class CourseCreateAPIView(generics.CreateAPIView):
    # current_user = request.user
    # print (current_user.id)
    queryset = course.objects.all()
    serializer_class = CourseCreateSerializer
    #permission needed
    
def create(request):
    current_user = request.user
    print ("******************************************************************************",current_user.id)
    # file=open('a.txt','w')
    # file.write(str(current_user.id))
    # file.close()
    