"""
cookie流程:
    首次访问:
        1, 浏览器没有携带cookie信息访问服务器
        2, 服务器检测到没有cookie
        3, 返回响应的时候携带cookie

    以后访问:
        1, 有cookie信息后每次请求都会带有cookie
        2, 服务器检测cookie识别身份



cookie特点:
    1, 键值对储存
    2, 基于域名, 不同域名不能互相访问


1- 设置cookie
    HttpResponse.set_cookie(cookie名, value=cookie值, max_age=cookie有效期)
    max_age单位为秒，默认为None 。如果是临时cookie，可将max_age设置为None

    例:
        def cookie(request):
            response = HttpResponse('ok')
            response.set_cookie('itcast1', 'python1')  # 临时cookie
            response.set_cookie('itcast2', 'python2', max_age=3600)  # 有效期一小时
            return response

2- 读取Cookie
    request.COOKIES.get('关键字')

    例:
        def cookie(request):
            cookie1 = request.COOKIES.get('key')
            print(cookie1)
            return HttpResponse('OK')

3- 删除cookie
    response.delete_cookie('key')

    例:
        response.delete_cookie('key')




--------------session-----------------

session是储存的服务器上面的cookie
在浏览器称cookie

session的流程:
    首次请求:
        1) 设置cookie同时session会保存在服务器

1- 启用Session
    Django默认启用Session, 在setting.py查看

2- session储存
    1) 数据库

    2) 本地缓存
        存储在本机内存中，如果丢失则不能找回，比数据库的方式读写更快
    3) 混合储存
        优先从本机内存中存取，如果没有则从数据库中存取
    4) Redis储存


3- session操作
    1) 设置
        request.session['键']=值
    2) 读取
        request.session.get('键',默认值)
    3) 删除所有值
        request.session.clear()
    4) 删除所有键值
        request.session.flush()
    5) 删除指定
        del request.session['键']
    6) 设置有效期
        如果value是一个整数，session将在value秒没有活动后过期。
        如果value为0，那么用户session的Cookie将在用户的浏览器关闭时过期。
        如果value为None，那么session有效期将采用系统默认值，
         默认为两周，可以通过在settings.py中设置SESSION_COOKIE_AGE来设置全局默认值
        request.session.set_expiry(value)



"""


