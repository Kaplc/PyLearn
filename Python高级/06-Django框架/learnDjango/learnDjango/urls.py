"""learnDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
# 浏览器输入的url先到项目的urls.py进行顺序匹配
# 匹配成功引导到相应模块, 匹配失败返回404
# urlpatterns列表的元素是url
#     url的参数: r(转义)'正则表达式', 模块路径
# 浏览器输入的url中的http://ip:port/ 和 get post不参与正则匹配
# url()已经更新成pat()

urlpatterns = [
    path('admin/', admin.site.urls),
    # r前缀的作用就是告诉解释器，我这个字符串不包含转义字符，比如字符串中如果包含'\n'，则不将其视为换行符，
    # 而视为一个'\'字符和'n'字符来处理r前缀的作用就是告诉解释器，
    # 我这个字符串不包含转义字符，比如字符串中如果包含'\n'，则不将其视为换行符，而视为一个'\'字符和'n'字符来处理
    # 就是不用在\前面再打一个\
    re_path(r'^book$', include('book.urls')),
    path('view/', include('view_learn.urls', namespace='view_learn'))

]
