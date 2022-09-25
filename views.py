from django.http import HttpResponse
from django.shortcuts import render

from app01.models import login_msg


def login(request):
    '''
    登录
    :param request:
    :return:
    '''
    if request.method == 'POST':
        res = {}
        if 'sub' in request.POST:  # 处理表单中的登录
            username = request.POST['user']
            userma = request.POST['pw']
            tmp = login_msg.objects.filter(user=username).exists()
            if tmp:  # 若表中存在该用户名数据，则已注册
                is_reg = login_msg.objects.filter(user=username, pw=userma).exists()
                if is_reg:  # 若查询有结果
                    return render(request, 'index.html')
                else:  # 若查询无结果，则用户名或密码错误
                    res['rlt'] = '用户名或密码错误'
                    return render(request, 'login.html', res)
            else:  # 若表中无该用户名数据，则未注册
                res['rlt'] = '该用户名未注册，请注册后登录'
                return render(request, 'login.html', res)
        elif 'reg1' in request.POST:  # 处理表单中的注册，界面跳转
            return render(request, 'register.html')
        else:
            pass
    return render(request, 'login.html')


def register(request):
    '''
    注册
    :param request:
    :return:
    '''
    if request.method == 'POST':
        res = {}
        if 'reg2' in request.POST:  # 处理表单中的注册
            username = request.POST['user']
            userma = request.POST['pw']
            usermail = request.POST['mail']
            tmp = login_msg.objects.filter(user=username).exists()
            if tmp:  # 若存在该用户名相关数据，则用户已注册
                res['rlt'] = '该用户名已注册'
                return render(request, 'register.html', res)
            else:  # 用户未注册，则向数据库中插入数据
                login_msg.objects.create(user=username, pw=userma, mail=usermail)
                res['rlt'] = '注册成功'
                return render(request, 'register.html', res)
        elif 'back' in request.POST:  # 处理返回，界面跳转
            return render(request, 'login.html')
        else:
            pass
    return render(request, 'register.html')


def forgotpwd(request):
    '''
    忘记密码
    :param request:
    :return:
    '''
    if request.method == 'POST':
        res = {}
        if 'fpwd' in request.POST:  # 处理表单中的注册
            username = request.POST['user']
            usermail = request.POST['mail']
            tmp = login_msg.objects.filter(user=username, mail=usermail).exists()
            if tmp:  # 若存在该用户名相关数据，则用户已注册,可以找回
                pwd = login_msg.objects.get(user=username)
                pwd1 = pwd.__dict__  # 把格式转换成字典，再切片。
                res['olt'] = '您的密码为：'
                res['rlt'] = pwd1.get('pw')
                return render(request, 'forgotpwd.html', res)
            else:  #
                res['rlt'] = '用户名不存在或用户名与邮箱不匹配'
                return render(request, 'forgotpwd.html', res)
        else:
            pass
    return render(request, 'forgotpwd.html')


def reset(request):
    '''
        重置密码
        :param request:
        :return:
        '''
    if request.method == 'POST':
        res = {}
        if 'reset' in request.POST:  # 处理表单中的注册
            username = request.POST['user']
            newpwd = request.POST['new-pw']
            oldpwd = request.POST['old-pw']

            tmp = login_msg.objects.filter(user=username).exists()
            if tmp:  # 若存在该用户名相关数据，则用户已注册,可以找回
                ma = login_msg.objects.filter(pw=oldpwd).exists()
                if ma:
                    login_msg.objects.filter(user=username).update(pw=newpwd)
                    res['rlt'] = '重置成功'
                else:
                    res['rlt'] = '密码错误'
                return render(request, 'reset.html', res)
            else:  # 用户未注册，则向数据库中插入数据
                res['rlt'] = '用户名不存在'
                return render(request, 'reset.html', res)
        else:
            pass
    return render(request, 'reset.html')


# ----------------------------------------------------这是一条分界线---------------------------------------------------
# 页面
def index(request):
    return render(request, 'index.html')


def keyInfo(request):
    return render(request, 'keyInfo.html')


def mstp_map(request):
    return render(request, 'mstp_map.html')


def efficiencyAnalysis(request):
    return render(request, 'efficiencyAnalysis.html')


def dianfei(request):
    return render(request, 'dianfei.html')


def deviceManager(request):
    return render(request, 'deviceManager.html')


def energy_consumption(request):
    return render(request, 'energy_consumption.html')


def userMng(request):
    return render(request, 'userMng.html')
