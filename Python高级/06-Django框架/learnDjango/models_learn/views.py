from django.shortcuts import render
from models_learn.models import BookInfo, PeopleInfo
# Create your views here.

person = PeopleInfo.objects.get(name='itheima')
person.name = 'itcast'
person.save()

book = BookInfo.objects.get(id=1)
