from django.test import TestCase

# Create your tests here.
import datetime
from django.conf import settings  
import os,django
import matplotlib.pyplot as plt
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "back.settings")
django.setup()

from order.models import Order
Order.objects.filter(productId__gt=6).delete()