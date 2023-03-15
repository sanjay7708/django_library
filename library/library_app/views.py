from django.shortcuts import render
from . forms import *
from django.http import HttpResponse

# Create your views here.
def login(request):
    form=Loginform
    dict={
        'form':form
    }
    return render(request,'libraryapp/login.html',context=dict)
def reg(request):
    reg=RegisterForm
    dict={
        'reg':reg
    }
    return render(request,'libraryapp/regiter.html',context=dict)