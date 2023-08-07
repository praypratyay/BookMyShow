from ..services import *

# Works like request/response DTOs
class BookTicketMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        self.book_ticket_service = BookTicketService()
        print("-----<<<<<BookTicket MiddleWare INITIALIZED>>>>-----")

    def __call__(self, request):
        request.book_ticket_service = self.book_ticket_service
        response = self.get_response(request)
    
        print("BookTicketMiddleware REQUEST  = ", request)
        print("BookTicketMiddleware RESPONSE = ", response)
        return response
