# Design BookMyShow (Low Level Design)

## **OVERVIEW**

> BookMyShow is an application generally used for booking movies/shows across different theatres in various cities. A person logs in into the app and books one/multiple tickets by selecting seats of one particular show. After confirming the seats, they make the payment and get the tickets.

<p>
    <img src="bookmyshow.jpg" width="800" height="500" />
</p>

We dont want just entities for this. We want to build an entire software system thats takes input. Persist data in a real database.
I will be using Django for this.

## Requirements and Clarifications

**Q) Does BookMyShow support mulliple cities?**

> _Yes._

**Q) Can one theatre have multiple auditoriums?**

> _Yes._

**Q) Can auditorium have different seating arrangement?**

> _Yes._

**Q) Can seats in an auditorium be of multiple types?**

> _Yes._

**Q) The price of a seat typically depends on time of a show, the theatre, the movie, or type of a seat. Is that the case here?**

> _Yes._

**Q) Will there be dynamic pricing i.e tickets becomes expensive if seats are less?**

> _No._

**Q) Are we allowing booking events as well?**

> _No, only support movies for now._

**Q) What all attributes of a movie we need to support?**

> _Rating. Cast. Features. Duration. Languages._

**Q) People should see all available movies in a city and then see the theatres which are playing that movie. Right?**

> _Yes._

**Q) Is only registered user allowed to book?**

> _Yes._

**Q) Is there a max limit on the no. of tickets one can book?**

> _Yes. Keep it 10._

**Q) Can a user book tickets for multiple shows at a time?**

> _No._

**Q) Are we supporting cancellation of a booking?**

> _Yes and they can get a refund._

**Q) Are we supporting booking food add-ons or discount coupons?**

> _No._

**Q) What mode of payment does it support?**

> _Online that is managed by 3rd Party._

## Classes - Attributes - Interfaces

### City
- ID
- Name
- Theatres (list of Theatre) 

### Theatre
- ID
- TheatreName
- Address
- Auditoriums (list of Auditorium) 

### Auditorium
- ID
- Name
- Seats (list of Seat)
- SupportedFeatures

### Feature
- 3D/2D/DOLBYAUDIO

### Seat
- ID
- SeatNumber
- Row
- Column
- SeatType

### SeatType
- ID
- SeatTypeName (Club/Exceutive)

### Show
- ID
- Movie
- Auditorium
- StartTime
- EndTime
- Features
- Language

### Movie
- ID
- Name
- Rating
- Languages
- Cast

### ShowSeatType (Mapping)
- ID
- Show
- SeatType
- Price

### ShowSeat (Mapping)
- ID
- Show
- Seat
- SeatStatus

### SeatStatus
- FREE/OCCUPIED/LOCKED

### Language
- ENGLISH/HINDI/TAMIL

### User
- ID
- Name
- Age
- Email
- Password
- Phone

### Ticket
- ID
- User
- BookingTime
- Show
- Amount
- Status
- Seats (list of Seat)
- Payments (list of Payment)

### TicketStatus
- BOOKED/CANCELLED

### Payment
- ID
- Amount
- PaymentProvider
- Type
- Status
- RefID
- Ticket

### PaymentType
- PAYING/REFUND

### PaymentStatus
- SUCCESSFULL/FAILED

### PaymentProvider
- RAZORPAY/PAYU

### PaymentGatewayAdapter

- #### RazorPayPaymentGatewayAdapter (PaymentGatewayAdapter)
- #### PayUPaymentGatewayAdapter (PaymentGatewayAdapter)

## Notes

- The seating arrangement across auditoriums can be very different. We implement this by a 100x100 Matrix (KISS - Keep It Simple, Stupid.) which stores seat information, and delete completely empty rows and columns. This is what is sent to frontend to visualize the seats.

- We are supporting concurrency in seat booking. Only one person is allowed to book seats at a time. We implement this by using soft locking :

    - Take DB lock
    - Get seats
    - Check seats status
    - If seats are not available, remove DB lock 
    - If every seat available, change seat status to LOCK and remove DB lock
    - Go to payment
    - Remove DB lock depending upon exit conditions


## Schema Design (TABLES)

### Django ORMs

## HOW TO RUN?

```python 
python3 manage.py migrate
python3 manage.py runserver 5555
```