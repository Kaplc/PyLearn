# print函数的格式化输出
'''age = 20
print(age)
print(f'我今年是{age}岁')'''

# input输入函数
'''a = input()
b = input('b = '  )
c = a + b
print(f'c = a + b = {c}')'''

# 数据类型转换

'''a = 1
b = 1.0
c = '100'
print()
print(f'a是{type(a)}类型')
print(f'b是{type(b)}类型')
print(f'c是{type(c)}类型')'''

'''c = int(c)#把c从str（字符串类型）转化成int（整数类型）
print(f'1.c是{type(c)}类型')
c = float(c)
print(f'2.c是{type(c)}类型')
c = str(c)
print(f'3.c是{type(c)}类型')'''

# 运算符

'''
算数运算符
+-*/ 加减乘除
// 除法取商
% 除法取余数
** 指数
优先级:() > ** > * / % // > + -
'''
'''a = 10
b = 3
print(f'c = a / b = {a / b}')
print(f'c = a // b = {a // b}') # 取商
print(f'c = a % b = {a % b}') # 取余
print(f'c = a ** b = {a ** b}') # 指数

c = (1 + 1) ** 2 * 10 - 1'''

# 赋值运算符
# =


# 复合赋值运算符
# +=
# -=
# *=
# /=

'''a = 2
a += 1 # a = a + 1

print(f'a = {a}')


a -= 1 # a = a -1
print(f'a = {a}')

b = 4
b += 3*2 #先右边正常计算再复合赋值运算：b += 6 ---> b = b + 6
print(f'b = {b}')'''

# 比较运算符
# ==
# >=
# <=
# !=
# 比较正确的值是true，错误false

'''a = 1
b = 2
c = 2
print(f'a == b 是 {a == b}')
print(f'b == c 是 {b == c}')
print(f'a >= b 是 {a >= b}')
print(f'a <= b 是 {a <= b}')
print(f'a != b 是 {a != b}')'''

# 逻辑运算符
# 与 and 两边都真才真，其余都假
# 或 or  两边假才假，其余都真
# 非 not 真假互换

'''a = 1
b = 2
c = 2
print(f'a == b(0) and b == c（1） 是 {a == b and b == c}')
print(f'a <= b(1) and b == c(1) 是 {a <= b and b == c}')
print(f'a == b(0) and b == c(1) 是 {a == b or b == c}')
print(f'a == b(0) and a >= b(0) 是 {a == b or a >= b}')
print(f'a != b 是 {not a != b}')'''

'''
if语句

1个功能：
执行满足条件的语句
+++++++++++++++++++++++++++++++++++++++++++++++++
3种用法：

if 条件:
    这里是条件成立要执行的代码，记得要缩进一个TAB键
else
    条件不成立要执行的表达式或者叫代码

（中文意思如果...否则...）

---------------------------

if...
elif...
else

（如果...如果...否则...）

------------------------------------------
if嵌套（如果里面还有如果，判断两次及以上）
if 条件:
    条件成立要执行的代码
    if 条件：
        条件成立要执行的代码

+++++++++++++++++++++++++++++++++++++++++++++++++
1种简写：
三目运算符：
条件成立要执行的表达式/代码 if 条件 else 条件不成立要执行的表达式/代码

'''

# if 条件:
#     这里是条件成立要执行的代码，记得要缩进一个TAB键
# else
#     条件不成立要执行的表达式或者叫代码
#
# （中文意思如果...否则...）
# a = 3
# b = 2
#
# if a < b:
#     print('a < b喔')
# else:
#     print('a > b 或者 a = b喔')

# c = 3
#
# if a < b:
#     print('a < b喔')
# elif a == b:
#     print('a = b喔')
# elif a == c:
#     print('a = b喔')
# else:
#     print('a > b ')

# print('a > b') if a > b else print('a <= b')
# 条件成立要执行的表达式/代码 if 条件 else 条件不成立要执行的表达式/代码

#
# a1 = input('a = ')
# a = int(a1)
# b = int(input('b = '))
# c = int(input('c = '))
# _max = 0
# if a > b:
#     if a > c:
#         _max = a
#     elif a == c:
#         _max = a
#     else:
#         _max = c
# elif a == b:
#     if a > c:
#         _max = a
#     elif a == c:
#         _max = a
#     else:
#         _max = c
# else: #a < b
#     if b > c:
#         _max = b
#     elif b == c:
#         _max = b
#     else:
#         _max = c
# print(f'最大值是{_max}')

'''
while循环和for循环
'''
'''

===========================
语法： =====================
===========================

while 条件:
    条件成立执行的代码
    
(while循环什么时候结束？条件不符合就结束）
------------------------------------------
 
for 临时变量 in 序列（字符串，表格之类...)
    循环时要执行的代码
    
(for循环什么时候结束？序列遍历完就结束）
    
------------------------------------------
while 条件:
    条件成立执行的代码

else:
    循环正常结束后要执行的代码
------------------------------------------    
    
for 临时变量 in 序列（字符串，表格之类...)
    循环时要执行的代码
else:
    循环正常结束后要执行的代码

==========================
2个退出循环代码：============
==========================

continue 1.退出本次循环然后从循环头开始执行 2.while/for... else ...的else后面代码要执行（跳过本次循环,正常结束）
break 1.退出所有循环 2.while/for... else ...的else后面代码不执行（强行打断循环直接结束整个循环，非正常结束）


==================
循环嵌套===========
==================

while 条件:
    条件成立执行的代码
    while 条件:
        条件成立执行的代码
-----------------------------------------------
for 临时变量 in 序列（字符串，表格之类...)
    循环时要执行的代码
    for 临时变量 in 序列（字符串，表格之类...)
        循环时要执行的代码
'''
# a = 1
# print()
# while a <= 10: #我要打印1~10的数字
#     print(a)
#     a += 1

'''
for 临时变量 in 序列（字符串，表格之类...)
    循环时要执行的代码
'''
# k = 0
# x = 0
# str1 = '慕容猪是个'
# for i in str1:
#     k += 1
#     if i == '猪':
#         x = 1
#
# if x == 1:
#     print(f'已经找到‘猪’这个字，在字符串‘{str1}’的第{k}位')
# else:
#     print('抱歉没有找到‘猪’这个字')


# a = 1
# while a <= 10: #我要打印 1~10 的数字且不想打印 5 这个数字
#     print(f'第{a}次循环的头')
#     if a == 5:
#         a += 1
#         continue;
#     print(a)
#     print(f'第{a}次循环的尾')
#     a += 1

# a = 1
# while a <= 10:  # 我本来想要打印 1~10 的数字且不想打印 5 及后面的数字
#     print(f'第{a}次循环的头')
#     if a == 5:
#         a += 1
#         continue;
#     print(a)
#     print(f'第{a}次循环的尾')
#     a += 1
# else:
#     print('经过了else')
# print('结束')

# k = 1
# x = 0
# str1 = '慕容猪是个'
# for i in str1:
#     if i == '猪':
#
#         x = 1
#         break
#
#     k += 1
# if x == 1:
#     print(f'在字符串‘{str1}’的第{k}位已经   找到  ‘猪’这个字，')
# else:
#     print(f'抱歉在字符串‘{str1}’的第{k}位   没有  找到‘猪’这个字')
#
# print(f'在字符串‘{str1}’的第{k}位已经   找到  ‘猪’这个字，') if x == 1 else print(f'抱歉在字符串‘{str1}’的第{k}位   没有  找到‘猪’这个字')

# x = y = 1
# print()
# while x <= 5:
#     y = 1
#     while y <= 5:
#         y += 1
#         print('*  ', end='')
#     x += 1
#     print()

'''

*            i = 1 j = 1
* *          i = 2 j = 1 /  i = 2 j = 2
* * *        i = 3 j = 1 /  i = 3 j = 2 /  i = 3 j = 3
* * * *      i = 4 j = 1 /  i = 4 j = 2 /  i = 4 j = 3 /  i = 4 j = 4 
* * * * *    i = 5 j = 1 /  i = 5 j = 2 /  i = 5 j = 3 /  i = 5 j = 4 / i = 5 j = 5
i是行，j是列

# i = j = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print('* ', end = '')
#         j += 1
#     print('', end = '\n')
#     i += 1
'''

'''

字符串
'''
'''
============
下标   ======
============

变量1 = 变量2[下标数字]
含义：提取变量2中第 下标数字 位的字符
下标数字从零开始

'''
# str1 = '123456789'
# print(str1[0])
# print(str1[8])

'''
============
切片   ======
============

变量1 = 序列名[开始位置下标数字：结束位置下标数字：步长]
提取范围：半开半闭区间 [ 开始,结束 ) 相当于[1,4）取123
步长含义：提取的间隔，负数为从右往左


'''

# a = '123456789'
#
# print(a[2:5:1])
# print(a[2:8:3])
# print(a[5:2:-1])


'''
==================
字符串查找   ======
==================

find()查找函数

语法：

字符串序列.find(子串， 开始下标，结束下标)

作用：如果找到子串则返回子串开始的下标，否则返回-1
注意事项:如果下标省略表示整个序列查找
-------------------------------------------------

index()查找函数

语法：

字符串序列.index(子串， 开始下标，结束下标)

作用：如果找到子串则返回子串开始的下标，否则报错
注意事项:如果下标省略表示整个序列查找
------------------------------------------

rfind()
从右开始查找
rindex()
从右开始查找

------------------------------

count()
语法：

字符串序列.count(子串， 开始下标，结束下标)

作用：返回找到的个数，没找到就是0
注意事项:如果下标省略表示整个序列查找

'''

# str1 = '987654321'
# a = '1'
# print(str1.find('1', 0, 4))
# print(str1.find(a, 0, 4))
# n = str1.find(a)
# print(n)

# #
# print(str1.index(a, 3, 4))
# print(str1.rfind(a, 3, 9))
# print(str1.rindex(a, 3, 9))

# b = '123 123 123 123'
# print(b.count(a))

'''
==================
字符串修改   ======
==================

'''
# replace()字符串修改函数
# 序列.replace(旧子串，新子串，替换次数)  新的替换旧的然后新的字符串做返回值

# old = '123 123 123 123'
# new = old.replace('1', '2', 2)
# print(new)
# print(old)

#
# # split()分割函数
# # 序列.split(分割字符，分割次数)     如果找到子串则返回子串开始的下标，否则返回-1
# # 注意事项:如果下标省略表示整个序列查找

# list1 = old.split('2', 3)
# print(list1)


#
# # join()分割函数
# # 链接的子串.join(列表)  合并列表里面的字符串
# a = ['幕', '容', '是', '猪']
# new1 = '...'.join(a)
# print(new1)

#
#
#
# str1 = 'Hello World'
# str2 = 'hello world'
# #
# # 字符串序列.capitalize()  字符串首字母大写
# new2 = str2.capitalize()
# print(new2)
# #
# # 字符串序列.title()  字符串中每个单词首字母大写
# new3 = str2.title()
# print(new3)
#
# # 字符串序列.upper()  字符串所有字母小写转大写
# print(str1.upper())
#
# # 字符串序列.lower()  字符串所有字母大写转小写
# print(str1.lower())
#
#
#
#
# str3 = '    123   123    '
#
# # 字符串序列.lstrip()  删除字符串左边的空格
# print(str3.lstrip())
#
# # 字符串序列.rstrip()  删除字符串右边的空格
# print(str3.rstrip())
#
# # 字符串序列.strip()  删除字符串两边的空格
# print(str3.strip())

'''
字符串对齐
'''

# str1 = '123'
#
# # 字符串序列.ljust(对齐后字符串总长度，填充长度的字符串)  把字符串左对齐并填充长度，不填填充字符默认空格
# print(str1.ljust(10))
# print(str1.ljust(10, '.'))
#
# # 字符串序列.rjust(对齐后字符串总长度，填充长度的字符串)  把字符串右对齐并填充长度，不填填充字符默认空格
# print(str1.rjust(10))
# print(str1.rjust(10, '.'))
#
# # 字符串序列.center(对齐后字符串总长度，填充长度的字符串)  把字符串居中对齐并填充长度，不填填充字符默认空格
# print(str1.center(10))
# print(str1.center(10, '.'))
#
# '''
# 判断字符串
# '''
# str1 = '12354684654'
# # 字符串序列.startswith( 子串， 开始下标， 结束下标）   判断字符串是否以该子串开头，正确返回True,否则返回False
#
# print(str1.startswith('123'))
# print(str1.startswith('122'))
# # 字符串序列.endsswith( 子串， 开始下标， 结束下标）   判断字符串是否以该子串结尾，正确返回True,否则返回False
# print(str1.endswith('654'))
#
# # isalpha() 判断非空字符串中，只包含字母，返回true或者false
# # isdigit() 判断非空字符串中，只包含数字
# # isalnum() 判断非空字符串中，只包含字母和数字
# # isspace()  判断非空字符串中，只包含空格
#
# print(str1.isalpha())
# print('abc abc'.isalnum())
# print(str1.isdigit())
# print('123abc'.isalnum())
# print('   '.isspace())
#

'''
列表  

'''

'''
想要一个变量存多个数据就用列表
变量 = [数据1, 数据2, 数据3,  ....]

数据类型可以不同，但是为了方便管理尽量相同

'''

'''
下标
'''

# list1 = ['幕', '容', '是', '个', '猪']
# print(list1)
# print(list1[0])
# print(list1[3])
#
'''
查找
index()
count()
len() 查看有多少个数据

in
查找数据在序列里面
语法：要查找的数据 in 列表序列
在返回true否则false

not in
判断序列不在里面
语法：要查找的数据 in 列表序列
不在返回true否则false
'''
# list1 = ['幕', '容', '是', '个', '猪']
# print(list1.index('猪'))
# print(list1.index('小'))
# print(list1.index('猪', 0, 3))

# print(list1.count('猪'))
#
# print(len(list1))
#
# print('猪' in list1)
# print('1' in list1)
# print('猪'not in list1)
# print('1' not in list1)

'''
列表添加数据
'''
'''
append()
在目标列表中往后添加数据
列表序列.append（数据）

extend()
在目标列表中往后添加拆解后数据
列表序列.extend()

insert()
往列表目标位置添加数据
列表序列.insert(位置下标，数据)
'''
# list1 = ['幕', '容', '是', '个', '猪']
# list1.append('吗')
# print(list1)
#
# list1.append([1, 2, [1, [1, [1, [1]]]]])
# print(list1)
#
# list2 = ['幕', '容', '是', '个', '猪']
# list2.extend('吗？')
# print(list2)
#
# list2 = ['幕', '容', '是', '个', '猪']
# list2.extend(['吗？', 1, '123'])
# print(list2)
#
# list2 = ['幕', '容', '是', '个', '猪']
# list2.insert(2, '就')
# print(list2)

'''
列表删除数据

'''

'''
del 目标             #删除目标 可以删除单个目标也可以删除整个序列

列表序列.pop(下标)    #删除指定下标的数据（不指定默认删除最后一个），并返回被删掉的数据

列表序列.remove(数据) #删除第一个匹配的数据

列表序列.clear（）    #清空列表

'''

# list1 = ['a', 'b', 'c', 'd']

# del list1
# print(list1)

# list1 = ['a', 'b', 'c', 'd']
# del list1[1]
# print(list1)

######################

# list1 = ['a', 'b', 'c', 'd']
# print(list1.pop())
# print(list1)
# list1 = ['a', 'b', 'c', 'd']
# print(list1.pop(2))
# print(list1)

###########################
#
# list1 = ['a', 'b', 'a', 'd']
# list1.remove('a')
# print(list1)
#
# #########################
# list1.clear()
# print(list1)

'''
列表修改数据

'''
'''
列表序列[下标] = '数据'                   #直接修改

列表序列.reverse()                      #逆置 

列表序列.sort(None, reverse = False)    #升序和降序 第二个参数false（默认）升序，true降序

'''

# list1 = ['a', 'b', 'c', 'd']
# list1[1] = 'a'
# print(list1)
###################################

# list1 = ['a', 'b', 'c', 'd']
# list1.reverse()
# print(list1)

# #######################################

# list2 = [4, 3, 2, 7, 6]
# list2.sort()
# print(list2)
#
# list2 = [4, 3, 2, 7, 6]
# list2.sort(reverse=False)
# print(list2)
#
# list2 = [4, 3, 2, 7, 6]
# list2.sort(reverse=True)
# print(list2)

'''
列表复制数据
'''

# a = [1, 2, 3]
#
# b = a.copy()
#
# print(b)

'''
列表遍历
'''

##############
# a = [7, 2, 3, 4, 5, 6, '123']
# #
# k = 0
# while k < len(a):
#     print(a[k])
#     k += 1


##############
# for i in a:
#     print(i)

'''
结论：遍历最好用for
'''

'''
列表嵌套
'''

# a = [[1, 2, 3, 4, 5], 2, [3, 2, 3, 4, [5, 6, '慕容是我老婆']], 4, 5]
# print(a[2][4][2])

'''
元组
'''
'''
和列表用法几乎一样，只是个不能修改数据的列表,并且把中括号改成小括号

'''
# a = [1, 2, 3, 4, 1]
# a[0] = 2
# print(a)
# b = (10)
# print(b)
# b = (10,)
# print(b)
# '''
# 元组的查找
#
# index()
# count()
# len()
# 和列表一样
# '''
#
# # a.index(1)
#
# # print(a.count(1))
# # print(len(a))


'''
字典
'''
# 关键字-数值 （键值对）
# a = ['慕容', '是个猪']
# b = {'name': '慕容', 8: '是个猪'}
# print(a[0])
# print(b['name'])
# print(b[8])
'''
增加和修改
'''

# b = {'name': '慕容', 'what': '是个猪'}
# b['name'] = '小慕容'
# print(b)
# b['names'] = '傻妍'
# print(b)

'''
删除

del 目标    删除字典/删除键值对，key不存在则报错
clear()   清空字典

'''
# del 目标    删除字典/删除键值对，key不存在则报错

# b = {'name': '慕容', 'what': '是个猪'}
# del b
# b.clear()
# print(b)

# b = {'name': '慕容', 'what': '是个猪'}
# del b['name']
# print(b)

##################

# clear()   清空字典

# b = {'name': '慕容', 'what': '是个猪'}
# b.clear()
# print(b)


'''
查找

key值查找     找到就返回该值，否则报错
get()        参数1填key，找到就返回值，否则返回第二个参数。如果省略第二个参数默认返回None
keys()       返回由key（关键字）组成的可迭代序列
values()     返回由values（数值）组成的可迭代序列
items()      返回由items(键值对)组成的可迭代序列
'''

# key值查找    找到就返回该值，否则报错

# a = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# print(a['b'])
# print(a['e'])

# 字典序列.get( 参数1 , 参数2)
# 参数1填key，找到就返回值，否则返回第二个参数。如果省略第二个参数默认返回None

# a = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# print(a.get('c'))
#
# print(a.get('e'))
# print(a.get('e', '找不到喔'))

# 字典序列.keys()   返回由key（关键字）组成的可迭代序列

# a = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# print(a.keys())
#
# # values()     返回由values（数值）组成的可迭代序列
#
# a = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# print(a.values())
#
# # items()      返回由items(键值对)组成的可迭代序列
#
# a = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# print(a.items())

'''
遍历
'''

# a = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# for key in a.keys():
#     print(key)
#
# for values in a.values():
#     print(values)
#
# for items in a.items():
#     print(items)
#
# # print(a.items[0])
# # 拆包键值对
#
# for key1000, values1 in a.items():
#     print(f'{key1000} = {values1}')


'''
集合

数据去重功能
数据无序排列，不能用下标查找数据
'''

# a = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
# print(a)

'''
增加

add()        追加单个数据，错误使用会报错
update()     追加的数据是序列，错误使用会报错
'''

# a.add(10)
# print(a)
#
# a.update([10,20,30])
# print(a)
# a.add([90,100])
# a.update(100)

'''
删除

remove()    删除集合中指定数据，没有这个数据会报错
discard()   删除集合中指定数据，没有这个数据也不会报错
'''

# a = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
# a.remove(1)
# print(a)
# a.remove(6)
# a.discard(1)
# print(a)
# a.discard(6)

'''
查找

in      判断数据是否在集合里面，在返回true否则false
not in  刚好相反
'''

# a = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
# print(1 in a)
# print(1 not in a)
# print(6 in a)


'''
公用函数

+           合并（字符串，列表，元组）
*           复制（字符串，列表，元组）
in          判断在（字符串，列表，元组，字典，集合）
not in      判断不在（字符串，列表，元组，字典，集合）
len()       获取序列数据个数
del         删除目标
max         获取序列中数据最大值
min         获取序列中数据最小值
range()     自动生成指定范围内的可迭代序列---->配合for来使用
enumrate()  把可遍历序列自动结合生成（下标，数据）这种元组的可迭代序列---->配合for
list()      把原序列转换成列表
tuple()     把原序列转换成元组
set()       把原序列转换成集合

'''
# + 和 *
# str1 = '123'
# str2 = '456'
# list1 = [1, 2, 3]
# list2 = [7, 8, 9]
# print(int(str1) + int(str2))
# print(list1 + list2)
# print(str1 * 3)
# print(list2 * 3)

# ===============================

# max 和 min
# str3 = 'abcdefg'
# print(max(str3))
# print(min(str3))
# print(max(list1))
# print(min(list2))

# ==============================

# range(开始， 结尾 ，步长）
# for c in range(10):
#     print(c)
# for a in range(1, 10, 1):
#     print(a)
# for b in range(0, 9, 2):
#     print(b)

# ==============================

# enumerate(可遍历对象， start = 0)

# for c in enumerate(str3, start=0):
#     print(c)

# for d in enumerate(str3):
#     print(d)

# for e in enumerate(str3, start=1):
#     print(e)

# =============================

# print(list(str1))
# print(tuple(str1))
# print(set(str1))


'''
推导式

解释:定义有规律的序列的简写
1.合并两个列表为字典
(使用范围列表 元组 集合)
'''
# 创建数据1~10的列表
# 常规方法
# list1 = []
# a = 1
# while a <= 10:
#     list1.append(a)
#     a += 1
# print(list1)
#
# list2 = []
# for b in range(1, 11):
#     list2.append(b)
# print(list2)


# # 推导式
#
# list3 = [c for c in range(1, 11)]
# print(list3)
# =============================================

# 推导式+if
## 创建0~10的偶数列表
# list1 = []
# a = 0
# while a <= 10:
#     if a % 2 == 0:
#         list1.append(a)
#     a += 1
# print(list1)
# #
# list3 = [c for c in range(0, 11, 2)]
# print(list3)
# list4 = [d for d in range(0, 11) if d % 2 == 0]
# print(list4)

#  =========================
# 推导式循环嵌套

# for a in range(1,4):
#     for b in range(1, 5):
#         print(a, b)
#
# list1 = [(x, y) for x in range(1, 4) for y in range(1, 5)]
# print(list1)

# =====================
# 字典推导式

# dict1 = {i : i ** 2 for i in range(1, 6)}
# print(dict1)

# =====================
# 和并两个列表为字典
# list1 = [a for a in range(1,6)]
# list2 = [b ** 2 for b in range(1, 7)]
# dict1 = {list1[i] : list2[i] for i in range(0, len(list1))}
# print(dict1)

# ====================
# 提取字典目标数据


# dict1 = {'a': 100, 'b':200, 'c':300, 'd':400, 'e':500}
#
# for key1,values1 in dict1.items():
#     print(key1,values1)
#
# dict2 = {key1:values1 for key1,values1 in dict1.items() if values1 > 300}
# print(dict2)


'''

(11)
(12 22) 
(13 23 33)
(14 24 34 44)
(15 25 35 45 55)
(16 26 36 46 56 66) 
(17 27 37 47 57 67 77)
(18 28 38 48 58 68 78 88)
(19 29 39 49 59 69 79 89 99)

xy

'''

# list1 = [(y,x) for x in range(1, 10) for y in range(1, 10) if y <= x]
# # for a,b in list1:
# #     # print(f'{a}*{b} ',end='')
# #     if a == b:
# #         print()
# # print(list1)
# list3 = []
# for x in range(1, 10):
#     for y in range(1, 10):
#         if y <= x:
#             list3.append((x, y))
#
# x = y = 1
# list2 =[]
# while y < 10:
#     while x <= y:
#         # print(f'{x}*{y} ',end='')
#         list2.append((x,y))
#         # if x == y:
#         #     print()
#         x += 1
#     x = 1
#     y += 1
# print(list2)

# list1 = [(y,x) for x in range(1,10) for y in range(1,10)]
# for a,b in list1:
#     if a <= b:
#         print(f'{a}{b}, ', end='')


'''
函数1

1.函数定义和调用
2.函数参数传递
3.函数返回值
4.函数嵌套
5.函数说明文档
'''

'''
定义和调用
'''

# 函数定义  def 函数名(参数)：

# def print_name():
#     print()
#     print('我的名字是',end='')
#     print()
#
# a = input('请输入姓名:')
# # 函数调用
# print_name()
# print(a)

# =========================

# 函数的参数和返回值
'''
实参：调用函数时输入的参数
形参：接收传进来的参数（定义参数时使用的参数）
'''

# def num_add(a,b):
#     c = a + b
#     return c
# a1 = int(input('a:'))
# b1 = int(input('b:'))
# c1 = num_add(a1,b1)
# print(f'{a1} + {b1} = {c1}')
#
# print(num_add(int(input('a:')), int(input('b:'))))


# ===========================

# 函数嵌套

# def num_add(a,b,c):
#     ''' 三个数求和'''
#     return a + b + c
#
# def num_average(a,b,c):
#     '''
#     三个数求平均值
#     :param a: 加数1
#     :param b: 加数2
#     :param c: 加数3
#     :return: 返回平均值
#     '''
#     sum = num_add(a,b,c)
#     return sum / 3
#
# help(num_average)

# def num_add(a,b,c):
#     return a + b + c
#
# def num_average(a,b,c):
#     return num_add(a,b,c) / 3

# print(num_average(int(input('a:')),int(input('b:')),int(input('c:'))))

# ================================

# 函数说明文档

# def a():
#     '''
#     :return:
#     '''
#
# help(a)
#
# def b(a,b):
#     '''
#     535
#     :param a: dasd
#     :param b: awd
#     :return: asdadawdaf
#     '''
#
# help(b)

'''
函数2

1.局部变量和全局变量及修改
2.函数单和多返回值传递
3.函数的位置参数,关键字参数,默认参数
4.不定长参数位置参数和关键字参数
5.元组字典的拆包
6.交换变量
'''

# a = 100
#
# def b():
#     a = 200
#     c = 300
#     print(a)
#
# b()
# print(a)
# # print(c)
#
# def aa():
#     global a
#     a = 200
# aa()
# print(a)

# =============================
# 函数单和多返回值传递
# 单返回值
# def f1():
#     return 10
# def f2(p):
#     print(p)

# 多返回值 默认返回元组类型
# f2(f1())
#
# def f3():
#     return 1,2
#
# a1 = f3()
# print(a1)

#
# def f4():
#     f_a1 = 3
#     f_a2 = 4
#     f_a3 = 5
#     return [f_a1, f_a2, f_a3]
# print(f4())

# ===================================
# 函数的位置参数和关键字参数

# def f1(name, age , id):
#     print(f'{name}是{age}岁，身份证号为{id}')
#
# # 位置参数
# f1('慕容', 20 , 123456789)
# f1(20, 123456789, '慕容')
#
# # 关键字参数
# f1(id=132456789, name= '慕容', age=20)
#
# # 位置参数加+关键字参数,位置参数必须在关键字前面
# f1('慕容', id=123456789, age=20)
#
# # 默认参数(位置参数必须在关键字前面)
# def f2(name, age, id, gender='女'):
#     print(f'{name}是{age}岁，性别{gender},身份证号为{id}')
#
# f2('慕容', 20 , 123456789)
# f2('慕容', 20 , 123456789, '男')

# ===================================
# 不定长参数位置参数和关键字参数

# def f1(*args):
#     print(args)
#
# f1('慕容', 20 , 123456789) #自动把参数打包成元组
#
# def f2(**kwargs):
#     print(kwargs)
#
# f2(id=132456789, name= '慕容', age=20) # 自动打包成字典

# ====================================
# 元组字典的拆包

# def f1():
#     return 1, 2, 3
# a1, a2, a3 = f1()
# print(a1)
# print(a2, a3)
#
# def f2():
#     return {'name': '慕容', 'id': 123456789, 'age': 20}
# a4, a5, a6 = f2()
# print(a4, a5, a6)
# print(f2()[a4], f2()[a5], f2()[a6])

# =====================================
# 交换变量

# a1 = 100
# a2 = 200
# a3 = 0
#
# a3 = a1
# a1 = a2
# a1 = a3
# print(a1, a2)
#
# a1, a2 = a2, a1
# print(a1, a2)

# ===================================
# 可变和不可变类型(可变int,float,str,tuple  不可变list,dict,set)
# id 就是内存地址的编号,通常用16进制表示
# def id_hex(p1):
#     print(hex(id(p1)))
# def f1(p1, p2):
#     print(id(p1) - id(p2))
''' 
不可变类型:一个值只有一个内存空间，如果有新的值会新创建另一个内存空间来储存
         虽然变量名字不同但是用的都是同一块内存的同一个值
'''
# a1 = 100
# id_hex(a1)
# a2 = 100
# a3 = a1
# id_hex(a2)
# id_hex(a3)
# a1 = 101
# id_hex(a1)

''' 
可变类型:用的是同一块内存，修改新增不会新创建内存空间来储存

'''
# list1 = [1,2,3]
# id_hex(list1)
# list1.append(4)
# id_hex(list1)

# 当做参数传入有不同的结果

# def f1(a):
#     a += 100
#     id_hex(a)
# def f2(a):
#     a.append(123)
#     id_hex(a)
#
# b = 200
# f1(b)
# id_hex(b)
#
# list1 = [1, 2, 3, 4]
# f2(list1)
# id_hex(list1)
# print(list1)

'''
递归函数 和 匿名函数

递归：自己调用自己
lambda：只有一个返回值的函数简写
'''
# 递归：自己调用自己
# 1+2+3+4+5

# def f1(p1,n):
#     if n == 1:
#         return p1
#
#     return p1 + f1(p1 + 1, n - 1)
#
# print(f1(1, 3))
#
# # lambda 只有一个返回值的函数简写
#
# # 语法：   函数名 = lambda 参数：返回值
# # 无参数
# f2 = lambda : '132'
# print(f2())
#
# # 有参数
# f3 = lambda p2: p2
# print(f3(5))
#
# f4 = lambda  p3,p4: p3+p4
# print(f4(3, 5))
#
# # 默认参数
# f5 = lambda p5 = 123: p5
# print(f5())
#
# # 不定长位置参数
# f6 = lambda *args: args
# print(f6(4,5,6))
#
# # 不定长关键字参数
# f7 = lambda **kwargs: kwargs
# print(f7(a = 1, b = 2))

'''
内置函数

abs()       绝对值函数
round()     四舍五入函数
f(g(x))     高阶函数
map(f1, list1)  将list1每个元素传人f1中，并将函数的返回结果组成新的列表迭代器,要进行强制转换成列表
reduce()        将list1的逐渐元素传人f1中，然后累计并将结果返回组成新的列表
filter()        将list1的每个元素传人f1中，然后过滤掉不符合的元素，符合条件的返回列表迭代器
'''

# abs()和round()
# print(abs(-1.2))
# print(round(1.5))

# 高阶函数
# def f_1(a, b, f):
#     return f(a) + f(b)
# print(f_1(1.3, 1.5, round))


# map(f1, list1)  将list1每个元素传人f1中，并将函数的返回结果组成新的列表迭代器,要进行强制转换成列表

# def f1(p1):
#     return p1**2
#
# list1 = [2, 3, 5]
# list2 = map(f1, list1)
# print(list(list2))

# reduce() 将list1的逐渐元素传人f1中，然后累计并将结果

# import functools
#
# def f2(p2, p3):
#     return p2 + p3
#
# list3 = [1, 2, 3, 4, 5, 6]
# print(functools.reduce(f2, list3))

# filter()   将list1的每个元素传人f1中，然后过滤掉不符合的元素，符合条件的返回列表迭代器

# def f3(p4):
#     return p4 % 2 == 0
#
# print(list(filter(f3, list3)))


# ====================================================
'''
文件操作

打开文件
操作文件
关闭文件
文件重命名
操作文件夹
'''

# 打开文件
'''
文件对象 = open(目标文件， 访问模式)

访问模式:
    w: 只写，文件指针在开头，先删除原数据再写入，文件不存在则创建
        wb:  二进制写入（包含w的所有特点：文件指针在开头，写人原数据会被覆盖，文件不存在则创建）
        w+:  读写（包含w的所有特点）
        wb+: 二进制读写（包含w的所有特点）
    r: 只读，文件指针在开头，边写边覆盖原数据，文件不存在则报错
        rb:  二进制读取（包含r的所有特点）
        r+:  读写（包含r的所有特点）
        rb+: 二进制读写（包含r的所有特点）
    a: 追加，文件指针在末尾，文件不存在则创建
        
'''
# 操作文件
'''
写
文件对象.write()
'''
'''
读
文件对象.read(num)  读取全部数据
文件对象.readlines(num) 按行读取数据并把数据组成列表
文件对象.readline(num)  一次读取一行的内容
文件对象.seek(偏移量, 起始位置)  移动文件指针

num参数是读取数据的字节长度，不填默认读取全部数据
'''
# 关闭文件
'''
文件对象.close()

'''
# 打开文件->操作文件->关闭文件（保存）
file1 = open('test.txt', 'r+')
file1.write('567')
file1.close()

file1 = open('test.txt', 'rb')
a = file1.read()
print(a)

# 文件操作函数
'''
文件重命名  os.rename(目标文件名， 新文件名)
删除文件   os.remove(目标文件名)
'''
# 先导入os模块
import os

# 文件夹操作函数
'''
获取当前目录      os.getcwd()
切换目录         os.chdir(目录)
获取目录列表      os.listdir(目录)
文件夹重命名      os.rename(目标文件夹名， 新文件夹名)
删除文件夹        os.remove（目标文件夹名)
'''

# 文件备份
# 打开文件->读取文件数据并储存数据->被储存的数据写入新的文件->关闭文件
