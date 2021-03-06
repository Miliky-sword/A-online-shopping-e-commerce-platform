from django.db import models
from django.db.models import Manager

# Create your models here.
class Product(models.Model):
    
    productName = models.CharField(max_length=32,null=True,blank=True,unique=True)
    status=models.IntegerField(default=1)# 0下架 1上架
    merchantName = models.CharField(max_length = 32)
    price = models.FloatField()
    dateInProduction = models.DateField()
    briefDescription = models.CharField(max_length=255, default="")
    imageUrl = models.CharField(max_length=500, default="")
    inventory = models.IntegerField(default=999)
    stars = models.FloatField(default=0)
    starsNumber = models.IntegerField(default=0)
    basePrice = models.FloatField(default=575)
    classword = models.CharField(max_length=100, default='all;')
    
    

 
class Comment(models.Model):

    productId = models.IntegerField(db_index=True)
    customerId = models.IntegerField()
    orderId = models.IntegerField()
    stars = models.IntegerField()
    neirong = models.CharField(max_length=512)
    
