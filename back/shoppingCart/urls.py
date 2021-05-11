from django.urls import path,re_path,include
from shoppingCart.views import *

urlpatterns = [
    path(r'allproductsofshoppingcart/', all_products_of_shoppingcart),
    path(r'removeaproductfromshoppingcart/', remove_a_product_from_shoppingcart),
    path(r'addaproducttoshoppingcart/', add_a_product_to_shoppingcart),
]