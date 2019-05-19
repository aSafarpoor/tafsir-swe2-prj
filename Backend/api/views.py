from django.shortcuts import render

# Create your views here.

class CustomLoginView(LoginView):
#         content = {
#             'user': unicode(request.user),  # `django.contrib.auth.User` instance.
#             'auth': unicode(request.auth),  # None
#         }
    def get_response(self):
        orginal_response = super().get_response()
        mydata = {"message": "some message"}
        orginal_response.data.update(mydata)
        return orginal_response
