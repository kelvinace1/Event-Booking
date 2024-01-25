from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('events/', views.all_events, name="events"),
    path('events/<int:event_id>/<int:ticket_id>/', views.event_detail, name="event_detail"),
    path('create/', views.create_event, name="create"),
    path('edit/<int:event_id>/<int:ticket_id>/', views.edit_event, name="edit"),
    path('delete/<int:event_id>/', views.delete_event, name="delete"),
    path('book/<int:event_id>/<int:ticket_id>/', views.book_ticket, name="book_ticket"),
    path('download/<int:booking_id>/', views.download_ticket, name="download_ticket"),
    #path('notification/', views.notification, name="notification"),
]
