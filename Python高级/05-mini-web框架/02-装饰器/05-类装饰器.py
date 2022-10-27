if __name__ == '__main__':
    class MyDecorator(object):
        # init不是int
        def __init__(self, func):
            # __func内部使用定义成私有属性
            self.__func = func

        def __call__(self, *args, **kwargs):
            print("类装饰器")
            self.__func()


    @MyDecorator
    def show():
        print("原函数")

    show()

