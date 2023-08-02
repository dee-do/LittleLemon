from django.test import TestCase
#from rest_framework.test import APITestCase
from Little_Lemon_App.models import Menu, Booking
from datetime import datetime
class MenuTest(TestCase):
    def setUp(self):
        Menu.objects.create(title='falafel', price=7.50, inventory=30)
        Menu.objects.create(title='moussaka', price=12.75, inventory=15)

    def test_get_item(self):
        menu_falafel = Menu.objects.get(title='falafel')
        menu_moussaka = Menu.objects.get(title='moussaka')
        self.assertEqual(menu_falafel.get_item(), "falafel:7.50")
        self.assertEqual(menu_moussaka.get_item(), "moussaka:12.75")
        
class BookingTest(TestCase):
    def setUp(self):
        Booking.objects.create(name='ruby', no_of_guests=2, bookingDate=datetime.now())
        Booking.objects.create(name='gina', no_of_guests=4, bookingDate=datetime.now())

    def test__str__(self):
        booking_ruby = Booking.objects.get(name='ruby')
        booking_gina = Booking.objects.get(name='gina')
        self.assertEqual(booking_ruby.get_booking(), "ruby")
        self.assertEqual(booking_gina.get_booking(), "gina")
    
