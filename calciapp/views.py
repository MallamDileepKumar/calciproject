from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def input(request):
    return render(request,'input.html',{})
def output(request):
    x = int(request.POST['t1'])
    y = int(request.POST['t2'])
    z = request.POST['calci']
    res = 0
    if z == "ADD":
        res = x+y
    elif z == "SUB":
        res = x-y
    elif z == "MUL":
        res = x*y
    else:
        res = x/y

    context = {"res":res}

    return render(request,'output.html',context=context)
