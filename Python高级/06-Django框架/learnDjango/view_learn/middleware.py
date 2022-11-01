# 定义一个中间件
# 中间件工厂函数需要接收一个可以调用的get_response对象。
# 返回的中间件也是一个可以被调用的对象，并且像视图一样需要接收一个request对象参数，
# 返回一个response对象

def my_middleware(self, get_request):
    """123"""
    # 初始化, 第一次使用中间件的时候被调用
    print("中间件初始化语句执行, 仅在服务器启动时初始化, 只执行一次")

    def middleware(request):
        print("中间件view处理前调用")
        response = get_request(request)

        print("中间件view处理后被调用")

        return response

    return middleware

    # 注意：Django运行在调试模式下，中间件init部分有可能被调用两次
