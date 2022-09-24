from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate
from .models import Flightdetails,leaves, Discount
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa 
from . models import Ticket_Details
import datetime
from django.db import IntegrityError
x = datetime.datetime.now()

def html_to_pdf(template_src, context_dict={}):
     template = get_template(template_src)
     html  = template.render(context_dict)
     result = BytesIO()
     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
     if not pdf.err:
         return HttpResponse(result.getvalue(), content_type='application/pdf')
     return None

def logins(request):

    if request.method == "POST":
        username =request.POST['username']
        password =request.POST['pass']

        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print('User logged in successful')
            return redirect('/login/booking')
        else:
            messages.info(request,'invalid credentials')
            print('Invalid credentials')
            return redirect('/login/login')    
    else:
        return render(request,'login/login.html')

def register(request):
    
    if request.method == "POST":
        first_name =request.POST['firstname']
        last_name =request.POST['lastname']
        username =request.POST['username']
        password =request.POST['pass']
        password1 =request.POST['pass1']
        email =request.POST['email']
        if password == password1:
            if User.objects.filter(username=username).exists():

                print('Username Exists or taken')
                messages.info(request,'Username already Exits')
                return redirect('/login/register')
                
                

            elif User.objects.filter(email=email).exists():
                print('Email already Exists')
                messages.info(request,'Email already Exits')
                return redirect('/login/register')
                
            else:
                user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('Account created') 
                return redirect('/login/booking')

        else:
            print('password not matching')
            messages.info(request,'password not matching')
            return redirect('/login/register')
            
    
    else:
        return render(request,'login/register.html')
    

def logout(request):
    auth.logout(request)
    return render(request,'login/booking.html')
       

def feedback(request):
    return render(request,'login/feedback.html')

def explore(request):
    return render(request,'login/Explore.html')

    
def flightdetails(request):
    
    if request.method == 'POST':
        flightDetails=Flightdetails()
        flightDetails.Fnumber= request.POST.get('Fnumber')
        flightDetails.coname= request.POST.get('coname')
        flightDetails.fromdestination= request.POST.get('fromdest')
        flightDetails.todestination= request.POST.get('todest')
        flightDetails.nooftickets= request.POST.get('nooftickets')
        flightDetails.save();    
        print('Flight details saved')    
        
        # return render(request,'login/flightdetails.html')     

    else:
        print('flight details not yet saved 1')
        return render(request,'login/flightdetails.html')
           
    return render(request,'login/flightdetails.html')     

def booking(request):
    return render(request,'login/booking.html')  


def faq(request):
    return render(request,'login/faq.html')        

def contact(request):
    return render(request,'login/contact.html')  

def discount(request):
    if request.method == 'POST':
        
        discount1=Discount()
        discount1.Coupon_Code= request.POST.get('coupon_code')
        discount1.Offer_Ammount= request.POST.get('amount')
        discount1.save()

        request.session['discountCoupon'] = request.POST.get('coupon_code')
        request.session['discountAmt'] = request.POST.get('amount') 
        
        return render(request,'login/booking.html')  
    return render(request,'login/discount.html')

def leave(request):
    if request.method == 'POST':
        Leaves=leaves()
        Leaves.Username= request.POST.get('username')
        Leaves.User_Id= request.POST.get('userid')
        Leaves.Mobile= request.POST.get('Mobilenumber')
        Leaves.Email= request.POST.get('Email')
       
        Leaves.Start_date= request.POST.get('sdate')
        Leaves.End_date= request.POST.get('edate')
        Leaves.comments= request.POST.get('comments')
        Leaves.save()
        print('leave details saved')
        return render(request,'login/leave.html') 
    else:
        print('leave details not updated')
        return render(request,'login/leave.html') 
         

def payment(request):    
    if request.method == 'POST':
            mobile = request.POST['mobile']
            email = request.POST['email']
            passengerscount = request.POST['passengersCount']
            fNameArr=[];lNameArr=[];genderArr=[]
            for i in range(1,int(passengerscount)+1):
                fname = request.POST[f'passenger{i}FName']
                lname = request.POST[f'passenger{i}LName']
                gender = request.POST[f'passenger{i}Gender']
                fNameArr.append(fname)
                lNameArr.append(lname)
                genderArr.append(gender.upper())

            request.session['fNameArr'] = fNameArr
            request.session['lNameArr'] = lNameArr
            request.session['gender'] = genderArr

            totalFare = request.session.get('totalAmt')

            request.session['email'] = email
            request.session['mobile'] = mobile
            request.session['passCnt'] = passengerscount

            totalFare *= float(passengerscount)
            
            request.session['totalFare'] = totalFare
            return render(request, 'login/payment.html', {
                'totalFare': totalFare
            })
    

def seat(request):
    return render(request,'login/seat.html')

def getFlights(request):
    if request.method == 'POST':
        flighttable = Flightdetails.objects.all()
        origin = request.POST.get('from')
        destination = request.POST.get('to')
        date = request.POST.get('departure')
        print(origin, destination)
        return render(request, 'login/flights.html',{
            'origin': origin, 
            'destination': destination,
            'date': date,
            'flighttable': flighttable
        })
    else: 
        return render(request,'login/flights.html') 

def book(request):
    flightNumber = request.POST.get('fID')
    flightDate = request.POST.get('fDate')
    flightCompany = request.POST.get('fCompany')
    flightFrom = request.POST.get('fFrom')
    flightTo = request.POST.get('fTo')
    flightFare = request.POST.get('fFare')
    flightBoarding = request.POST.get('fBoardingTime')
    flightArrival = request.POST.get('fArrivalTime')
    flightFee = 300
    request.session['flightNumber'] = flightNumber
    request.session['flightDate'] = flightDate
    request.session['flightCompany'] = flightCompany
    request.session['flightFrom'] = flightFrom
    request.session['flightTo'] = flightTo
    request.session['flightFare'] = flightFare
    request.session['flightBoarding'] = flightBoarding
    request.session['flightArrival'] = flightArrival
    request.session['flightFee'] = flightFee

    try:
        discountCoupon = request.session.get('discountCoupon')
        discountAmt = request.session.get('discountAmt')
        totalAmt = (float(flightFare) + float(flightFee)) - float(discountAmt)
    except TypeError:
        discountCoupon = 'N/A'
        discountAmt = float(0)
        totalAmt = (float(flightFare) + float(flightFee)) - float(discountAmt)

    print(totalAmt, discountAmt, discountCoupon)

    request.session['totalAmt'] = totalAmt

    return render(request, 'login/book.html', {
        'flightNumber': flightNumber, 
        'flightDate': flightDate, 
        'flightCompany': flightCompany, 
        'flightFrom': flightFrom, 
        'flightTo': flightTo, 
        'flightFare': flightFare, 
        'flightBoarding':flightBoarding, 
        'flightArrival': flightArrival,
        'flightFee': flightFee,
        'flightDiscount': discountAmt,
        'couponCode': discountCoupon,
        'flightFareTotal': totalAmt,
    })

def ticket(request):
    fN = request.session.get('flightNumber')
    bT = x.strftime("%H")+':'+x.strftime("%M")+':'+x.strftime("%S")
    bD = x.strftime("%d")+'-'+x.strftime("%m")+'-'+x.strftime("%Y")
    fD = request.session.get('flightDate')
    fC = request.session.get('flightCompany')
    fF = request.session.get('flightFrom')
    fT = request.session.get('flightTo')
    fFare = request.session.get('flightFare')
    fB = request.session.get('flightBoarding')
    fA = request.session.get('flightArrival')
    fFee = request.session.get('flightFee')
    tFee = request.session.get('totalFare')
    email = request.session.get('email')
    mobile = request.session.get('mobile')

    tktNum = request.session.get('tktNum')
    passCnt = request.session.get('passCnt')

    fname = request.session.get('fNameArr')
    lname = request.session.get('lNameArr')
    gender = request.session.get('gender')
    passArr = zip(fname, lname, gender)

    discountAmt = request.session.get('discountAmt')

    try:
        tickDet = Ticket_Details()
        
        arr = []
        for i, j, k in zip(fname, lname, gender):
            arr.append(f"{i} {j} - {k}")

        tickDet.BookingUser = request.user
        tickDet.Passengers = arr
        tickDet.FlightNumber = fN
        tickDet.FlightDate = fD
        tickDet.Email = email
        tickDet.Status = 'CONFIRMED'
        tickDet.BookingDate = bD
        tickDet.BookingTime = bT
        tickDet.FlightBoarding = fB
        tickDet.FlightArrival = fA
        tickDet.Mobile = mobile
        tickDet.TicketNumber = tktNum
        tickDet.FlightName = fC
        tickDet.FlightFrom = fF
        tickDet.FlightTo = fT
        tickDet.FlightFare = fFare
        tickDet.FlightCharges = fFee
        tickDet.TotalFare = tFee
        tickDet.PassengerCount = passCnt
        tickDet.DiscountAmount = discountAmt
        tickDet.save()
    except IntegrityError:
        pass

    data = {
        'flightNumber': fN, 
        'bookingDate': bD,
        'bookingTime': bT,
        'flightDate': fD, 
        'flightCompany': fC, 
        'flightFrom': fF, 
        'flightTo': fT, 
        'flightFare': fFare, 
        'flightBoarding':fB, 
        'flightArrival': fA,
        'flightFee': fFee,
        'email': email,
        'mobile': mobile,
        'totalFee': tFee,
        'passArr': passArr,
        'tktNum': tktNum,
        'flightDiscount': discountAmt
    }

    return render(request, 'login/ticket.html', data)

def payment_process(request):
    fN = request.session.get('flightNumber')
    mobile = request.session.get('mobile')
    tktNum = fN[0:3] + mobile[0:4] + fN[3:6]
    request.session['tktNum'] = tktNum
    mobile = request.session.get('mobile')
    tktNum = request.session.get('tktNum')
    fF = request.session.get('flightFrom')
    fT = request.session.get('flightTo')
    return render(request,'login/payment_process.html',{
        'flightFrom': fF, 
        'flightTo': fT,
        'tktNum': tktNum
    })


def downloadTicket(request):
    fN = request.session.get('flightNumber')
    bT = x.strftime("%H")+':'+x.strftime("%M")+':'+x.strftime("%S")
    bD = x.strftime("%d")+'-'+x.strftime("%m")+'-'+x.strftime("%Y")
    fD = request.session.get('flightDate')
    fC = request.session.get('flightCompany')
    fF = request.session.get('flightFrom')
    fT = request.session.get('flightTo')
    fFare = request.session.get('flightFare')
    fB = request.session.get('flightBoarding')
    fA = request.session.get('flightArrival')
    fFee = request.session.get('flightFee')
    tFee = request.session.get('totalFare')
    email = request.session.get('email')
    mobile = request.session.get('mobile')

    fname = request.session.get('fNameArr')
    lname = request.session.get('lNameArr')
    gender = request.session.get('gender')
    passArr = zip(fname, lname, gender)

    passCnt = request.session.get('passCnt')
    tktNum = request.session.get('tktNum')

    discountAmt = request.session.get('discountAmt')

    try:
        tickDet = Ticket_Details()
        
        arr = []
        for i, j, k in zip(fname, lname, gender):
            arr.append([f"{i} {j} - {k}"])

        tickDet.BookingUser = request.user
        tickDet.Passengers = arr
        tickDet.FlightNumber = fN
        tickDet.FlightDate = fD
        tickDet.Email = email
        tickDet.Status = 'CONFIRMED'
        tickDet.BookingDate = bD
        tickDet.BookingTime = bT
        tickDet.FlightBoarding = fB
        tickDet.FlightArrival = fA
        tickDet.Mobile = mobile
        tickDet.TicketNumber = tktNum
        tickDet.FlightName = fC
        tickDet.FlightFrom = fF
        tickDet.FlightTo = fT
        tickDet.FlightFare = fFare
        tickDet.FlightCharges = fFee
        tickDet.TotalFare = tFee
        tickDet.PassengerCount = passCnt
        tickDet.DiscountAmount = discountAmt
        tickDet.save()
    except IntegrityError:
        pass

    data = {
        'flightNumber': fN, 
        'bookingDate': bD,
        'bookingTime': bT,
        'flightDate': fD, 
        'flightCompany': fC, 
        'flightFrom': fF, 
        'flightTo': fT, 
        'flightFare': fFare, 
        'flightBoarding':fB, 
        'flightArrival': fA,
        'flightFee': fFee,
        'email': email,
        'mobile': mobile,
        'totalFee': tFee,
        'passArr': passArr,
        'tktNum': tktNum,
        'flightDiscount': discountAmt
    }
    pdf = html_to_pdf('login/ticket.html', data)
    return HttpResponse(pdf, content_type='application/pdf')

def dashboard(request):
    ticket = Ticket_Details.objects.all()
    return render(request, 'login/dashboard.html', {
        "ticket": ticket
    })

def showTicket(request):
    ticket_number = request.POST.get('tickNum')
    ticket = Ticket_Details.objects.all()
    for i in ticket:
        if ticket_number == str(i.TicketNumber):
            ticket = i
    splitArr = (ticket.Passengers.split(", "))
    pdf = html_to_pdf('login/showticket.html', { "ticket": ticket, "splitArr": splitArr })
    return HttpResponse(pdf, content_type='application/pdf')
        
def cancelTicket(request):
    ticket_number = request.POST.get('tickNumb')
    Ticket_Details.objects.filter(TicketNumber = ticket_number).delete()
    ticket = Ticket_Details.objects.all()
    return render(request, 'login/dashboard.html', {"ticket": ticket})

def details(request):
    return render(request, 'login/details.html')

def details_update(request):
    if request.method == "POST":
        userupdate = request.POST['userupdate']
        first_name =request.POST['firstname']
        last_name =request.POST['lastname']
        email =request.POST['email']
        user1 = User.objects.all()

        for i in user1:
            if userupdate == i.username:
                user = User.objects.filter(username=userupdate).update(email=email,first_name=first_name,last_name=last_name)
                print('Account saved') 
                return redirect('/login/details')

        
        else:
            return redirect('/login/details')  
        
    else:
        return render(request,'login/details_update.html') 

def ticketStatus(request):
    if request.method == 'POST':
        ticket = Ticket_Details.objects.all()
        ticketNum = request.POST.get('ticketid')
        arr = []
        for i in ticket.iterator():
            arr.append(i.TicketNumber)
        if(ticketNum in arr):
            return render(request, 'login/ticket-status.html', {'status': 'CONFIRMED'})
        else:
            return render(request, 'login/ticket-status.html', {'status': 'CANCELLED'})   
    return render(request, 'login/ticket-status.html')

