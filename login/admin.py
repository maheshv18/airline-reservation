from django.contrib import admin

from login.models import Flightdetails, Ticket_Details, leaves, Discount, Seat_Choice


# Register your models here.
admin.site.register(Flightdetails, list_display = ["Fnumber", "coname", "fromdestination", "todestination", "flight_fare"])
admin.site.register(leaves)
admin.site.register(Ticket_Details, list_display = ["TicketNumber", "BookingUser", "FlightFrom", "FlightTo", "TotalFare"])
admin.site.register(Discount)
admin.site.register(Seat_Choice)




