# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django import forms
from models import User, goods
from tkMessageBox import *
from app01 import models
from django.template import  Context
import qrcode
from django.utils.six import BytesIO
# Create your views here.
class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=50)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())
    email = forms.EmailField(label='邮箱')

def regist(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            email = userform.cleaned_data['email']
            User.objects.create(username=username,password=password,email=email)
            User.save
            showinfo(title='注册',message='注册成功')
            return render_to_response('login.html',{'userform':userform})
            # return HttpResponse('regist successs!!!')
    else:
        userform = UserForm()
    return  render_to_response('regist.html',{'userform':userform})

def login(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            user = User.objects.filter(username__exact=username,password__exact=password)

            if user:
                return render_to_response('index.html',{'userform':userform})
            else:
                return  HttpResponse('用户名或密码错误,请重新登录')
    else:
        userform = UserForm()
    return render_to_response('login.html',{'userform':userform})

def index(req):
    username = req.COOKIES.get('username','')
    return render_to_response('index.html' ,{'username':username})
    goods_list = goods.objects.all()
    return render_to_response("index.html",{"goods_list":goods_list})

def table(request):
    goods_list = goods.objects.all()
    # count = 80
    # curr_page = 1
    # if count % 3 ==0:
    #     num_pages=count/3
    # else:
    #     num_pages=count/3+1
    # last_pages=int(num_pages)-1
    # int_curr_page = int(curr_page)
    # if int_curr_page == 0:
    #     has_previous = False
    # else:
    #     has_previous=True
    # if int_curr_page== int(num_pages)-1:
    #     has_next =False
    # else:
    #     has_next = True
    # previous_page_number = int_curr_page-1
    # next_page_number = int_curr_page+1
    # return render_to_response("table.html",{"goods_list":goods_list,'count':count,'num_pages':num_pages,
    #                                         'last_page':last_pages,'previous_page_num':previous_page_number,
    #                                         'next_page_number':next_page_number,
    #                                         'has_previous':has_previous,'has_next':has_next})
    return render_to_response("table.html",{"goods_list":goods_list,})
    q = request.GET.get('q')
    error_msg = ''

    if not q:
        error_msg = '请输入关键词'

    post_list = Post.objects.filter(title__icontains=q)
    return render(request, 'table.html', {'error_msg': error_msg,
                                               'goods_list': goods_list})

def erweima(request):
    return render_to_response("erweima.html")



