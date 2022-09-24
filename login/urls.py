from django.contrib import admin
from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login',views.logins,name="logins"),
    path('register',views.register,name="register"),
    path('feedback',views.feedback),
    path('booking',views.booking),
    path('contact',views.contact),
    path('payment',views.payment),
    path('leave',views.leave),
    path('logout',views.logout),
    path('flightdetails',views.flightdetails),
    path('getFlights',views.getFlights),
    path('book',views.book),
    path('faq',views.faq),
    path('explore',views.explore),
    path('ticket', views.ticket),
    path('payment_process', views.payment_process),
    path('downloadTicket', views.downloadTicket),
    path('dashboard', views.dashboard),
    path('showTicket', views.showTicket),
    path('cancelTicket', views.cancelTicket),
    path('discount', views.discount),
    path('seat', views.seat),
    path('details', views.details,name='user-profile'),
    path('ticket-status', views.ticketStatus),
    path('details/update', views.details_update,name='user-profile-update'),
    
    








    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]