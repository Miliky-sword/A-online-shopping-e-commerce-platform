from django.urls import path,re_path,include
from product.views import *

urlpatterns = [
    path(r'getProduct/', getProduct),
    path(r'addProduct/', addProduct),
    path(r'changeProductStatus/', changeProductStatus),
    path(r'getAvailableProduct/', getAvailableProduct)
]
