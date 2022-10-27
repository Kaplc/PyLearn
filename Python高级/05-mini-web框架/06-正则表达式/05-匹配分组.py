"""
"|":	    匹配左右任意一个表达式
"(ab)":	    将括号中字符作为一个分组
"\num":	        引用分组num匹配到的字符串
"(?P<name>)":	分组起别名
"(?P=name)":	引用别名为name分组匹配到的字符串

# "."在正则表达式属于匹配任意一个字符, 加\转换成真正的字符
# 分组:默认是1一个分组，多个分组从左到右依次加1
        print(match_obj.group(1))
"""

import re


# "|": 匹配左右任意一个表达式
def example():
    # 水果列表
    fruit_list = ["apple", "banana", "orange", "pear"]

    # 遍历数据
    for value in fruit_list:
        # |    匹配左右任意一个表达式
        match_obj = re.match("apple|pear", value)
        if match_obj:
            print("%s是我想要的" % match_obj.group())
        else:
            print("%s不是我要的" % value)


#   "apple", "pear"
#   "banana", "orange"


# "(ab)": 将括号中字符作为一个分组
def ex2():
    # "."在正则表达式属于匹配任意一个字符, 加\转换成真正的字符
    match_obj = re.match("[a-zA-Z0-9_]{4,20}@(163|126|qq|sina|yahoo)\.com", "hello@163.com")
    if match_obj:
        print(match_obj.group())
        # 获取分组数据
        print(match_obj.group(1))
    else:
        print("匹配失败")

    #   hello@163.com
    match_obj = re.match("(qq):([1-9]\d{4,10})", "qq:10567")

    if match_obj:
        print(match_obj.group())
        # 分组:默认是1一个分组，多个分组从左到右依次加1
        print(match_obj.group(1))
        # 提取第二个分组数据
        print(match_obj.group(2))
    else:
        print("匹配失败")

    #   qq:10567, qq, 10567


# "\num": 引用分组num匹配到的字符串 \\1
def ex3():
    match_obj = re.match("<[a-zA-Z1-6]+>.*</[a-zA-Z1-6]+>", "<html>hh</div>")

    if match_obj:
        print(match_obj.group())
    else:
        print("匹配失败")

    match_obj = re.match("<([a-zA-Z1-6]+)>.*</\\1>", "<html>hh</html>")

    if match_obj:
        print(match_obj.group())
    else:
        print("匹配失败")


#     <html>hh</div>

    match_obj = re.match("<([a-zA-Z1-6]+)><([a-zA-Z1-6]+)>.*</\\2></\\1>", "<html><h1>www.itcast.cn</h1></html>")

    if match_obj:
        print(match_obj.group())
    else:
        print("匹配失败")


# "(?P<别名>)":	分组起别名
# "(?P=别名)":	引用别名为name分组匹配到的字符串

def ex4():
    match_obj = re.match("<(?P<name1>[a-zA-Z1-6]+)><(?P<name2>[a-zA-Z1-6]+)>.*</(?P=name2)></(?P=name1)>",
                         "<html><h1>www.itcast.cn</h1></html>")

    if match_obj:
        print(match_obj.group())
    else:
        print("匹配失败")


# 1h

if __name__ == '__main__':
    example()
    ex2()
    ex3()
    ex4()
