from datetime import date
from django.shortcuts import render
from order.models import Order
from product.models import Product
from user.models import LoginUser
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
import json
from django.db.models import Q

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
        order.productId = req['productId']
        order.totalprice = req['totalprice']
        order.inventory = req['inventory']
        order.merchantName = req['merchantName']
        order.status = 'Pending'
        order.address = LoginUser.objects.filter(username=order.username).first().address
        order.toPhoneNumber = LoginUser.objects.filter(username=order.username).first().phoneNumber
        order.fromAddress = LoginUser.objects.filter(username=order.merchantName).first().address
        order.fromPhoneNumber = LoginUser.objects.filter(username=order.merchantName).first().phoneNumber
        product = Product.objects.filter(id=order.productId).first()
        print(product, order.productId)
        order.profit = order.totalprice - order.inventory * product.basePrice
        inv = product.inventory
        product.inventory = inv - order.inventory if  inv - order.inventory > 0 else 0
        try:
            order.save()
            product.save()
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
        order = Order.objects.filter(id = id).first()
        if order.status != 'Pending':
            return JsonResponse({
                'status' : 501,
                'msg'    : 'You have payed the order!'
            })
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
        order = Order.objects.filter(id = id).first()
        if order.status != 'Payed':
            return JsonResponse({
                'status' : 501,
                'msg'    : 'the order must be payed first!'
            })
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
        order = Order.objects.filter(id = id).first()
        if order.status != 'Out for delivery':
            return JsonResponse({
                'status' : 501,
                'msg'    : 'the order is not delivering'
            })
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

def change_order_status_canceling(request):
    '''
    更改订单状态为取消
    '''
    if request.method == "POST":
        req = json.loads(request.body)
        id = req['id']
        order = Order.objects.filter(id = id).first()
        order = Order.objects.filter(id = id)
        try:
            order.update(status = 'Canceling')
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
        order = Order.objects.filter(id = id).first()
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
        users = Order.objects.filter(username=username).all().order_by('-time_created').values()
        data['dataArray'] = list(users)
        # print(data)
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
        users = Order.objects.filter(merchantName=username).all().order_by('-time_created').values()
        data['dataArray'] = list(users)
        # print(data)
        return JsonResponse({
            'status' : 200,
            'data' : data
        }, safe=False)

def loadSalesData(request):
    '''
    该方法返回两个列表
    一个是销售量，一个是x轴label
    url: loadSalesData
    '''
    import datetime
    if request.method == "POST":
        req = json.loads(request.body)
        value = req['value']
        startdatestr = req['startdate']
        enddatestr = req['enddate']
        merchant = req['merchantName']
        sd = startdatestr.split('T')[0].split('-')
        ed = enddatestr.split('T')[0].split('-')
        startdate = date(int(sd[0]), int(sd[1]), int(sd[2]))
        enddate = date(int(ed[0]), int(ed[1]), int(ed[2]))

        if value == 'all' :
            p = Order.objects.filter(merchantName=merchant).values()
        else:
            p = Order.objects.filter(merchantName=merchant).filter(productName=value).values()

        if (enddate - datetime.date.today()).days > 0:
            enddate = datetime.date.today()

        range_days = []
        for i in range(0, (enddate - startdate).days + 1):
            range_days.append(str(startdate + datetime.timedelta(days=i)))

        sales = [0 for i in range_days]
        for i in p:
            orderdate = i['time_created'].date()
            if (enddate - orderdate).days > 0:
                sales[(orderdate - startdate).days] += i['inventory']

        interval = round(len(range_days) / 12)

        return JsonResponse({
            'status' : 200,
            'labelX' : range_days,
            'valueY' : sales,
            'interval' : interval
        })

def loadProfitData(request):
    '''
    该方法返回两个列表
    一个是销售量，一个是x轴label
    url: loadProfitData
    '''
    import datetime
    if request.method == "POST":
        req = json.loads(request.body)
        year = req['year']
        year = int(year)
        groupby = req['groupby']
        merchant = req['merchantName']

        totalprofit = 0

        p = Order.objects.filter(merchantName=merchant).values()

        startdate = datetime.date(int(year), 1, 1)
        enddate = datetime.date(int(year), 12, 31)

        range_days = []
        # for i in range(0, (enddate - startdate).days + 1):
        #     print((startdate + datetime.timedelta(days=i)).isocalendar()[1])

        for i in p:
            totalprofit += i['profit']


        if groupby == 'days':
            for i in range(0, (enddate - startdate).days + 1):
                range_days.append(str(startdate + datetime.timedelta(days=i))[-5:])
            profit = [0 for _ in range_days]
            for i in p:
                orderdate = i['time_created'].date()
                if orderdate.year == year:
                    profit[(orderdate - startdate).days] += float(i['profit'])
            interval = 365 // 30
        elif groupby == 'weeks':
            if enddate.isocalendar()[1] == 1:
                weekmax = 54
            else:
                weekmax = enddate.isocalendar()[1] + 1
            for i in range(1, weekmax):
                range_days.append(str(i))
            profit = [0 for _ in range_days]
            for i in p:
                orderdate = i['time_created'].date()
                if orderdate.year == year:
                    profit[orderdate.isocalendar()[1]] += i['profit']
            interval = 0
        elif groupby == 'months':
            for i in range(1, 13):
                range_days.append(str(i))
            profit = [0 for _ in range_days]
            for i in p:
                orderdate = i['time_created'].date()
                if orderdate.year == year:
                    profit[orderdate.month - 1] += i['profit']
            interval = 0
        elif groupby == 'years':
            range_days = ['2016', '2017', '2018', '2019', '2020', '2021']
            profit = [0 for _ in range_days]
            profit[-1] = totalprofit
            interval = 0
        return JsonResponse({
            'status' : 200,
            'labelX' : range_days,
            'valueY' : profit,
            'interval' : interval,
            'totalprofit' :totalprofit
        })



def drawStatistic(request):
    '''
    disabled
    url： statistic/
    该方法会在后端生成一张统计图片，并返回图片名称
    cla 1 商品
    cla 0 商家
    '''
    if request.method == "POST":
        req = json.loads(request.body)
        cla = req['class']
        name = req['name']
        import os
        import datetime
        from django.conf import settings  
        import matplotlib.pyplot as plt
        def get_nday_list(n):
            before_n_days = []
            for i in range(1, n + 1)[::-1]:
                before_n_days.append(str(datetime.date.today() - datetime.timedelta(days=i)))
            return before_n_days

        #  params
        date_length = 30
        step = 5
        if cla == 1:
            filename = name + '_product.jpg'
        if cla == 0:
            filename = name + '_merchant.jpg'
        filename = filename.replace(" ", 'c')
        print("filename", filename)
        filepath = os.path.join(settings.STATICFILES_DIRS[0],'statistic/' + filename)

        #  check 
        if os.path.exists(filepath) :
            os.remove(filepath)

        #  x, y data
        date_list = get_nday_list(date_length)
        # .filter(~Q(status!="Pending")).filter(~Q(status!="Canceled"))
        if cla == 1:
            p = Order.objects.filter(productName=name).filter(~Q(status="Pending")).filter(~Q(status="Canceled")).values()
        elif cla == 0:
            p = Order.objects.filter(merchantName=name).filter(~Q(status="Pending")).filter(~Q(status="Canceled")).values()
        else:
            return JsonResponse({
                'status' : 500,
                'msg' : 'false',
            })
        p = list(p)
        order_list = [(str(i['time_created'].date()), i['inventory']) for i in p]
        count_list = []
        for i in date_list:
            count = 0
            for j in order_list:
                if j[0] == i:
                    count += j[1]
            count_list.append(count)
        # count_list = [order_list.count(i) for i in date_list]

        #  draw and save pic
        plt.figure(figsize=(9, 4), dpi=144)
        plt.plot(date_list, count_list, '-')
        plt.title(name)
        plt.xlabel("Date [Year | Month | Day]")
        plt.ylabel("sales")
        plt.xticks(range(0,date_length,step))
        # plt.show()
        plt.savefig(filepath)
        return JsonResponse({
            'status' : 200,
            'msg' : 'picture load complete',
            'src' : filename
        })

    
