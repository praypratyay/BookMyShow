from enum import Enum

class Feature(Enum):
    THREE_D = 1 
    TWO_D = 2
    DOLBY_AUDIO = 3

class Language(Enum):
    ENGLISH = 1
    HINDI = 2 
    TAMIL = 3

class SeatStatus(Enum):
    FREE = 1
    OCCUPIED = 2
    LOCKED = 3

class TicketStatus(Enum):
    BOOKED = 1
    PROCESSING = 2
    CANCELLED = 3

class PaymentType(Enum):
    MONEY = 1
    REFUND = 2
    DISCOUNT = 3

class PaymentStatus(Enum):
    SUCCESSFULL = 1
    FAILED = 2 

class PaymentProvider(Enum):
    RAZORPAY = 1
    PAYU = 2 


