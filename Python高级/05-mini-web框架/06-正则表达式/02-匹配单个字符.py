"""
匹配单字符:
    "." : 匹配任意1个字符（除了\n）
    "[]": 匹配[ ]中列举的字符
    "\d": 匹配数字，即0-9
    "\D": 匹配非数字，即不是数字
    "\s": 匹配空白，即 空格，tab键
    "\S": 匹配非空白
    "\w": 匹配非特殊字符，即a-z、A-Z、0-9、_、汉字
    "\W": 匹配特殊字符，即非字母、非数字、非汉字

"""

import re


# ".": 匹配任意1个字符（除了\n）
def example():
    ret = re.match(".", "M")
    print(ret.group())

    ret = re.match("t.o", "too")
    print(ret.group())

    ret = re.match("t.o", "two")
    print(ret.group())


# "[]": 匹配[]中列举的字符, 其中取一个
def ex2():
    # 如果hello的首字符小写，那么正则表达式需要小写的h
    ret = re.match("h", "hello Python")
    print(ret.group())

    # 如果hello的首字符大写，那么正则表达式需要大写的H
    ret = re.match("H", "Hello Python")
    print(ret.group())

    # 大小写h都可以的情况(不需要加逗号)
    ret = re.match("[hH]", "hello Python")
    print(ret.group())
    ret = re.match("[hH]", "Hello Python")
    print(ret.group())
    ret = re.match("[hH]ello Python", "Hello Python")
    print(ret.group())

    # 匹配0到9第一种写法
    ret = re.match("[0123456789]Hello Python", "7Hello Python")
    print(ret.group())

    # 匹配0到9第二种写法
    # [0-9]等价\d
    ret = re.match("[0-9]Hello Python", "7Hello Python")
    print(ret.group())

    ret = re.match("[0-35-9]Hello Python", "3Hello Python")
    print(ret.group())

    # 下面这个正则不能够匹配到数字4，因此ret为None
    ret = re.match("[0-35-9]Hello Python", "4Hello Python")
    print(ret.group())


# "\d": 0-9
def ex3():
    # 普通的匹配方式
    ret = re.match("嫦娥1号", "嫦娥1号发射成功")
    print(ret.group())

    ret = re.match("嫦娥2号", "嫦娥2号发射成功")
    print(ret.group())

    ret = re.match("嫦娥3号", "嫦娥3号发射成功")
    print(ret.group())

    # 使用\d进行匹配
    ret = re.match("嫦娥\d号", "嫦娥1号发射成功")
    print(ret.group())

    ret = re.match("嫦娥\d号", "嫦娥2号发射成功")
    print(ret.group())

    ret = re.match("嫦娥\d号", "嫦娥3号发射成功")
    print(ret.group())


# "\D": 非数字
def ex4():
    # match_obj = re.match("\D", "f")
    match_obj = re.match("\D", "5")
    if match_obj:
        # 获取匹配结果
        print(match_obj.group())
    else:
        print("匹配失败")


# "\s": 匹配空白，即 空格，tab键
def ex5():
    # 空格属于空白字符
    match_obj = re.match("hello\sworld", "hello world")
    if match_obj:
        result = match_obj.group()
        print(result)
    else:
        print("匹配失败")

    # \t 是tab键 属于空白字符
    match_obj = re.match("hello\sworld", "hello\tworld")
    if match_obj:
        result = match_obj.group()
        print(result)
    else:
        print("匹配失败")


# "\S": 匹配非空白
def ex6():
    match_obj = re.match("hello\Sworld", "hello&world")
    if match_obj:
        result = match_obj.group()
        print(result)
    else:
        print("匹配失败")

    match_obj = re.match("hello\Sworld", "hello world")
    if match_obj:
        result = match_obj.group()
        print(result)
    else:
        print("匹配失败")


# "\w": 匹配非特殊字符，即a-z、A-Z、0-9、_、汉字
def ex7():
    # 匹配非特殊字符中的一位
    match_obj = re.match("\w", "A")
    match_obj = re.match("\w", "%")
    if match_obj:
        # 获取匹配结果
        print(match_obj.group())
    else:
        print("匹配失败")


# "\W": 匹配特殊字符，即非字母、非数字、非汉字, 非下划线
def ex8():
    # 匹配特殊字符中的一位
    match_obj = re.match("\W", "&")
    match_obj = re.match("\W", "A")
    if match_obj:
        # 获取匹配结果
        print(match_obj.group())
    else:
        print("匹配失败")


if __name__ == '__main__':
    # example()
    # ex2()
    # ex3()
    # ex4()
    # ex5()
    # ex6()
    # ex7()
    ex8()
