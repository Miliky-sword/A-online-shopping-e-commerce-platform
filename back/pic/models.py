from django.db import models

# Create your models here.
class Pic(models.Model):

    productId = models.IntegerField()
    path = models.CharField(max_length=512)
