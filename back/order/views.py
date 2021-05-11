from django.shortcuts import render
from order.models import Order
from user.models import LoginUser
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
import json

# Create your views here.
def create_order(request):
    '''
    创建一个订单
    '''
    order = Order()
    if request.method == "POST":
        req = json.loads(request.body)
        order.username = req['username']
        order.productName = req['productName']
        order.totalprice = req['totalprice']
        order.inventory = req['inventory']
        order.merchantName = req['merchantName']
        order.status = 'Pending'
        order.address = LoginUser.objects.filter(username=order.username).first().address
        try:
            order.save()
        except:
            return JsonResponse({
                'status' : 500,
                'msg'    : 'add failed'
            })
        return JsonResponse({
            'status' : 200,
            'msg'    : 'add success'
        })
def change_order_status_payed(request):
    '''
    更改订单状态为已支付
    '''
    if request.method == "POST":
        req = json.loads(request.body)
        id = req['id']
        order = Order.objects.filter(id = id)
        try:
            order.update(status = 'Payed')
        except:
            return JsonResponse({
                'status' : 500,
                'msg'    : 'change failed'
            })
        return JsonResponse({
            'status' : 200,
            'msg'    : 'change success'
        })

def change_order_status_delivering(request):
    '''
    更改订单状态为正在递送
    '''
    if request.method == "POST":
        req = json.loads(request.body)
        id = req['id']
        order = Order.objects.filter(id = id)
        try:
            order.update(status = 'Out for delivery')
        except:
            return JsonResponse({
                'status' : 500,
                'msg'    : 'change failed'
            })
        return JsonResponse({
            'status' : 200,
            'msg'    : 'change success'
        })

def change_order_status_delivered(request):
    '''
    更改订单状态为递送成功
    '''
    if request.method == "POST":
        req = json.loads(request.body)
        id = req['id']
        order = Order.objects.filter(id = id)
        try:
            order.update(status = 'Delivered')
        except:
            return JsonResponse({
                'status' : 500,
                'msg'    : 'change failed'
            })
        return JsonResponse({
            'status' : 200,
            'msg'    : 'change success'
        })

def change_order_status_canceled(request):
    '''
    更改订单状态为取消
    '''
    if request.method == "POST":
        req = json.loads(request.body)
        id = req['id']
        order = Order.objects.filter(id = id)
        try:
            order.update(status = 'Canceled')
        except:
            return JsonResponse({
                'status' : 500,
                'msg'    : 'change failed'
            })
        return JsonResponse({
            'status' : 200,
            'msg'    : 'change success'
        })

def get_customer_orders(request):
    '''
    获得一个顾客的所有订单
    '''
    if request.method == "POST":
        data = {}
        req = json.loads(request.body)
        username = req['username']
        users = Order.objects.filter(username=username).all().values()
        data['dataArray'] = list(users)
        print(data)
        return JsonResponse({
            'status' : 200,
            'data' : data
        }, safe=False)

def get_merchant_orders(request):
    '''
    获得一个顾客的所有订单
    '''
    if request.method == "POST":
        req = json.loads(request.body)
        username = req['merchantName']
        data = {}
        users = Order.objects.filter(merchantName=username).all().values()
        data['dataArray'] = list(users)
        print(data)
        return JsonResponse({
            'status' : 200,
            'data' : data
        }, safe=False)


    
