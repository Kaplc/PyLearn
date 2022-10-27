"""
在settings.py中保存了数据库的连接配置信息，Django默认初始配置使用sqlite数据库

切换MySQL数据库步骤:
    1) 安装PyMySQL
    2) 在工程配置目录__init__.py添加语句:
        import pymysql
        pymysql.install_as_MySQLdb()
        作用是让Django的ORM能以mysqldb的方式来调用PyMySQL
    3) 修改DATABASES配置信息(setting.py)
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'HOST': '127.0.0.1',  # 数据库主机
                'PORT': 3306,  # 数据库端口
                'USER': 'root',  # 数据库用户名
                'PASSWORD': 'mysql',  # 数据库用户密码
                'NAME': 'book'  # 数据库名字
            }
        }
    4) 在MySQL中创建数据库
"""