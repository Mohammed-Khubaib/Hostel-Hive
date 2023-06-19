from django.shortcuts import render ,HttpResponse
from HostelHive.models import Booknow
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')
def khubaib(request):
    return HttpResponse("Khubaib is working on Django this time")
    
def home(request):
    return HttpResponse("This is the home page")
def about(request):
    return render(request,'about.html')
def pricing(request):
    return render(request,'pricing.html')
def booknow(request):
    if request.method == "POST" :
        name = request.POST.get('name')
        country_zip = request.POST.get('country_zip')
        checkin =  request.POST.get('checkin')
        checkout = request.POST.get('checkout')
        rooms = request.POST.get('rooms')
        adults = request.POST.get('adults')
        children = request.POST.get('children')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        bknow = Booknow(name = name , country_zip = country_zip, checkin = checkin , checkout = checkout, rooms = rooms  ,adults=adults, children = children , email=email , phonenumber = phonenumber)
        bknow.save()
        # i want this messages to print if and only if the data is saved without anyissues
        try:
            bknow.save()
            messages.warning(request, "Your Reservation is Successfully Registered")
            messages.success(request, "We will shortly contact you through your email or phone number")
        except Exception as e:
            messages.error(request, f"An error occurred while saving the reservation: {str(e)}")
    return render(request,'booknow.html')
    

