from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from home.models import contact
# Create your views here.
def index(request):
    context={
        'variable':'This is sent'
    }
    return render(request,'index.html',context)
   # return HttpResponse("This is home page")
def about(request):
    return render(request,'about.html')
   # return HttpResponse("This is about page")
def services(request):
    return render(request,'services.html')
    #return HttpResponse("This is services page")
def contact(request):
    if request.method=="POST":
        firstName=request.POST.get('firstName')
        lastName=request.POST.get('lastName')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=contact(firstName=firstName,lastName=lastName,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        #date=datetime.today()
        
    return render(request,'contact.html')
    #return HttpResponse("This is contact page")