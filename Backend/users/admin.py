from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from course_app.models import course
from course_app.models import who_has_what
#class CustomUserAdmin(UserAdmin):
    #add_form = CustomUserCreationForm
    #form = CustomUserChangeForm
    #model = CustomUser
    #list_display = ['email', 'username', 'name' ]

admin.site.register(CustomUser)#, CustomUserAdmin
admin.site.register(course)
admin.site.register(who_has_what)
