from django.shortcuts import render
from .models import Menu, Booking
from rest_framework import generics, viewsets
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(request):
    return render(request, "index.html", {})

# GET all items and POST (create an item)
class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

#GET, UPDATE and DELETE single item, detail view
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


#this viewset provides list, create, retrieve, update and destroy actions 
# class BookingViewSet(viewsets.ModelViewSet):
#     #permission_classes = [IsAuthenticated]
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer

# GET all bookings and POST (create a booking)
class BookingsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

#GET, UPDATE and DELETE single booking, detail view
class SingleBookingView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset= Booking.objects.all()
    serializer_class = BookingSerializer