# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django import forms
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.template import loader, Context, Template
import os

def login(request):

    user_loggedin = 'Guest'
    errors_list = []
    if request.method == 'POST':
        #print('pp: ', request.POST.get('username'), request.POST.get('password'))
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        #print('authuser', user)
        if user is not None:
            if user.is_active:
               auth_login(request, user)
               uu = request.user
               loginusername = user
               u = User.objects.get(username=uu)
               return HttpResponseRedirect('/')
            else:
               return HttpResponse('用户没有启用!')
        else:
               return HttpResponse('用户名或者密码错误！')
    else:
        context = {'errors_list': errors_list, 'user_loggedin': user_loggedin}
        return render_to_response('login.html')           


def loginout(request):
    auth_logout(request)
    return HttpResponseRedirect('/login/')

@login_required
def index(req):
    return render_to_response('index.html')



@login_required
def salt(request):
    if request.method == 'POST':
        A = request.POST['a1']
        B = request.POST.getlist("b1")
        print A
        os.system('> /home/ops/ip.txt')
        for i in B:
            os.system('echo "%s\n">>/home/ops/ip.txt'%i)
        sun = os.popen('pssh  -h /home/ops/ip.txt -i sudo  "%s"'%A).read().strip()
        ss = sun.split('\n')
        return render_to_response('salt.html',{'ss':ss})
    else:
        return render_to_response('salt.html')


