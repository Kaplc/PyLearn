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
    HttpRequest对象的属性GET、POST都是QueryDict类型的对象
    python字典不同，QueryDict类型的对象用来处理同一个键带有多个值的情况


    get()：根据键获取值, 不存在则返回None值
        get('键',默认值) # 设置默认值进行后续处理

    getlist()：根据键获取值, 值以列表返回
        getlist('键',默认值)

3- 查询字符串Query String (?k1=v1&k2=v2)

        # 获取k1的值
        a = request.GET.get('k1')

        # 获取k1的值返回列表
        alist = request.GET.getlist('k1')

    重要：查询字符串不区分请求方式，即假使客户端进行POST方式的请求，依然可以通过request.GET获取请求中的查询字符串数据

3- 请求体
    Django默认开启了CSRF防护，会对上述请求方式进行CSRF防护验证，
    在测试时可以关闭CSRF防护机制，方法为在settings.py文件中注释掉CSRF中间件

    发送请求体数据的请求方式有POST、PUT、PATCH、DELETE


    使用Postman发送POST表单 -> 点击 body-> form-data
    1) 表单类型数据
        通过request.POST获取, 返回QueryDict
            b = request.POST.get('k1')
            alist = request.POST.getlist('k2')


    使用Postman发送POST非表单 -> 点击 body-> raw
    2) 非表单类型数据
        Django无法自动解析, 只能通过获取原始数据解析(JSON等)

        请求的JOSN: {"a": 1, "b": 2}
        json_str = request.body # 返回bytes类型
        req_data = json.loads(json_str)



4- 请求头
    常见请求头:
        CONTENT_LENGTH– 请求正文的长度（以字符串形式）。
        CONTENT_TYPE– 请求正文的MIME类型。
        HTTP_ACCEPT– 响应的可接受内容类型。
        HTTP_ACCEPT_ENCODING– Acceptable 响应的编码。
        HTTP_ACCEPT_LANGUAGE– Acceptable 响应的语言.
        HTTP_HOST– 客户端发送的HTTP主机标头。
        HTTP_REFERER– 参考页（如有）。
        HTTP_USER_AGENT– 客户端的用户代理字符串。
        QUERY_STRING– 查询字符串，作为单个（未分析）字符串。
        REMOTE_ADDR– 客户端的IP地址。
        REMOTE_HOST– 客户端的主机名。
        REMOTE_USER– 由Web服务器验证的用户（如果有）。
        REQUEST_METHOD– 字符串，如“GET”或“POST”。
        SERVER_NAME– 服务器的主机名。
        SERVER_PORT– 服务器的端口（作为字符串）。

    # 获取请求头的CONTENT_TYPE
    data = request.META['CONTENT_TYPE']

5- 常用HttpRequest对象属性

    request.method  # method属性获取请求的方法
    request.user  # 请求的用户对象
    request.path  # 一个字符串，表示请求的页面的完整路径，不包含域名和参数部分
    request.encoding # 一个字符串，表示提交的数据的编码方式
        如果为None则表示使用浏览器的默认设置，一般为utf-8。
        这个属性是可写的，可以通过修改它来修改访问表单数据使用的编码，
        接下来对属性的任何访问将使用新的encoding值。
    request.FILES  # 一个类似于字典的对象，包含所有的上传文件
"""
