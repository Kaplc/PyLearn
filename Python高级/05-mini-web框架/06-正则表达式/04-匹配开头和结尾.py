"""
"^": 匹配字符串开头后一个字符
"$": 匹配字符串结尾前一个字符

"""
import re


# "^": 匹配字符串开头
def example():
    # 匹配以数字开头的数据
    match_obj = re.match("^\d.*", "3hello")  # 以数字开头的所有字符串
    if match_obj:
        # 获取匹配结果
        print(match_obj.group())
    else:
        print("匹配失败")


#   "3hello"


# "$": 匹配字符串结尾
def ex2():
    # 匹配以数字结尾的数据
    match_obj = re.match(".*\d$", "hello5")  # 以数字结尾的所有字符串
    if match_obj:
        # 获取匹配结果
        print(match_obj.group())
    else:
        print("匹配失败")


#   hello5

# 以数字结尾和开头的所有字符串
def ex3():
    match_obj = re.match("^\d.*\d$", "4hello4")
    if match_obj:
        # 获取匹配结果
        print(match_obj.group())
    else:
        print("匹配失败")


#     "4hello4"

# [^指定字符]: 表示除了指定字符都匹配
# 该一个字符除了aeiou的字符都匹配

def ex4():
    match_obj = re.match("1[^aeiou]", "1h")
    if match_obj:
        # 获取匹配结果
        print(match_obj.group())
    else:
        print("匹配失败")


# 1h

if __name__ == '__main__':
    example()
    ex2()
    ex3()
    ex4()
