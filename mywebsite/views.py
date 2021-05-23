from django.shortcuts import render,HttpResponse
from datetime import datetime
from mywebsite.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def about(request):
    return render(request, 'about.html')

def services(request):
   return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(email=email, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Congrats!! Your request send successfully..')
    return render(request, 'contact.html')
    
def login(request):
    return render(request, 'login.html')
    
def register(request):
     return render(request, 'register.html')

def shop(request):
    return render(request, 'shop.html')

def automob(request):
    return render(request, 'automob.html')

def electrician(request):
    return render(request, 'electrician.html')

def shoplogin(request):
    return render(request, 'shoplogin.html')

def registershop(request):
    return render(request, 'registershop.html')