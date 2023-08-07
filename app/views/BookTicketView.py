from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from ..services import *

# Create your views/controllers here
class BookTicketView(View):

    def get(self, request):

        seat_ids = request.GET.get("seat_ids")
        show_id = request.GET.get("show_id")
        user_id = request.GET.get("user_id")

        try:
            ticket  = request.book_ticket_service.book_ticket(seat_ids, show_id, user_id)
            print(ticket.show.id)
            return ticket

        except:
            return HttpResponse("---Some Exception Occured---")