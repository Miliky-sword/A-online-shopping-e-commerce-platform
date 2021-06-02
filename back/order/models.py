from django.db import models

# Create your models here.
class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Payed', 'Payed'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
        ('Canceled', 'Canceled'),
    )

    username = models.CharField(max_length=32,null=True,blank=True)
    productName = models.CharField(max_length=32,null=True,blank=True)
    productId = models.IntegerField()
    merchantName = models.CharField(max_length = 32)
    time_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, choices=STATUS)
    inventory = models.IntegerField(default=999)
    address = models.TextField(null=True,blank=True)
    toPhoneNumber = models.CharField(max_length=11, default=12233345556)
    fromAddress = models.TextField(default="test from address")
    fromPhoneNumber = models.CharField(max_length=11, default=12233345556)
    totalprice =  models.FloatField()
    profit = models.FloatField(default=500)