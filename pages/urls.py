from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),#'' means the main menue or home page
    path('about', views.about, name='about'),  #views.method name is about/ name='about' name of our url
    path('services', views.services, name='services'),  #comma at the end is must
    path('contact', views.contact, name='contact'),
]
