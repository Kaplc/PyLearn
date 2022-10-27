"""
视图作用: 处理请求的地方, 并把结果返回给请求者

使用视图时需要进行两步操作
    1.定义视图(views.py)
        1) 在每个子应用的views.py
        2) 视图的第一个参数是HttpRequest类型的对象reqeust，包含了所有请求信息
            def index(request):
        3) 视图必须返回HttpResponse对象，包含返回给请求者的响应信息:
            return HttpResponse
        4) 需要导入HttpResponse模块: from django.http import HttpResponse

    2.配置URLconf
        查找视图的过程 :
            1.请求者在浏览器地址栏中输入URL, 请求到网站.
            2.网站获取URL信息.
            3.然后与编写好的URLconf逐条匹配.
                1) URlconf入口: 匹配url先在setting.py找入口文件--ROOT_URLCONF = 'learnDjango.urls'
                2) 先在项目的urls.py进行匹配, 成功引导到对应模块, 失败返回404
                3)
            4.如果匹配成功则调用对应的视图.
            5.如果所有的URLconf都没有匹配成功.则返回404错误.


    注意!!!!---url()已经更新成re_pat(): 详情查看文档说明
"""