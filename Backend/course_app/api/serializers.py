from rest_framework.serializers import ModelSerializer
from  course_app.models import course,section

class CourseListSerializer(ModelSerializer):
    class Meta:
        model=course
        fields='__all__'

'''class SectionListSerializer(ModelSerializer):
    class Meta:
        model=section
        fields='__all__'
'''
