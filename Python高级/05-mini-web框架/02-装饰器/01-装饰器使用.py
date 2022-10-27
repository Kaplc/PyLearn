import time


# 装饰器定义: 给原有函数添加额外功能

# 本质闭包函数
def decorator(func_out):
    def inner():
        print("已添加登陆验证")
        func_out()

    return inner


def comment():
    print("发表评论")


# 传入原函数名称给装饰器, 在内部函数执行原函数和新功能.
# 最后返回内部函数并把原函数同名替换
comment = decorator(comment)

comment()


@decorator  # 简写: 相当于comment_1 = inner, inner = decorator(comment_1) --> comment_1 = decorator(comment_1)
def comment_1():
    print("发表评论")


# 示例:

def decorator_time(func_out):
    def inner():
        # time()统计1970/01/01 00:00:01 到现在的时间
        begin = time.time()
        func_out()
        end = time.time()
        result = end - begin
        print("函数执行时间: ", result)

    return inner()


@decorator_time
def func():
    for i in range(10000):
        print(i)
