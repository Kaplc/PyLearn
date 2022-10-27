"""
HTTP向服务器传参方式::
    1) 提取URL的特定部分
    2) 查询url中的字符串（query string)
    3) 请求体（body）中发送的数据，比如表单数据、json、xml
    4) http报文的头（header）

1- URL路径参数
    1) 从URL中获取值，需要在正则表达式中使用分组
    2) 获取参数方式:
        位置参数
            应用中urls.py
            url(r'^(\d+)/(\d+)/$', views.index)

            view.py
            def index(request, value1, value2):
                # 构造上下文
                context = {'v1':value1, 'v2':value2}
                return render(request, 'Book/index.html', context)

        关键字参数
            应用中urls.py
            # ?P<name1>: name1是参数的别名
            url(r'^(?P<value1>\d+)/(?P<value2>\d+)/$', views.index),

            view.py
            def index(request, value2, value1):
                # 构造上下文
                context = {'v1':value1, 'v2':value2}
                return render(request, 'Book/index.html', context)

2- Django中的QueryDict对象

3- 查询字符串Query String

4- 请求体

5- 请求头

"""