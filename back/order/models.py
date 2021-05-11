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
    merchantName = models.CharField(max_length = 32)
    time_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, choices=STATUS)
    inventory = models.IntegerField(default=999)
    address = models.TextField(null=True,blank=True)
    totalprice =  models.FloatField()