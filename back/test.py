from django.test import TestCase

# Create your tests here.
import datetime
from django.conf import settings  
import os,django
import matplotlib.pyplot as plt
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "back.settings")
django.setup()
import datetime
from order.models import Order
enddate = datetime.date(2019, 12, 30)
print(enddate.isocalendar()[1] + 1)