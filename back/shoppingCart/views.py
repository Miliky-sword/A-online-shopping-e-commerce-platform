from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
import json
from shoppingCart.models import shoppingcartP

# Create your views here.
def all_products_of_shoppingcart(request):
    '''
    返回一个用户的购物车中的所有商品
    '''
    if request.method == 'POST':
        data = {}
        req = json.loads(request.body)
        username = req['username']
        if username == '':
            return JsonResponse({
                'status' : 300
            })
        users = shoppingcartP.objects.filter(username=username).all().values()
        data['dataArray'] = list(users)
        print('data', data)
        return JsonResponse({
            'status' : 200,
            'data' : data
        }, safe=False)

def remove_a_product_from_shoppingcart(request):
    '''
    删除用户购物车中的一个商品
    '''
    if request.method == "POST":
        req = json.loads(request.body)
        productName = req['productName']
        username = req['username']
        merchantName = req['merchantName']
        print("delete ", username, productName)
        shoppingcartP.objects.filter(username = username, productName=productName, merchantName = merchantName).delete()
        return JsonResponse({
            'status': 200,
            'msg': 'delete success'
        })

def add_a_product_to_shoppingcart(request):
    '''
    '''
    if request.method == "POST":
        req = json.loads(request.body)
        username = req['username']
        productName = req['productName']
        merchantName = req['merchantName']
        price = req['price']
        inventory = req['inventory']
        sp = shoppingcartP()
        sp.username = username
        sp.productName = productName
        sp.merchantName = merchantName
        sp.price = price
        sp.inventory = inventory
        try:
            sp.save()
        except:
            return JsonResponse({
                'status' : 500,
                'msg'    : 'add failed'
            })
        return JsonResponse({
            'status' : 200,
            'msg'    : 'add success'
        })