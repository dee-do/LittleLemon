import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Menu, Booking
from ..serializers import BookingSerializer, MenuSerializer
from datetime import datetime
from django.contrib.auth.models import User
from rest_framework.test import force_authenticate, APIClient

#initialize the APIClient
client = APIClient()

#test module for GET all menu items
class GetAllMenuItems(TestCase):
    #use this method to add some test instances of menu items
    def setUp(self):
        user = User.objects.create_user('user1', 'Pas$w0rD1')
        client.force_authenticate(user=user)

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


#test for GET all bookings
class GetAllBookings(TestCase):
    #use this method to add some test instances of bookings
    def setUp(self):
        user = User.objects.create_user('user2', 'Pas$w0rD2')
        client.force_authenticate(user=user)

        Booking.objects.create(name='ronny', no_of_guests=2, bookingDate=datetime.now())
        Booking.objects.create(name='nancy', no_of_guests=6, bookingDate=datetime.now())
        Booking.objects.create(name='joel', no_of_guests=4, bookingDate=datetime.now())
    

    def test_get_all_bookings(self):
        #get API response
        response = client.get(reverse('bookings'))
        #get data from DB
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code,status.HTTP_200_OK )



#test module for creating a new menu item (POST)
class CreateNewMenuItem(TestCase):

    def setUp(self):
        user = User.objects.create_user('user3', 'Pas$w0rD3')
        client.force_authenticate(user=user)

        self.valid_payload = {
            'title': 'tzatziki',
            'price': 5.50 ,
            'inventory': 30
        }
        self.invalid_payload = {
            'title': '',
            'price': 5.50 ,
            'inventory': 30
        }

    #json.dumps is used below to convert python objects to json string
    def test_create_valid_item(self):
        response = client.post(
                                reverse('menu'),
                                data = json.dumps(self.valid_payload),
                                content_type= 'application/json'
                            )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_item(self):
        response = client.post(
                                reverse('menu'),
                                data = json.dumps(self.invalid_payload),
                                content_type= 'application/json'
                            )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


#test module for creating a new booking (POST)
class CreateNewBooking(TestCase):

    def setUp(self):
        user = User.objects.create_user('user4', 'Pas$w0rD4')
        client.force_authenticate(user=user)

        #use .isoformat() below because datetime.now() is not JSON serializable
        #this results in json.dumps() erroring out
        self.valid_payload = {
            'name': 'Rita',
            'no_of_guests': 2,
            'bookingDate': datetime.now().isoformat()
        }
        self.invalid_payload = {
            'name': '',
            'no_of_guests': 6.50 ,
            'bookingDate': datetime.now().isoformat()
        }

    #json.dumps is used below to convert python objects to json string
    def test_create_valid_booking(self):
        response = client.post(
                                reverse('bookings'),
                                data = json.dumps(self.valid_payload),
                                content_type= 'application/json'
                            )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_item(self):
        response = client.post(
                                reverse('bookings'),
                                data = json.dumps(self.invalid_payload),
                                content_type= 'application/json'
                            )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


#test for updating an existing menu item (PUT)
class UpdateSingleMenuItem(TestCase):

    def setUp(self):
        user = User.objects.create_user('user5', 'Pas$w0rD5')
        client.force_authenticate(user=user)

        self.pie = Menu.objects.create(title="pie", price=4.50, inventory=30)

        self.valid_payload = {
            'title': 'spinach cheese pie',
            'price': 5.50 ,
            'inventory': 35
        }
        self.invalid_payload = {
            'title': '',
            'price': 7.50 ,
            'inventory': 20
        }

    def test_valid_update_item(self):
        response = client.put(
                                reverse('menu_item', kwargs={'pk':self.pie.pk}),
                                data= json.dumps(self.valid_payload),
                                content_type= 'application/json'
                            )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_item(self):
        response = client.put(
                                reverse('menu_item', kwargs={'pk':self.pie.pk}),
                                data= json.dumps(self.invalid_payload),
                                content_type= 'application/json'
                            )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleBooking(TestCase):
    def setUp(self):
        user = User.objects.create_user('user6', 'Pas$w0rD6')
        client.force_authenticate(user=user)
       
        self.Travis = Booking.objects.create(name='Travis', no_of_guests=2, bookingDate=datetime.now())
        #use .isoformat() below because datetime.now() is not JSON serializable
        #this results in json.dumps() erroring out
        self.valid_payload = {
            'name': 'Trina',
            'no_of_guests': 2,
            'bookingDate': datetime.now().isoformat()
        }
        self.invalid_payload = {
            'name': '',
            'no_of_guests': 4 ,
            'bookingDate': datetime.now().isoformat()
        }


    def test_valid_update_booking(self):
        response = client.put(
                                reverse('single_booking', kwargs={'pk':self.Travis.pk}),
                                data= json.dumps(self.valid_payload),
                                content_type= 'application/json'
                            )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_booking(self):
        response = client.put(
                                reverse('single_booking', kwargs={'pk':self.Travis.pk}),
                                data= json.dumps(self.invalid_payload),
                                content_type= 'application/json'
                            )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)