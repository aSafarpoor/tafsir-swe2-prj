from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from . import models
from course_app.models import course

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = '__all__'
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('id','email', 'username','picture')

class TeacherInfoSerializer(ModelSerializer):
    class Meta:
        model= models.CustomUser
        fields='__all__'
        #fields=('id','picture','introduction','case_history','first_name','last_name','course_counter')


class WhatPersonHave(ModelSerializer):
    class Meta:
        model = course
        fields = '__all__'
        # fields=('name','summary','picture')
class regserializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('email','username','password','phone_number')
