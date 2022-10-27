"""
正则表达式: 匹配字符串时代码的书写规则

re模块: 使用正则表达式需要使用的模块

"""

import re

# result = re.match(正则表达式, 要匹配的字符串)
result = re.match("abc", "abcdef")

# 如果上一步提取到数据使用group方法提取数据
info = result.group()
print(info)
