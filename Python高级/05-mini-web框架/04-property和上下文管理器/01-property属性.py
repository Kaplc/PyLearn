"""
1- property属性就是负责把一个方法当做属性进行使用
2- 定义property属性有两种方式: 1)装饰器方式 2) 类属性方式
"""

import logging


# 装饰器方式
class Person(object):

    def __init__(self):
        self.__age = 0

    # 调用属性方式调用方法
    @property
    def age(self):
        return self.__age

    # 设置属性时执行的方法
    @age.setter
    def age(self, new_age):
        if new_age >= 150:
            print("PersonI: 设置年龄过大")
            # logging.error("PersonI: 设置年龄过大")

        else:
            self.__age = new_age


# 类属性方式
class PersonII(object):
    def __init__(self):
        self.__age = 10

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age >= 150:
            print("PersonII: 设置年龄过大")
            logging.error("PersonII: 设置年龄过大")

        else:
            self.__age = new_age

    # 类属性方法设置property
    # property的参数说明:
    # 第一个参数是获取属性时要执行的方法
    # 第二个参数是设置属性时要执行的方法
    # 直接调用age, 而不是调用 get_age, set_age 具体的方法
    age = property(get_age, set_age)


if __name__ == '__main__':
    new_person_age = Person()
    # 调用属性执行方法
    result = new_person_age.age
    print('PersonI:', result)

    # 修改属性执行修改方法
    new_person_age.age = 151

    new_result = new_person_age.age = 100
    print('PersonI:', new_result)

    new_personII_age = PersonII()
    # PersonII: 调用属性执行方法
    resultII = new_personII_age.age
    print('PersonII:', resultII)

    # 修改属性执行修改方法
    new_personII_age.age = 200

    new_resultII = new_personII_age.age = 50
    print('PersonII:', new_resultII)

