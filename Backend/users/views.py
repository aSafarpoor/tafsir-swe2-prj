from rest_framework import generics
from .serializers import TeacherInfoSerializer,WhatPersonHave,TeacherInfoSerializer

from . import models
from . import serializers
from course_app.models import course
from users.models import CustomUser
class UserListView(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer


class TeacherDetailsAPIView(generics.RetrieveAPIView):
    #session = Session.objects.get(session_key=session_key)
    lookup_field = 'id'
    queryset = CustomUser.objects.all()
    serializer_class = TeacherInfoSerializer

class JoinTable(generics.ListAPIView):
    serializer_class =  WhatPersonHave

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        choosed_id = self.kwargs['choosed_id']
        return course.objects.filter(course_teacher=choosed_id)