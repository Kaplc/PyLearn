"""
生成器简介:   根据程序员制定的规则循环生成数据，当条件不成立时则生成数据结束。
            数据不是一次性全部生成处理，而是使用一个，再生成一个，可以节约大量的内存。

"""

# 与列表推导式类似，生成器推导式使用小括号

# 创建生成器
my_generator = (i * 2 for i in range(5))  # 0, 2, 4, 6, 8
print(my_generator)


# 每次执行next()获取生成器下一值
def result():
    value = next(my_generator)
    print(value)


# yield关键字的生成器: 是一个可迭代对象
def generator_y():
    for i in range(6):
        print('开始生成...')
        # 说明: 代码执行到 yield 会暂停，然后把结果返回出去，下次启动生成器会在暂停的位置继续往下执行
        print("暂停前")
        yield i
        print("暂停后")
        print('完成一次...')


# 案例: 生成斐波那契数列
def fbnc(count):
    a = 0
    b = 1
    k = 3
    if count == 1:
        return "第", count, "个: ", a
    elif count == 2:
        print("下一个")
        return "第", count, "个: ", b
    else:
        print("第 1 个:  0")
        print("下一个")
        print("第 2 个:  1")
        print("下一个")
        for i in range(1, count - 1):
            a, b = b, a + b
            data = b
            print("第", k, "个: ", data)
            yield "下一个"
            k += 1


if __name__ == '__main__':
    # for i in my_generator:
    #     print(i)
    #
    # # 单次调用
    # y = generator_y()
    # print(next(y))
    # print(next(y))
    #
    # # 遍历调用
    # for i in generator_y():
    #     print(i)
    #
    # 斐波那契生成
    for i in fbnc(10):
        print(i)

