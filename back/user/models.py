from django.db import models
from django.db.models import Manager

# Create your models here.

class LoginUser(models.Model):
    
    username = models.CharField(max_length=32,null=True,blank=True,unique=True)
    password = models.CharField(max_length=999)
    user_type=models.IntegerField(default=1)# 0顾客 1商家 2管理员
    address = models.TextField(null=True,blank=True)
    phoneNumber = models.CharField(max_length=11, default=12233345556)
    sig = models.CharField(max_length=200, default="There are no personalized signature")
    email = models.EmailField(default="testemail@email.com")
    


    # null针对数据库，True表示可以为空，即在数据库的存储中可以为空
    # blank 针对表单，表示在表单中该字段可以不填，但对数据库没有影响
    '''
    email = models.EmailField()
    phone_number = models.CharField(max_length=11,null=True,blank=True)
    photo = models.ImageField(upload_to='img',null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    gender = models.CharField(max_length=4,null=True,blank=True)
    '''
    
    
    