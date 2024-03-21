from django.db import models
from car.models import Car
from django.contrib.auth.models import User

class Booknow(models.Model):
    car=models.ForeignKey(Car,on_delete=models.CASCADE, null=True, blank=True, default=None)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    start_date=models.DateField()
    end_date=models.DateField()

    def __str__(self):
        return self.car.name

    def total_days(self):
        if self.end_date >= self.start_date:
            return (self.end_date - self.start_date).days
        else:
            return 0

    def subtotal(self):
        return self.quantity * self.car.rent * self.total_days()

class Order(models.Model):
    car= models.ForeignKey(Car,on_delete=models.CASCADE)
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    address= models.TextField()
    phone= models.CharField(max_length=30)
    no_of_days = models.IntegerField()
    order_status= models.CharField(max_length=20,default="pending")
    date_ordered= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Account(models.Model):
    acctnum= models.CharField(max_length=20)
    accttype= models.CharField(max_length=20)
    amount= models.IntegerField()

    def __str__(self):
        return self.acctnum