"""
1- authenticate(username=username, password=password)方法
    Django自带的用户认证, 传入用户名和密码参数校验.
    用户存在返回用户对象, 不存在返回None

2- login(请求对象, 用户对象)
    Django登录函数标记用户已登录

3- request.session.set_expiry(None)
    设置session过期时间单位秒
    填None使用全局设置好的过期时间

4- 重写父对象方法
    定义一个同名函数和传入相同参数

"""
