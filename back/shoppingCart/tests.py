from django.test import TestCase
# Create your tests here.
import os
from django.conf import settings  
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "back.settings")
django.setup()

