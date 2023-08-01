import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Menu, Booking
from ..serializers import BookingSerializer, MenuSerializer

#initialize the APIClient app
client = Client()

class GetAllMenuItems(TestCase):
    #use this method to add some test instances of menu items
    def setUp(self):
        Menu.objects.create(title="kanafa", price=4.50, inventory=30)
        Menu.objects.create(title="turkish coffee", price=4.00, inventory=40)
        Menu.objects.create(title="shish kabab", price=12.50, inventory=20)
    
    def test_get_all_menuitems(self):
        #get API response
        response = client.get(reverse('menu'))
        #get data from DB
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code,status.HTTP_200_OK )
