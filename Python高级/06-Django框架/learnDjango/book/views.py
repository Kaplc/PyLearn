from django.shortcuts import render
from django.http import HttpResponse
from models_learn.models import BookInfo, PeopleInfo
from django.db import models

# Create your views here.


"""
1, 第一个参数是请求或和请求相关的, 是HttpResponse实例对象
2, 所以返回的也必须是个HttpResponse实例对象

"""


def index(request):
    context = {"title": '测试模板处理数据'}
    # render(当前请求request, 模板文件, context=None)

    return render(request, 'book/index.html', context)
    return HttpResponse("OK")


def book_info(request):
    books = BookInfo.objects.all()
    print(books)
    context = {
        'books': books
    }

    person = PeopleInfo.objects.get(name='itcast')
    book = BookInfo.objects.get(id=1)

    person.name = 'itcast'
    person.save()
    PeopleInfo.objects.filter(name='itcast').update(name='传智播客')
    for i in books:
        print(i)
    return render(request, 'book/bookInfo.html', context)
