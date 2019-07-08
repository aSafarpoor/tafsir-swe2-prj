from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from image_file_test.models import image_file,movie_link
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from aboutus_app.models import aboutus,contactus,news
from course_app.models import course,section
from course_app.models import who_has_what,question_exam
#class CustomUserAdmin(UserAdmin):
    #add_form = CustomUserCreationForm
    #form = CustomUserChangeForm
    #model = CustomUser
    #list_display = ['email', 'username', 'name' ]

admin.site.register(CustomUser)#, CustomUserAdmin
admin.site.register(course)
admin.site.register(question_exam)
admin.site.register(section)
admin.site.register(who_has_what)
admin.site.register(image_file)
admin.site.register(aboutus)
admin.site.register(news)
admin.site.register(movie_link)
admin.site.register(contactus)
