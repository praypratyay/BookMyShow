from django.db import transaction
from ..models import *
from ..repositories import *
from .TicketPriceCalcService import *

class BookTicketService:

    def __init__(self):
        self.seatRepo = SeatRepository()
        self.showRepo = ShowRepository()
        self.showseatRepo = ShowSeatRepository()
        self.userRepo = UserRepository()

    """ Atomicity is the defining property of database transactions. 
        atomic allows us to create a block of code within which the atomicity on the database is guaranteed. 
        If the block of code is successfully completed, the changes are committed to the database. 
        If there is an exception, the changes are rolled back.
    """
    @transaction.atomic
    # Any db call with select_for_update() that is inside this function, we take the LOCK.
    def book_ticket(self, seat_ids, show_id, user_id):

        seats = self.seatRepo.get_seats_by_ids(seat_ids)
        show = self.showRepo.get_show_by_id(show_id)
        user = self.userRepo.get_user_by_id(user_id)

        # LOCK TAKEN HERE (for those rows)
        show_seats = self.showseatRepo.get_all_showseats_by_seatsandshow(seats, show)

        # We can also use transaction.atomic() as context manager via with statement to lock only some lines that we want to.
        for show_seat in show_seats:
            if show_seat.status != SeatStatus.FREE:
                # Note: We can have custom exceptions as well (Good Practice)
                raise Exception("SEAT NOT AVAILABLE")

        for show_seat in show_seats:
            show_seat.status = SeatStatus.LOCKED
            # Note: We can create save functions inside repositories (Good Practice)
            show_seat.save()
        
        
        ticket = Ticket()
        ticket.ticketStatus = TicketStatus.PROCESSING
        ticket.show = show
        ticket.seats = seats
        ticket.bookedby = user
        ticket.amount = TicketPriceCalcService().ticket_calculator()
        ticket.save()
        
        return ticket
    # LOCK RELEASED HERE