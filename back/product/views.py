from product.models import Product, Comment
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
import json
from django.db.models import Q
from user.models import LoginUser
from pic.models import Pic
from order.models import Order

# Create your views here.
def getProduct111():
    '''
    获取商品列表
    可以选择返回所有商品或者返回某个商家的商品
    '''
    products = Product.objects.all().values()
    print(products)

def getProductInfo(request):
    '''
    获取商品列表
    可以选择返回所有商品或者返回某个商家的商品
    '''
    if request.method == "POST":
        req = json.loads(request.body)
        # print(req)
        id = req['pid']
        print('id', 'id', id)
        data = {}
        products = Product.objects.filter(id=id).values()
        data['dataArray'] = list(products)
        return JsonResponse({
            'status' : 200,
            'msg' : 'cha zhao cheng gong',
            'data' : data
        })


def getProduct(request):
    '''
    获取商品列表
    可以选择返回所有商品或者返回某个商家的商品
    '''
    if request.method == "POST":
        req = json.loads(request.body)
        # print(req)
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
            # print(merchantName)
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
        # print(req)
        product.productName = req['productName']
        # product.merchantName = req['merchantName']
        product.merchantName = req['merchantName']
        product.status = 1
        product.price = req['price']
        product.basePrice = req['cost']
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

def editproductinfo(request) :
    '''
    url: editproinfo
    该函数修改商品属性
    '''
    if request.method == "POST":
        req = json.loads(request.body)
        pid = req['pid']
        price = req['price']
        cost = req['cost']
        dateinpro = req['date']
        inventory = req['inventory']
        desc = req['desc']
        pro = Product.objects.filter(id=pid).first()
        if price != '':
            pro.price = float(price)
        if cost != '' :
            pro.basePrice = cost
        if dateinpro != '' :
            pro.dataInProduction = dateinpro
        if inventory != '' :
            pro.inentory = inventory
        if desc != '' :
            pro.breifDescription = desc
        try:
            pro.save()
        except:
            return JsonResponse({
                'status' :500,
                'msg' : 'There are somethiing wrong! Nothing was changed!'
            })
        return JsonResponse({
            'status' : 200,
            'msg' : 'the information has been changed!'
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

def delProduct(request):
    '''
    该方法为商品浏览页面返回可用的商品
    '''
    if request.method == "POST":
        req = json.loads(request.body)
        id = req['id']
        products = Product.objects.filter(id = id)
        try:
            products.delete()
        except:
            return JsonResponse({
                'status' : 500,
                'msg' : 'del failed'
            })
        # print("del sc")
        return JsonResponse({
            'status' : 200,
            'msg' : 'del success'
        })

def GetAllComments(request):
    '''
    返回一个商品的所有评论
    '''
    if request.method == "POST":
        req = json.loads(request.body)
        # print(req)
        productId = req['pid']
        data = {}
        try:
            comments = Comment.objects.filter(productId=productId).filter(~Q(neirong='')).values()
        except:
            return JsonResponse({
                'status' : 500,
                'msg' : 'load comments failed',
            })
        data['dataArray'] = list(comments)
        print(list(comments))
        return JsonResponse({
            'status' : 200,
            'msg' : 'load comments success',
            'data' : data
        }, safe=False)

def AddComment(request):
    '''
    添加一条评论
    '''
    if request.method == "POST":
        commment = Comment()
        req = json.loads(request.body)
        pid = req['productId']
        neirong = req['neirong']
        oid = req['orderId']
        print(oid)
        cid = req['customerName']
        star = req['star']
        check = Comment.objects.filter(orderId=oid).values_list()
        c = LoginUser.objects.filter(username=cid).first()
        ord = Order.objects.filter(id=oid).first()
        print(ord)
        if ord.status != 'Delivered':
            return JsonResponse({
                'status' : 501,
                'msg' : "you can't comment on a product not deliveried"
            })
        if len(check) > 0 :
            return JsonResponse({
                'status' : 501,
                'msg'    : "you can't comment an order twice!"
            })
        else:
            commment.productId = pid
            commment.orderId = oid
            commment.customerId = c.id
            commment.neirong = neirong
            commment.stars = star
        if star != 0:
            pro = Product.objects.filter(id=pid).first()
            curn = pro.starsNumber
            curs = pro.stars
            curs = (curs * curn + star) / (curn + 1)
            pro.starsNumber = curn + 1
            pro.stars = curs

            pro.save()

        print(commment.orderId, commment.neirong)
        try:
            commment.save()
            print(" try save")
        except:
            return JsonResponse({
                'status' : 500,
                'msg' : 'comment failed'
            })
        return JsonResponse({
            'status' : 200,
            'msg' : 'Thank you for your comment'
        })

def ChangeStars(request):
    '''
    更新一个商品的评星
    '''
    if request.method == "POST":
        req = json.loads(request.body)
        star = req['star']
        productname = req['productName']
        try:        
            product = Product.objects.filter(productName = productname).first()
            prestar = product.stars
            starnumber = product.starsNumber
            starnumber += 1
            nowstar = (prestar * starnumber + star) / starnumber
            product.update(stars = nowstar)
            product.update(starsNumber = starnumber)
        except:
            return JsonResponse({
            'status' : 500,
            'msg' : 'change failed'
        })
        return JsonResponse({
            'status' : 200,
            'msg' : 'change success'
        })
    
def UploadPic(request):
    print(111)
    import os
    from django.conf import settings  
    from pic.models import Pic
    if request.method == "POST":
        fp = request.FILES.get("file")
        pid = request.POST.get("productId")
        pro = Product.objects.filter(id=pid).first()
        pro.imageUrl = fp.name
        p = Pic()
        p.productId = pid
        p.path = fp.name
        if fp:
            path = os.path.join(settings.STATICFILES_DIRS[0],'media/' + fp.name)  # 上传文件本地保存路径， image是static文件夹下专门存放图片的文件夹
            if fp.multiple_chunks():  # 判断上传文件大于2.5MB的大文件
                # 为真
                file_yield = fp.chunks()  # 迭代写入文件
                with open(path,'wb') as f:
                    for buf in file_yield:   # for情况执行无误才执行 else
                        f.write(buf)
                    else:
                        print("大文件上传完毕")
            else:
                try:
                    p.save()
                    pro.save()
                except:
                    return JsonResponse({
                        'status' : 500,
                        'msg'    : 'save failed'
                    })
                with open(path,'wb') as f:
                    f.write(fp.read())
                    print("小文件上传完毕")
            # models.ImgPath.objects.create(path=('image/' + fp.name))   # image是static文件夹下专门存放图片的文件夹
        else:
            return JsonResponse({
                'status' : 200,
                'msg'    : "tsakjbs"
            })
        return JsonResponse({
            'status' : 200,
            'msg'    : "tsakjbs"
        })

def Search(request):
    if request.method == 'POST':
        data = {}
        req = json.loads(request.body)
        q = req['keyword']
        order = req['order']
        print(1, order, 1)
        if q != '':
            if order == "dec":
                post_list = Product.objects.filter(productName__icontains=q).order_by("-price").values()
            if order == "inc":
                post_list = Product.objects.filter(productName__icontains=q).order_by("price").values()
            if order == '':
                post_list = Product.objects.filter(productName__icontains=q).values()
            data['dataArray'] = list(post_list)
        else:
            if order == "dec":
                post_list = Product.objects.all().order_by("-price").values()
            if order == "inc":
                post_list = Product.objects.all().order_by("price").values()
            if order == '':
                post_list = Product.objects.all().values()
            data['dataArray'] = list(post_list)
        return JsonResponse({
            'status' : 200,
            'data' : data
        }, safe=False)


def loadComment(request):
    if request.method == "POST":
        req = json.loads(request.body)
        pid = req['pid']
        try:
            p = Comment.objects.filter(productId=pid).values()
        except:
            return JsonResponse({
                'status' : 500,
                'msg'    : 'load comments failed'
            })
        data = {}
        data['dataArray'] = list(p)
        return JsonResponse({
            'status' : 200,
            'data' : data
        }, safe=False)

def loadPic(request):
    if request.method == "POST":
        req = json.loads(request.body)
        pid = req['pid']
        print("pid", pid)
        try:
            p = Pic.objects.filter(productId=pid).values()
            print('p',111,  p)
        except:
            return JsonResponse({
                'status' : 500,
                'msg' : 'load pictures failed'
            })
        data = {}
        data['dataArray'] = list(p)
        return JsonResponse({
            'status' : 200,
            'msg' : 'load pictures done',
            'data' : data
        })






