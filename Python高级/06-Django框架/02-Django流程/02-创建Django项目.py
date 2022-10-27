"""
1- 创建工程的命令为： django-admin startproject 工程名称
    文件说明:
        与项目同名的目录，此处为 - 工程名称。
        settings.py是项目的整体配置文件。
        urls.py是项目的URL配置文件。
        wsgi.py是项目与WSGI兼容的Web服务器入口。
        manage.py是项目管理文件，通过它管理项目。

2- 快速预览到开发的效果: python manage.py runserver ip:端口
    (默认IP是127.0.0.1，默认端口为8000)

3- django默认工作在调式Debug模式下，如果增加、修改、删除文件，服务器会自动重启。

4- 按ctrl+c停止服务器

5- 创建子应用: python manage.py startapp 子应用名称
    文件说明:
        admin.py文件跟网站的后台管理站点配置相关。
        apps.py文件用于配置当前子应用的相关信息。
        migrations目录用于存放数据库迁移历史文件。
        models.py文件用户保存数据库模型类。
        tests.py文件用于开发测试用例，编写单元测试。
        views.py文件用于编写Web应用视图

6- 注册安装子应用: settings.py中的INSTALLED_APPS加入子应用的配置信息文件apps.py中的Config类
    'book.apps.BookConfig'

"""