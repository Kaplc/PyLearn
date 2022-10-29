from django.urls import *
from .views import *

app_name = 'view'

urlpatterns = [
    re_path(r'^index$', index, name='view'),
    # url位置传参
    re_path(r'^url_p/(\d+)/(\d+)$', url_position),
    # url关键字传参
    re_path(r'^url_k/(?P<v1>\d+)/(?P<v2>\d+)', url_keyword),
    # url字符串传参
    re_path(r'^url_s/', query_string),
    # 请求体POST表单传参
    re_path(r'^body_bf/', request_body_fdata),
    # 请求体POST非表单
    re_path(r'^body_bnf/', request_body_nfdata),
    # 请求头传参
    re_path(r'^header/', request_header),
    # HttpResponse_I
    re_path(r'resi/', http_response_i),
    # HttpResponse_II
    re_path(r'resii/', http_response_ii),

]
