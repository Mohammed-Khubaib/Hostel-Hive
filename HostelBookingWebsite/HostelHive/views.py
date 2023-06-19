from django.shortcuts import render ,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def khubaib(request):
    return HttpResponse("Khubaib is working on Django this time")
    
def home(request):
    return HttpResponse("This is the home page")
def about(request):
    return render(request,'about.html')
    # return HttpResponse("About page")
def pricing(request):
    return render(request,'pricing.html')
def booknow(request):
    # return HttpResponse("booknow page")
    return render(request,'booknow.html')
    