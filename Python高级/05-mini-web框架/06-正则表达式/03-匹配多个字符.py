"""
"*":	匹配前一个字符出现0次或者无限次，即可有可无
"+":	匹配前一个字符出现1次或者无限次，即至少有1次
"?":	匹配前一个字符出现1次或者0次，即要么有1次，要么没有
"{m}":	匹配前一个字符出现m次
"{m,n}":匹配前一个字符出现从m到n次

"""

import re


# "*": 匹配前 "一个字符" 出现0次或者无限次，即可有可无[0, +∞)
def example():
    ret = re.match("[A-Z][a-z]*", "M")
    print(ret.group())

    ret = re.match("[A-Z][a-z]*", "MnnM")
    print(ret.group())

    ret = re.match("[A-Z][a-z]*", "Aabcdef")
    print(ret.group())


#   M none, Mnn, Aabcdef


# "+":	匹配前一个字符出现1次或者无限次，即至少有1次[1, +∞)
def ex2():
    match_obj = re.match("t.+o", "two")
    if match_obj:
        print(match_obj.group())
    else:
        print("匹配失败")


#   two

# "?":	匹配前一个字符出现1次或者0次，即要么有1次，要么没有
def ex3():
    match_obj = re.match("https?", "http")
    if match_obj:
        print(match_obj.group())
    else:
        print("匹配失败")


#     http

# "{m}":	匹配前一个字符出现m次
# "{m,n}":匹配前一个字符出现从m到n次
def ex4():
    ret = re.match("[a-zA-Z0-9_]{6}", "12a3g45678")
    print(ret.group())

    ret = re.match("[a-zA-Z0-9_]{8,20}", "1ad12f23s34455ff66")
    print(ret.group())

    ret = re.match(r".*\d+.*", "aaaaa45455dadadad")
    print(ret)


# 12a3g4, 1ad12f23s34455ff66

if __name__ == '__main__':
    example()
    ex2()
    ex3()
    ex4()
