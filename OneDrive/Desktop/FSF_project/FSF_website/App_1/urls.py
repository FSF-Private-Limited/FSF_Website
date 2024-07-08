from django.urls import path
from .views import Home,About,Services,Careers,Contact,Register
urlpatterns = [
    path('',Home,name="home"),
    path('about',About,name="about"),
    path('services',Services,name="services"),
    path('careers',Careers,name="careers"),
    path('contact',Contact,name="contact"),
    path('register',Register,name="register")
]
