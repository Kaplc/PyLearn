if __name__ == '__main__':
    # 带有参数装饰器: 定义一个外部函数嵌套装饰器, 外部函数接收参数
    def decorator(flag):

        def out(func):

            def inner(a, b):
                if flag == "+":
                    print("加法计算")
                elif flag == "-":
                    print("减法计算")
                inner_result = func(a, b)
                return inner_result
            return inner

        return out


    @decorator("+")  # decorator_out = decorator("+"), add_num = inner = decorator_out(add_num)
    def add_num(a, b):
        add_result = a + b
        return add_result


    @decorator("-")
    def sub_num(a, b):
        sub_result = a - b
        return sub_result


    result = add_num(1, 2)
    print(result)
