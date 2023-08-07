from ..services import *

# Works like request/response DTOs
class UserMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        self.user_service = UserService()
        print("-----<<<<<UserMiddleWare INITIALIZED>>>>-----")

    def __call__(self, request):
        request.user_service = self.user_service
        response = self.get_response(request)
    
        print("UserMiddleware REQUEST  = ", request)
        print("UserMiddleware RESPONSE = ", response)
        return response
