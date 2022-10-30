"""
1- 配置
    1) Django项目创建templates目录
    2) 修改setting.py的TEMPLATES配置的DIRS(路径)

2- 定义模板
    1) 创建html文件

3- 模板渲染
    步骤:
        1) 获取模板, 返回模板对象
            loader.get_template(模板文件在模板目录中的相对路径)
        2) 渲染模板, 响应请求
            模板对象.render(context=None, request=None)

    例:
        from django.http import HttpResponse
        from django.template import loader

        def index(request):
            # 1.获取模板
            template=loader.get_template('index.html')

            context={'city': '北京'}
            # 2.渲染模板
            return HttpResponse(template.render(context))



    Django提供了一个函数render可以简写上述代码

    from django.shortcuts import render

    def index(request):
        context={'city': '北京'}
        return render(request,'index.html',context)




"""
