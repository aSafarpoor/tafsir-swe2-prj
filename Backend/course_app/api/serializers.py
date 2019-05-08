from rest_framework.serializers import ModelSerializer
from  course_app.models import course

class CourseListSerializer(ModelSerializer):
    class Meta:
        model=course
        fields='__all__'

