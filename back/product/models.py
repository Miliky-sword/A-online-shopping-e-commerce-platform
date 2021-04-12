from django.db import models
#from django.db.models import Manager

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
    