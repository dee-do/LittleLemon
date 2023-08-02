"""
URL configuration for Little_Lemon_Proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from rest_framework.routers import DefaultRouter
from Little_Lemon_App import views

""" router = DefaultRouter()
#tables below is the url prefix i.e. the url will be restaurant/booking/tables
#router.register('tables', views.BookingViewSet)
router.register('bookings', views.BookingViewSet)
router.register('bookings/<int:pk>', views.SingleBookingView.as_view())
 """

urlpatterns = [
    #path('restaurant/', include (router.urls)),
    path('admin/', admin.site.urls),
    path('restaurant/', include('Little_Lemon_App.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/',include('djoser.urls.authtoken')),
    
]
