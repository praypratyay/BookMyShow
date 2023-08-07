from ..models import *

# Using Django ORMs via DAOs/Repositories
# Keeping query logic separate from models

class SeatRepository:

    def get_seats_by_ids(self, seat_ids):
        return Seat.objects.filter(id__in=seat_ids)
    
class ShowRepository:

    def get_show_by_id(self, show_id):
        return Show.objects.filter(id=show_id)

class ShowSeatRepository:

    """The select_for_update() function locks the database table rows 
       selected by the query until the end of transaction.
    """

    def get_all_showseats_by_seatsandshow(self, seats, show):
        return ShowSeat.objects.select_for_update().filter(seat__in=seats, show=show)

class UserRepository:

    def get_user_by_id(self, user_id):
        return User.objects.filter(id=user_id)