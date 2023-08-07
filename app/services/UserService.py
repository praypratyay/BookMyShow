from django.contrib.auth.hashers import make_password
from ..models import *
from ..repositories import *

class UserService:

    def signupUser(self, email, password):
        
        encryptedpassword = make_password(password)
    
        print("XXXXXXXXXXXXXXXXXXXXXXXXXX")
        user = User()
        user.name = email
        user.password = encryptedpassword
        #user2 = User.objects.create(email = email, password = password)
        print("OOOOOOOOOOOOOOOOOOOOO")
        user.save()
        print("-------------")

        return user
