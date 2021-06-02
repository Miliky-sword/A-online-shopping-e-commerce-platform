from django.shortcuts import render
import hashlib
from user.models import LoginUser
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
import json
# Create your views here.

def hello(request):
    return HttpResponse('hello world')

def setPassword(password):
    '''
    加密密码
    '''
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result

def allUsers(request):
    '''
    返回所有用户
    '''
    if request.method == 'GET':
        data = {}
        users = LoginUser.objects.all().values()
        data['data'] = list(users)
        # print(data)
        return JsonResponse({
            'data' : data
        }, safe=False)

def allMerUsers(request):
    '''
    返回所有用户
    '''
    if request.method == 'POST':
        data = {}
        users = LoginUser.objects.filter(user_type=1).values()
        data['dataArray'] = list(users)
        # print(data)
        return JsonResponse({
            'data' : data
        }, safe=False)

def removeUserByName(request):
    '''
    通过用户名删除用户
    '''
    if request.method == "POST":
        req = json.loads(request.body)
        username = req['username']
        print("delete ", username)
        LoginUser.objects.filter(username=username).delete()
        return JsonResponse({
            'status': 200,
            'msg': 'delete success'
        })
    

def register(request):
    '''
    注册
    '''
    if request.method=='POST':
        req = json.loads(request.body)
        #email = request.POST.get('email')
        username = req['username']
        password = req['password']
        user_type= req['user_type']
        address = req['address']
        print(username, password, user_type, address)
        if username:
            # 判断用户名是否存在
            loginuser=LoginUser.objects.filter(username=username).first()
            if not loginuser:
                # 不存在，写库
                user=LoginUser()
                user.username=username
                user.password=setPassword(password)
                user.user_type=user_type
                user.address = address
                user.save()
                return JsonResponse({
                    'status': 200,
                    'msg': 'zhu ce cheng gong'
                })
            else:
                # 存在
                error_msg = '用户名已经被注册，请登录'
        else:
            error_msg = '用户名不可为空'
        return JsonResponse({
            'status' : 500,
            'msg':error_msg
        })
    return JsonResponse({
        'status': 501,
        'msg' : 'zhu ce shi bai 2'
    })

def login(request):
    if request.method=='POST':
        
        req = json.loads(request.body)
        username = req['username']
        password = req['password']
        print(username, password)
        #user_type= request.POST.get('user_type')
        #code = request.POST.get('vaild_code')
        if username:
            print(3)
            user = LoginUser.objects.filter(username=username).first()
            if user:
                print("login 4")
                if user.password==setPassword(password):
                    #vaild_code = Vaild_Code.objects.filter(code_status=0,code_user=email,code_content=code).first()
                    if True:#vaild_code:
                        if True:#time.time() - vaild_code.code_time < 120:
                            data = {
                                'msg' : "deng lu cheng gong",
                                'status' : 200,
                                'userName' : user.username,
                                'userType' : user.user_type   
                            }
                            response = JsonResponse(data)
                            response.set_cookie('username', username)
                            response.set_cookie('password', password)
                            #response.set_cookie('user_type', user.user_type)
                            #response.set_cookie('userid', user.id)
                            request.session['username'] = user.username
                            request.session['userType'] = user.user_type  
                            #response.content = '登录成功'
                            #vaild_code.code_status = 1
                            print("login 2")
                            #vaild_code.save()
                            return response
                        else:
                            error_msg = '验证码超时，请重新获取'
                    else:
                        error_msg = '验证码不正确'
                else:
                    error_msg = '密码错误'
            else:
                error_msg = '该用户不存在，请先注册'
        else:
            error_msg = '邮箱不可为空'
        data = {
            'msg' : error_msg,
            'status' : 500
        }
        print(1)
        return JsonResponse(data)
    return HttpResponse(content="jieshu")

def addsig(request):
    '''
    url: addsig/
    该函数为指定用户添加一条签名
    '''
    if request.method == 'POST':
        req = json.loads(request.body)
        username = req['username']
        sig = req['sig']
        usr = LoginUser.objects.filter(username=username).first()
        usr.sig = sig
        try:
            usr.save()
        except:
            return JsonResponse({
                'status' : 500,
                'msg' : "Sorry! change personalized signature failed"
            })
        return JsonResponse({
            'status' : 200,
            'msg' : 'The personalized signature has changed'
        })

def loadinfo(request):
    '''
    url: loadinfo/
    该函数返回指定用户的所有信息
    '''
    if request.method == 'POST' :
        req = json.loads(request.body)
        username = req['username']
        print("username", username)
        try :
            usr = LoginUser.objects.filter(username=username).values()
        except:
            return JsonResponse({
                'status' : 500,
                'msg' : "load user's info failed"
            })
        data = {}
        dataArray = list(usr)
        data['dataArray'] = dataArray
        return JsonResponse({
            'status' : 200,
            'msg' : "load user info done",
            'data': data
        })

def editinfo(request):
    '''
    url: editinfo/
    该函数用于修改个人信息
    '''
    if request.method == 'POST':
        req = json.loads(request.body)
        username = req['username']
        address = req['address']
        phonenumber = req['phonenumber']
        password = req['password']
        email = req['email']
        usr = LoginUser.objects.filter(username=username).first()
        if address != '':
            usr.address = address
        if phonenumber != '':
            usr.phoneNumber = phonenumber
        if password != '':
            print(len(setPassword(password)))
            usr.password = setPassword(password)
        if email != '':
            usr.email = email
        try:
            usr.save()
        except:
            return JsonResponse({
                'status' : 500,
                'msg': 'Invalid format! Please check it again!'
            })
        return JsonResponse({
            'status':200,
            'msg' : 'the information has changed'
        })