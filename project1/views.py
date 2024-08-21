from django.shortcuts import HttpResponse, render
from Restaurantly.models import Bookatable,Contect

def home(request, fname="home"):
    if request.method == "POST":
        print("Yes In Post Method......")
        if fname == "home":
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            date = request.POST.get('date')
            time = request.POST.get('time')
            people = request.POST.get('people')
            message = request.POST.get('message')
            obj = Bookatable(name=name, email=email, phone=phone, date=date, time=time, people=people, message=message)
            obj.save()
            return render(request,'index.html')
        else:
            print("Yes......")
            Name = request.POST.get('name1')
            Email = request.POST.get('email1')
            Subject = request.POST.get('subject1')
            Message = request.POST.get('message1')
            print("name::{} email::{} subject::{} message::{}".format(Name,Email,Subject,Message))
            obj1 = Contect(name=Name, email=Email, subject=Subject, message=Message)
            obj1.save()
            return render(request,'index.html')
    return render(request, 'index.html')

def contact_view(request):
    return render(request, 'Contect.html')

def about_us(request):
    return render(request, 'About.html')

def service(request):
    return render(request, 'service.html')

def string_method(request):
    return render(request, 'index.html')
