from django.urls import path,re_path,include
from order.views import *

urlpatterns = [
    path(r'createorder/', create_order),
    path(r'changeorderstatusdelivering/', change_order_status_delivering),
    path(r'changeorderstatusdelivered/', change_order_status_delivered),
    path(r'changeorderstatuscanceled/', change_order_status_canceled),
    path(r'changeorderstatuspayed/', change_order_status_payed),
    path(r'getcustomerorders/', get_customer_orders),
    path(r'getmerchantorders/', get_merchant_orders)
]