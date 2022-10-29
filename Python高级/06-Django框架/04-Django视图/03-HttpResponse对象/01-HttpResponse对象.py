"""
1- HttpResponse
    使用django.http.HttpResponse来构造响应对象
    语法:
        # content：表示返回的内容。
        # status_code：返回的HTTP响应状态码
        HttpResponse(content=响应体, content_type=响应体数据类型, status=状态码)

    例:
        from django.http import HttpResponse

        def response(request):
            return HttpResponse('itcast python', status=400)
            # 或者
            response = HttpResponse('itcast python')
            response.status_code = 400
            response['itcast'] = 'Python'
            return response

2- HttpResponse子类
    可以快速设置状态码

        HttpResponseRedirect 301
        HttpResponsePermanentRedirect 302
        HttpResponseNotModified 304
        HttpResponseBadRequest 400
        HttpResponseNotFound 404
        HttpResponseForbidden 403
        HttpResponseNotAllowed 405
        HttpResponseGone 410
        HttpResponseServerError 500

3- JsonResponse
    返回json数据，可以使用JsonResponse
    

"""