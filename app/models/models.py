from django.db import models
from django.utils import timezone

# Create your models here
# ORMs (Mapping from Classes to Schema)
# ForeignKey = ManyToOneRelationship
# CASCADE = Deleting entries in child table when parent is deleted

from .enums import *

class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    # Dont create this table. Keep it abstract
    class Meta:
        abstract = True

class City(BaseModel):
    name = models.CharField(max_length=255)

"""Note:
   Creating an object of Theatre is in turn also
   going to create an object of City in City Table too.
"""
class Theatre(BaseModel):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

# HACKING
class AuditoriumFeature(BaseModel):
    feature = models.CharField(max_length=255, choices=[(feature.name, feature.value) for feature in Feature])

# Can't have a relationship between models and enums so create a new model (HACKING)
class Auditorium(BaseModel):
    name = models.CharField(max_length=255)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    features = models.ManyToManyField(AuditoriumFeature)

# Club/Executive --- SILVER/GOLD/PLAT
class SeatType(BaseModel):
    seatTypeName = models.CharField(max_length=255)

class Seat(BaseModel):
    name = models.CharField(max_length=255)
    row = models.IntegerField()
    column = models.IntegerField()
    auditorium = models.ForeignKey(Auditorium, on_delete=models.CASCADE)
    seatType = models.ForeignKey(SeatType, on_delete=models.CASCADE)


# HACKING
class MovieLanguage(BaseModel):
    language = models.CharField(max_length=255, choices=[(language.name, language.value) for language in Language])

class Movie(BaseModel):
    name = models.CharField(max_length=255)
    rating = models.IntegerField() 
    languages = models.ManyToManyField(MovieLanguage)
    cast = models.CharField(max_length=255)

class Show(BaseModel):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    auditorium = models.ForeignKey(Auditorium, on_delete=models.CASCADE)
    startTime  = models.DateTimeField()
    endTime = models.DateTimeField()
    language = models.CharField(max_length=255, choices=[(language.name, language.value) for language in Language])

# Mapping Class
class ShowSeat(BaseModel):
    # DDLJ ---- A1 ---- AVL
    # DDLJ ---- A2 ---- OCC
    # DDLJ ---- A3 ---- AVL
    # K2H2 ---- A1 ---- AVL
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=[(seatstatus.name, seatstatus.value) for seatstatus in SeatStatus])
  

# Mapping Class
class ShowSeatType(BaseModel):
    # DDLJ ---- GOLD ---- 50
    # DDLJ ---- PLAT ---- 100
    # K2H2 ---- GOLD ---- 40
    # K2H2 ---- PLAT ---- 80
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    seatType = models.ForeignKey(SeatType, on_delete=models.CASCADE)
    price = models.FloatField()


class User(BaseModel):
    name = models.CharField(max_length=255) 
    age = models.IntegerField()  
    password = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.IntegerField() 
    
    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        print('Save method executed!')

class Ticket(BaseModel):
    amount = models.FloatField()   
    timeofBooking = models.DateTimeField()
    bookedby = models.ForeignKey(User, on_delete=models.DO_NOTHING) 
    show = models.ForeignKey(Show, on_delete=models.CASCADE) 
    ticketStatus = models.CharField(max_length=255, choices=[(ticketStatus.name, ticketStatus.value) for ticketStatus in TicketStatus])
    seats = models.ManyToManyField(Seat)

class Payment(BaseModel):
    amount = models.FloatField() 
    status = models.CharField(max_length=255, choices=[(paymentStatus.name, paymentStatus.value) for paymentStatus in PaymentStatus])
    type = models.CharField(max_length=255, choices=[(paymentType.name, paymentType.value) for paymentType in PaymentType])
    provider = models.CharField(max_length=255, choices=[(paymentProvider.name, paymentProvider.value) for paymentProvider in PaymentProvider])
    refID = models.CharField(max_length=255)
    time = models.DateTimeField()
    ticket = models.ForeignKey(Ticket, on_delete=models.DO_NOTHING) 
