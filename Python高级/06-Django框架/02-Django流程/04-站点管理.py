"""
站点: 分为内容发布和公共访问两部分
    内容发布的部分由网站的管理员负责查看、添加、修改、删除数据
    Django能够根据定义的模型类自动地生成管理模块

使用Django的管理模块, 需要按照如下步骤操作 :
    1.管理界面本地化
        setting.py的LANGUAGE_CODE设置语言, TIME_ZONE设置时区
        LANGUAGE_CODE = 'zh-Hans'
        TIME_ZONE = 'Asia/Shanghai'
    2.创建管理员
        python manage.py createsuperuser
        重置密码: python manager.py changepassword 用户名
        登陆站点 :http://127.0.0.1:8000/admin
    3.注册模型类
        站点界面中没有书籍和人物管理入口,因为没有注册模型类:
        在子应用的admin.py文件中注册模型类, 导入模型模块 :from book.models import BookInfo,PeopleInfo

    4.发布内容到数据库


"""
"""
在model类内加入__str__方法, 优化展示:  

    def __str__(self):
    # 将模型类以字符串的方式输出
        return self.name

"""
