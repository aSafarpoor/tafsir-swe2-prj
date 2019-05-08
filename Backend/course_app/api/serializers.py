from rest_framework.serializers import ModelSerializer
from  course_app.models import course

class CourseListSerializer(ModelSerializer):
    class Meta:
        model=course
        fields='__all__'

class CourseCreateSerializer(ModelSerializer):
    class Meta:
        model = course
        fields = ( 'name', 'summary','pre_movie','Headlines','course_section_number','total_time_of_course','ref','price','all_text_content','exam','course_teacher','course_main_field')
        #fields='__all__'