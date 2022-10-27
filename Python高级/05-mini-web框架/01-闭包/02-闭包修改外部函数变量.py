# 闭包修改外部函数的变量

def func_out():
    num1 = 10

    def func_inner():
        # nonlocal关键字
        nonlocal num1
        num1 = 20
        print(num1)

    return func_inner


inner = func_out()
inner()
