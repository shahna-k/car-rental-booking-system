from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=30)
    image=models.ImageField(upload_to='car/categories',blank=True,null=True)
    def __str__(self):
        return self.name

class Featured(models.Model):
    name=models.CharField(max_length=30)
    image=models.ImageField(upload_to='car/featured',blank=True,null=True)
    rent = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='car/cars', blank=True, null=True)
    rent=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name