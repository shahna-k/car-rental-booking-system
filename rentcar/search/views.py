from django.shortcuts import render
from car.models import Car

def search(request):
    q = ""
    product=None
    if(request.method=="POST"):
        q = request.POST['q']
        if q:
            product=Car.objects.filter(name__icontains=q)
    return render(request,'search.html',{'p':product,'query':q})
