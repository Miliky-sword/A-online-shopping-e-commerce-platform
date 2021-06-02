from django.urls import path,re_path,include
from user.views import *

urlpatterns = [
    re_path(r'^$',hello),
    path(r'register/', register),
    path(r'login/', login),
    path(r'allusers/', allUsers),
    path(r'removeUserByName/', removeUserByName),
    path(r'addsig/', addsig),
    path(r'loadinfo/', loadinfo),
    path(r'editinfo/', editinfo),
    path(r'getMerchant/', allMerUsers)
]