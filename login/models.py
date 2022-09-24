from django.db import models

# Create your models here.

class Flightdetails(models.Model):
    Fnumber= models.CharField(unique=True, max_length=10)
    coname= models.CharField(max_length=15)
    fromdestination=models.CharField(max_length=15)
    todestination=models.CharField(max_length=15)
    nooftickets=models.IntegerField()
    boardingTime = models.TimeField(blank=True, null=True)
    arrivalTime = models.TimeField(blank=True, null=True)
    flight_fare = models.FloatField(blank=True,null=True)

    def __str__(self):
        return f"{self.Fnumber}, {self.coname}, {self.fromdestination}, {self.todestination}"

class leaves(models.Model):
    Username=models.TextField()
    User_Id=models.CharField(unique=True,max_length=20)
    Mobile=models.IntegerField()
    Email=models.EmailField()
    Start_date=models.DateField()
    End_date=models.DateField()
    comments=models.TextField()   


class payment(models.Model):
    Name_on_Card =models.TextField()
    CardNumber =models.IntegerField(unique=True)
    ExpDate=models.DateField()
    cvv=models.IntegerField()

class Ticket_Details(models.Model):
    BookingUser = models.CharField(max_length=10)
    Passengers = models.TextField()
    TicketNumber = models.CharField(max_length=10, unique=True)
    FlightNumber = models.CharField(max_length=6)
    FlightDate = models.CharField(max_length=15)
    Email = models.EmailField()
    Status = models.CharField(max_length=20)
    BookingDate = models.CharField(max_length=15)
    BookingTime = models.CharField(max_length=10)
    FlightBoarding = models.CharField(max_length=10)
    Mobile = models.IntegerField()
    FlightName = models.CharField(max_length=20)
    FlightArrival = models.CharField(max_length=10)
    FlightFrom = models.CharField(max_length=20)
    FlightTo = models.CharField(max_length=20)
    FlightFare = models.FloatField()
    FlightCharges = models.FloatField()
    TotalFare = models.FloatField()
    PassengerCount = models.IntegerField()
    DiscountAmount = models.CharField(max_length=15)

    
class Discount(models.Model):
    Coupon_Code=models.CharField(max_length=20) 
    Offer_Ammount=models.FloatField(max_length=20)   
    
class Seat_Choice(models.Model):
    seat_no=models.CharField(max_length=20) 
    seat_class=models.CharField(max_length=20)