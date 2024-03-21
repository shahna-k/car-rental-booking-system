from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from car.models import Category,Car,Featured

def aboutus(request):
    return render(request,'aboutus.html')

def allcategories(request):
    c=Category.objects.all()
    f=Featured.objects.all()
    return render(request,'category.html',{'c':c,'f':f})

def allproducts(request,p):
    c=Category.objects.get(name=p)
    p=Car.objects.filter(category=c)
    return render(request,'cars.html',{'c':c,'p':p})

def details(request,p):
    product=Car.objects.get(name=p)
    return render(request,'details.html',{'p':product})

def register(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        e = request.POST['e']
        if(p==cp):
            u = User.objects.create_user(username=u, password=p, email=e)
            u.save()
            return redirect('car:login')
        else:
            return HttpResponse("Password not matching")
    return render(request,'register.html')

def user_login(request):
    if (request.method == "POST"):
        name = request.POST['n']
        pass1 = request.POST['p']
        user = authenticate(username=name, password=pass1)
        if user:
            login(request,user)
            return redirect('car:allcategories')
        else:
            messages.error(request, "Invalid Credentials")
    return render(request,'login.html')

@login_required()
def user_logout(request):
    logout(request)
    return user_login(request)