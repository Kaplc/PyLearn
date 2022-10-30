from django.urls import *
from .views import *

app_name = 'view'

urlpatterns = [
    # ----------request-----------
    re_path(r'^index', index, name='view'),
    # url位置传参
    re_path(r'^url_p/(\d+)/(\d+)', url_position),
    # url关键字传参
    re_path(r'^url_k/(?P<v1>\d+)/(?P<v2>\d+)', url_keyword),
    # url字符串传参
    re_path(r'^url_s/', query_string),
    # 请求体POST表单传参
    re_path(r'^body_bf/', request_body_fdata),
    # 请求体POST非表单
    re_path(r'^body_bnf/', request_body_nfdata),
    # 请求头传参

    # ------------response------------
    re_path(r'header/', request_header),
    # HttpResponse_I
    re_path(r'resi/', http_response_i),
    # HttpResponse_II
    re_path(r'resii/', http_response_ii),
    # JsonRespons
    re_path(r'json/', json_response),
    # redirect重定向
    re_path(r'redirect', redirect_i),

    # ------------cookie-----------
    re_path(r'set_cookie', set_cookie),
    re_path('read_cookie', read_cookie),
    re_path('del_cookie', del_cookie),

    # -----------session------------
    re_path('set_session', set_session),
    re_path('get_session', get_session),
    re_path('del_session', del_session),

    # ----------类视图-----------
    re_path('viewclass', CenterView.as_view()),

    # ---------中间件------------
    re_path('middleware', middleware_test),

    # ---------Django自带模板---------
    re_path('self_template', self_templates),

    # -------模板语言--------
    re_path('grammar', grammar),

    # -------过滤器-------
    re_path('filter', filter_test),

    # -------模板继承--------
    re_path('inherit', inherit_test)

]
