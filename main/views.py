from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Event, Ticket, Booking, Account
from .forms import EventForm, TicketForm, BookingForm
from .pdf import generate_ticket_pdf


def index(request):
    return render(request, 'main/index.html')

def all_events(request):
    events  = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'main/events.html', context)

def event_detail(request, event_id, ticket_id):
    event = get_object_or_404(Event, pk=event_id)
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    context = {
        'event': event,
        'ticket': ticket,
    }
    
    return render(request, 'main/event_detail.html', context)

@login_required
def create_event(request):
    if request.method == 'POST':
        event_form = EventForm(request.POST)
        ticket_form = TicketForm(request.POST)
        if event_form.is_valid() and ticket_form.is_valid():
            event = event_form.save(commit=False)
            event.owner = request.user
            event.save()
            ticket = ticket_form.save(commit=False)
            ticket.event = event     
            ticket.save()
            return redirect('event_detail', event.id, ticket.id)
    else:
        event_form = EventForm()
        ticket_form = TicketForm()
    return render(request, 'main/create_events.html', {'event_form': event_form, 'ticket_form': ticket_form})

@login_required
def edit_event(request, event_id, ticket_id):
    event = get_object_or_404(Event, pk=event_id)
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    if event.owner != request.user:
            return redirect('events')
    if request.method == 'POST':    
        event_form = EventForm(request.POST, instance=event)
        ticket_form = TicketForm(request.POST, instance=ticket)
        if event_form.is_valid() and ticket_form.is_valid():
            event_form.save()
            ticket_form.save()
            return redirect('events')
    else:
        event_form = EventForm(instance=event)
        ticket_form = TicketForm(instance=ticket)

    context = {
            'event': event,
            'ticket': ticket,
            'event_form': event_form,
            'ticket_form': ticket_form
    }
    return render(request, 'main/edit_event.html', context)

@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if event.owner != request.user:
            return redirect('events')
    if request.method == 'POST':    
        event.delete()
        return redirect('events')
    return render(request, 'main/delete_event.html', {'event': event})
@login_required
def book_ticket(request, event_id, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id, event__id = event_id)
    account = get_object_or_404(Account, account=request.user)
    booking = None
    available_tickets = None
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            quantity_requested = form.cleaned_data['quantity']
            if quantity_requested <= ticket.quantity_available:
                total = ticket.price * quantity_requested
                if account.balance > total:   
                    booking = Booking(user=request.user, ticket=ticket, quantity=quantity_requested)
                    available_tickets = ticket.quantity_available - booking.quantity
                    ticket.quantity_available = available_tickets 
                    booking.save()
                    ticket.save()
                    account.balance -= total
                    account.save()
                else:
                    return HttpResponseForbidden("not enough money")
                
                return render(request, 'main/book_ticket_success.html', { 'ticket': ticket, 'booking': booking, 'total': total, 'available_tickets':available_tickets, 'account':account,})
            else:
                return HttpResponseForbidden("cannot get quantity requested")
        
    else:
        form = BookingForm()
    return render(request, 'main/book_ticket.html', {'form': form, 'ticket':ticket, 'booking':booking, 'available_tickets':available_tickets})
@login_required
def book_ticket(request, event_id, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id, event__id=event_id)
    account = get_object_or_404(Account, user=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            quantity_requested = form.cleaned_data['quantity']
            if quantity_requested <= ticket.quantity_available:
                total = ticket.price * quantity_requested
                if account.balance >= total:
                    ticket.quantity_available -= quantity_requested
                    ticket.save()
                    account.balance -= total
                    account.save()
                    booking = Booking.objects.create(user=request.user, ticket=ticket, quantity=quantity_requested)
                    return render(request, 'main/book_ticket_success.html', {'ticket': ticket, 'booking': booking, 'total': total, 'account': account})
                return HttpResponseForbidden("not enough money")
            return HttpResponseForbidden("cannot get quantity requested")
    else:
        form = BookingForm()
    return render(request, 'main/book_ticket.html', {'form': form, 'ticket': ticket})

@login_required
def download_ticket(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)


    pdf_buffer = generate_ticket_pdf(booking)

   
    response = HttpResponse(pdf_buffer.read(), content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=ticket_{booking.id}.pdf'
    return response

"""def notification(request):
    notifications = Notification.objects.filter(user=request.user)
    context = {
        'notifications': notifications
    }
    return render(request,'main/notification.html', context) """