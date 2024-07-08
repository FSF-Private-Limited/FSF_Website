from django.shortcuts import render
from .models import Userdata
# Create your views here.

def Home(request):
    return render(request,"index.html")

def About(request):
    return render(request,"about.html")

def Services(request):
    return render(request,"services.html")

def Careers(request):
    return render(request,"careers.html")

def Contact(request):

    return render(request,"contact.html")

def Register(request):
    if request.method == "POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        number=request.POST.get('number')
        city=request.POST.get('city')
        email=request.POST.get('email')
        regarding=request.POST.get('regarding')
        userform=Userdata(firstname=firstname,lastname=lastname,number=number,city=city,email=email,regarding=regarding)
        userform.save()
      
    return render(request,"register.html")




