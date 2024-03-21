from django.shortcuts import render,redirect
from order.models import Booknow,Account,Order
from car.models import Car
from django.contrib.auth.decorators import login_required
from datetime import datetime
from order.forms import booknowform

@login_required
def booknow(request,p):
    car = Car.objects.get(name=p)
    u=request.user
    if(request.method == 'POST'):
        form = booknowform(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            try:
                order = Booknow.objects.get(user=u, car=car, start_date=start_date, end_date=end_date)
                if (order.quantity < order.car.stock):
                    order.quantity += 1
                    order.save()
            except:
                order = Booknow.objects.create(car=car, user=u, quantity=1, start_date=start_date, end_date=end_date)
                order.save()
            return redirect('order:bookview')
    else:
        start_date = datetime.now().date()
        form = booknowform(initial={'start_date': start_date})
    return render(request, 'booknowform.html', {'form': form, 'car': car})

def bookview(request):
    u=request.user
    total = 0
    try:
        order = Booknow.objects.filter(user=u)
        for i in order:
            total += i.car.rent * i.total_days()
    except:
        pass
    return render(request,'booknow.html',{'o':order,'total':total})

def delete_booking(request,p):
    u=request.user
    order = Booknow.objects.get(user=u, id=p)
    order.delete()
    return redirect('order:bookview')

def orderform(request):
    if(request.method== "POST"):
        a = request.POST['a']
        p = request.POST['p']
        n = request.POST['n']
        u = request.user
        order = Booknow.objects.filter(user=u)

        total = 0
        for i in order:
            total += i.car.rent * i.total_days()

        ac = Account.objects.get(acctnum=n)
        if (ac.amount >= total):
            ac.amount = ac.amount - total
            ac.save()

            for i in order:
                o = Order.objects.create(user=u, car=i.car, address=a, phone=p, no_of_days=i.total_days(), order_status="paid")
                o.save()
                i.car.stock = i.car.stock - i.quantity
                i.car.save()

            order.delete()
            msg = "Booking Done Successfully"
            return render(request, 'orderdetail.html', {'m': msg})
        else:
            msg = "Insufficient Amount in User Account.You cannot confirm booking"
            return render(request, 'orderdetail.html', {'m': msg})
    return render(request, 'orderform.html')

def orderview(request):
    u = request.user
    o=Order.objects.filter(user=u)
    return render(request,'orderview.html',{'o':o})