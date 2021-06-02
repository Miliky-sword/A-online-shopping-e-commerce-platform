from django.urls import path,re_path,include
from product.views import *

urlpatterns = [
    path(r'getProduct/', getProduct),
    path(r'addProduct/', addProduct),
    path(r'changeProductStatus/', changeProductStatus),
    path(r'getAvailableProduct/', getAvailableProduct),
    path(r'delProduct/', delProduct),
    path(r'AddComment/', AddComment),
    path(r'ChangeStars', ChangeStars),
    path(r'post/', UploadPic),
    path(r'search/', Search),
    path(r'getProductInfo/', getProductInfo),
    path(r'loadcomment/', GetAllComments),
    path(r'loadPic/', loadPic),
    path(r'editproinfo/', editproductinfo)
]
