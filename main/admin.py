from django.contrib import admin
from .models import Event, Ticket, Booking, Account
# Register your models here.

admin.site.register(Event)
admin.site.register(Ticket)
admin.site.register(Booking)
admin.site.register(Account)
#admin.site.register(Notification)