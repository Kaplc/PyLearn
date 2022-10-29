import json

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.urls import reverse


# ------namespace的使用--------
def index(request):
    # 项目的namespace:子应用的name
    path = reverse('view_learn:view')
    print(path)
    return HttpResponse("OK")


# ------url路径传参--------
# 位置传参
# v1, v2接收url传参
def url_position(request, v1, v2):
    print('v2: ', v2)
    print('v2: ', v2)
    return HttpResponse("url_位置传参")


# 关键字传参
# v1, v2 是key
def url_keyword(request, v2, v1):
    print('v2: ', v2)
    print('v1: ', v1)
    return HttpResponse("url_关键字传参")


# ---------字符串传参（形如?k1=v1&k2=v2）----------
def query_string(request):
    # get()获取单个参数, 多个值只会获取最后一个
    v1 = request.GET.get('v1')
    v2 = request.GET.get('v2')
    print("get('v1'): ", v1)
    print("get('v2'): ", v2)

    # getlist()获取参数以列表返回
    alist = request.GET.getlist('v1')
    print("getlist('v1')", alist)
    # 调用列表的另一值
    print(alist[1])
    return HttpResponse("字符串传参")


# --------请求体传参----------

def request_body_fdata(request):
    a = request.POST.get('v1')
    b = request.POST.get('v2')
    alist = request.POST.getlist('v1')
    print(request.POST)
    print(a)
    print(b)
    print(alist)
    return HttpResponse("请求体传参表单")


def request_body_nfdata(request):
    # 接收JSON字符串
    json_data = request.body
    edata = json_data.decode()
    print(edata)
    print(type(edata))

    # JSON字符串转字典
    data = json.loads(json_data)
    print(data)
    print(type(data))
    print(data['v1'])
    print(data['v2'])
    return HttpResponse("请求体传参非 表单")


# -------请求头传参-------
def request_header(request):
    print(request.META['CONTENT_TYPE'])
    print(request.META['REMOTE_HOST'])

    # 常用的request对象属性

    print(request.method)  # method属性获取请求的方法
    print(request.user)  # 请求的用户对象
    print(request.path)  # 一个字符串，表示请求的页面的完整路径，不包含域名和参数部分
    print(request.encoding)  # 一个字符串，表示提交的数据的编码方式
    print(request.FILES)  # 一个类似于字典的对象，包含所有的上传文件
    return HttpResponse("请求头传参")


# ---------HttpResponse对象------------

def http_response_i(request):
    # 获取HttpResponse对象
    response = HttpResponse()
    # 调用属性方式设置状态码(100-599)
    response.status_code = 200
    # 自定义响应头It-cast, 值为Python
    response['It-cast'] = 'Python'
    return response


def http_response_ii(res):
    # 或者
    # HttpResponse(content=响应体, content_type=响应体数据类型, status=状态码)
    # content_type是mime类型: text/html, text/css等等
    # 状态码只能是系统规定的100~599
    # context只能传递字符串
    data = {
        "data": "aaa"
    }

    return HttpResponse(content=data, content_type='', status=200)


# --------JsonResponse----------
# 返回json数据，可以使用JsonResponse来构造响应对象

# 自动设置
# 帮助我们将数据转换为json字符串
# 设置响应头Content-Type为application/json

from django.http import JsonResponse


def json_response(req):
    json_data = {
        "aaa": "1",
        "bbb": "2"
    }
    return JsonResponse(json_data)


# --------redirect重定向-----------
from django.shortcuts import redirect


def redirect_i(request):
    # 参数是除ip和端口的完整的url
    return redirect('/view/index')


# ----------cookie----------------

def set_cookie(req):
    response = HttpResponse()
    # 从响应发送cookie
    # set_cookie(cookie名, cookie值, max_age=过期时间(秒))
    response.set_cookie("set_cookie", "value", max_age=100)
    return response


def read_cookie(req):
    # 从请求获取cookie
    cookie = req.COOKIES.get('set_cookie')
    print(cookie)
    return HttpResponse("read_cookie")


def del_cookie(req):
    # 从请求删除cookie
    res = HttpResponse()
    res.delete_cookie('set_cookie')
    return res


# -----------session-------------

def set_session(req):
    print(req.COOKIES)
    username = 'zzy'
    # 设置session, 并保存至数据库
    # req.session['储存到数据库的关键字'] = username
    req.session['username'] = username

    return HttpResponse("set_session")


def get_session(req):
    # 从数据库获取session通过关键字
    session_data = req.session.get('username')
    print(session_data)

    return HttpResponse("get_session")


def del_session(req):
    # req.session.clear()
    # 从数据库删除session
    req.session.flush()

    return HttpResponse()
