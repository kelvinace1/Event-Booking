from django import forms
from .models import Event, Ticket, Booking

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'location']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['ticket_type', 'price', 'quantity_available']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['quantity']

