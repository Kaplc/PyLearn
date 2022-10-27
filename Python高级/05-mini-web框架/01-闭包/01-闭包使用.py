# 闭包作用保存外部函数的变量
# 形成条件: 1) 函数嵌套 2) 内部函数使用外部函数变量和参数 3) 外部函数返回内部函数

def func_out():
    num1 = 10

    def func_inner(num2):
        result = num1 + num2
        print("结果: ", result)
    # 返回内部函数
    return func_inner


# 调用外部函数返回值是内部函数,并传递到new_func
new_func = func_out()

# 相当于使用内部函数并传参
new_func(1)


# 案例

def config_name(name):
    def inner(message):
        print(name + ':' + message)

    return inner


# 创建tom实例并向外部函数传参
tom = config_name("Tom")
# 内部函数传参
tom("你好")