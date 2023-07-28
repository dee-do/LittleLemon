from django.shortcuts import render
from .models import Menu, Booking
from rest_framework import generics, viewsets
from .serializers import MenuSerializer, BookingSerializer

# Create your views here.
def index(request):
    return render(request, "index.html", {})

# GET and POST
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

#DELETE, GET detail and PUT
class SingleMenuItemView(generics.DestroyAPIView, generics.RetrieveUpdateAPIView):
    pass


#this viewset provides list, create, retrieve, update and destroy actions 
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
