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
        mydata = {"teacher": self.user.teacher,
            "student" : self.user.student
        }
        orginal_response.data.update(mydata)
        return orginal_response
