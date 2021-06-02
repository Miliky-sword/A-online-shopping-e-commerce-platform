from django.db import models
from django.db.models import Manager

# Create your models here.
class shoppingcartP(models.Model):
    username = models.CharField(max_length=32,null=True,blank=True)
    pid = models.IntegerField()
    productName = models.CharField(max_length=32,null=True,blank=True)
    merchantName = models.CharField(max_length = 32)
    price = models.FloatField()
    inventory = models.IntegerField(default=1)