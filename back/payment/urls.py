from django.contrib import admin
from django.conf.urls import url
from payment import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('index/', views.index),
    url('refund/', views.refund),
    url('result/', views.pay_result),  # 支付宝处理完成后回调的get请求路由
    url('update_order/', views.update_order), # 支付宝处理完成后回调的post请求路由
]
