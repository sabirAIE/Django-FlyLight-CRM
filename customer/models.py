from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    tags = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.tags 

class Product(models.Model):
    categories = [
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
    ]
    name = models.CharField(max_length= 100, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(choices=categories, null=True, max_length=100)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

class Order(models.Model):
    order_status = [
        ('Pending','Pending'),
        ('Delivered','Delivered'),
        ('Out for Delivery', 'Out for Delivery')
    ]
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    products = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    status = models.CharField(choices=order_status,null=True, max_length=100)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return self.status