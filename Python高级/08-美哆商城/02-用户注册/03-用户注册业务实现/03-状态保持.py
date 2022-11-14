"""
1- django自带的login()方法设置session并保存在redis中
    login(请求, 储存对象)

2- 自定义过期时间
    在setting.py下
        SESSION_COOKIE_AGE = 172800
"""
