from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from django.urls import reverse


def index(request):
    # 项目的namespace:子应用的name
    path = reverse('view_learn:view')
    print(path)
    return HttpResponse("OK")


# v1, v2接收url传参
def url(request, v1, v2):
    print('v1: ', v1)
    print('v2: ', v2)
    return HttpResponse("url_v1v2")

