from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class Event(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    date = models.DateTimeField()
    location = models.CharField(max_length=255, blank=False, null=False)
    owner = models.ForeignKey(User, related_name='events', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Ticket(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE, related_name='tickets')
    ticket_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_available = models.IntegerField()

    class Meta:
        ordering = ['price']

    def __str__(self):
        return f'{self.ticket_type} for {self.event} at {self.price}'
 

class Booking(models.Model):
    user = models.ForeignKey(User, related_name='bookings', on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, related_name='bookings', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.ticket.event.title} - {self.ticket.ticket_type} - Quantity: {self.quantity}"
    
class Account(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.account}'s balance -{self.balance}"
    
