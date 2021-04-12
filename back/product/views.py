from product.models import Product
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
import json

# Create your views here.

def getProduct(request):
    '''
    获取商品列表
    可以选择返回所有商品或者返回某个商家的商品
    '''
    if request.method == "POST":
        req = json.loads(request.body)
        print(req)
        isAll = req['isAll']
        if isAll:
            data = {}
            products = Product.objects.all().values()
            data['dataArray'] = list(products)
            return JsonResponse({
                'status' : 200,
                'msg' : 'cha zhao cheng gong',
                'data' : data
            })
        else :
            merchantName = req['merchantName']
            print(merchantName)
            data = {}
            products = Product.objects.all().filter(merchantName = merchantName).values()
            data['dataArray'] = list(products)
            return JsonResponse({
                'status' : 200,
                'msg' : 'cha zhao cheng gong',
                'data' : data
            })

def addProduct(request):
    '''
    添加商品
    '''
    if request.method == "POST":
        product = Product()
        req = json.loads(request.body)
        print(req)
        product.productName = req['productName']
        product.merchantName = req['merchantName']
        product.status = 1
        product.price = req['price']
        product.inventory = req['inventory']
        product.dateInProduction = req['dateInProduction']
        product.briefDescription = req['briefDescription']
        product.save()
        return JsonResponse({
            'status' : 200,
            'msg' : 'tian jia cheng gong'
        })

def changeProductStatus(request):
    '''
    修改商品可用状态
    '''
    if request.method == "POST":
        req = json.loads(request.body)
        productName = req['productName']
        status = req['status']
        product = Product.objects.filter(productName=productName).first()
        product.status = status
        product.save()
        return JsonResponse({
            'status' : 200,
            'msg' : 'xiu gai zhuang tai cheng gong'
        })

def getAvailableProduct(request):
    '''
    该方法为商品浏览页面返回可用的商品
    '''
    if request.method == "GET":
        data = {}
        products = Product.objects.filter(status=1).values()
        data['dataArray'] = list(products)
        return JsonResponse({
            'status' : 200,
            'msg' : 'cha zhao cheng gong',
            'data' : data
        })






