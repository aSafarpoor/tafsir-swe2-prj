from django.shortcuts import render
from rest_auth.views import LoginView
# Create your views here.

class CustomLoginView(LoginView):
#         content = {
#             'user': unicode(request.user),  # `django.contrib.auth.User` instance.
#             'auth': unicode(request.auth),  # None
#         }
    def get_response(self):
        orginal_response = super().get_response()
        teacher = self.user.teacher
        student =  self.user.student

        if teacher == True and student == True:
            user = "student and teacher"

        if teacher and not student:
            user = "teacher"

        if not teacher and student:
            user = "student"
        if not teacher and not student :
            user = "nothing"

        mydata = {"type": user,
        }
        orginal_response.data.update(mydata)
        return orginal_response
