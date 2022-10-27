if __name__ == '__main__':

    # 通用装饰器
    def decorator(func):

        def inner(*args, **kwargs):
            print("正在执行加法运算: ")
            num = func(*args, **kwargs)
            return num

        # 返回函数不用加()
        return inner


    @decorator  # add_num = decorator(add_num)
    def add_num(*args, **kwargs):
        # args元组类型
        # kwargs字典类型
        result = 10

        for value in args:
            result += value

        # kwargs.values()取字典的值遍历
        for value in kwargs.values():
            result += value

        return result


    add_num = decorator(add_num)
    add_result = add_num(1, 2)
    print("结果为: ", add_result)


    @decorator
    def text():
        print("文字")


    text()
