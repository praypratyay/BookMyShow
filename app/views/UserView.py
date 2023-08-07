from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from ..services import *

# Create your views/controllers here
class UserView(View):

    def get(self, request):

        email = request.GET.get("email")
        password = request.GET.get("password")
        print("USER EMAIL = ", email)

        try:
            user  = request.user_service.signupUser(email, password)
            return user
        except:
            return HttpResponse("---Some Exception Occured---")