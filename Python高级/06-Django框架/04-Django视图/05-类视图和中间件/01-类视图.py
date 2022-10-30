"""
作用: 在一个视图函数处理两种不同的请求

普通方式: 在view的函数里面使用if判断request.method为get还是post
    代码可读性与复用性都不佳

使用类视图继承View


"""
