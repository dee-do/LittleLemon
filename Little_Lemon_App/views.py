from django.shortcuts import render
from .models import Menu, Booking
from rest_framework import generics, viewsets
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(request):
    return render(request, "index.html", {})

# GET and POST
class MenuItemsView(generics.ListCreateAPIView):
    
    #permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

#GET, UPDATE and DELETE single item, detail view
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


#this viewset provides list, create, retrieve, update and destroy actions 
class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
