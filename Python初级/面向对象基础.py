'''
定义类

class 类名（project）：
    代码

'''

'''
定义属性
def __int__(self):
    self.变量名 = 数据
    
定义方法
def 函数名（self）：
    代码


'''


# self是指调用改方法、属性的对象
class washer():  # 定义类
    def __int__(self):  # 定义属性
        self.width = 100
        self.longth = 100

    def washing(self):  # 定义方法
        print('开始洗衣服')

    def dehydration(self):
        print('甩干')


'''
创建对象

对象名 = 类名（）

'''

washers = washer()

'''
调用类的属性和方法

对象名.属性名
对象名.方法名（）

'''

# print(f'{washers.longth}')
# washers.washing()
# washers.dehydration()

'''
类外面定义属性
'''


class washer():  # 定义类
    def __int__(self):  # 定义属性
        self.width = 100
        self.longth = 100

    def washing(self):  # 定义方法
        print('开始洗衣服')

    def dehydration(self):
        print('甩干')


washers.width = 50  # 类外面定义属性
# print(washers.width)
'''
类里面获取属性
'''


class washer():  # 定义类
    def __init__(self):  # 定义属性
        self.width = 100
        self.long = 100

    def washing(self):  # 定义方法
        print('开始洗衣服')

    def dehydration(self):
        print('甩干')

    def long_width(self):
        print(f'长{self.long},宽{self.width}')  # 类里面获取属性


# washers_2 = washer()
# washers_2.long_width()

'''
__str__方法

def __str__(self)：
    return 数据

print（对象）直接输出return后面的数据
====================================
__del__方法

def __del__(self):
    代码
    
当删除对象时
del 对象名
执行__del__的代码
'''


class washer():  # 定义类
    def __init__(self):  # 定义属性
        self.width = 100
        self.long = 100

    def __str__(self):  # __str__方法
        return '对对象使用print打印的东西'

    def __del__(self):  # __del__方法
        print('删除对象后会执行的代码')

    def washing(self):  # 定义方法
        print('开始洗衣服')

    def dehydration(self):
        print('甩干')

    def long_width(self):
        print(f'长{self.long},宽{self.width}')  # 类里面获取属性


# washers_3 = washer()
# print(washers_3)
# del washers_3

# =====================================================================


'''
                继承
含义：子类继承了父类之后拥有父类的所有属性和方法

1.单继承
2.多继承
3.子类重写父类同名属性和方法
4._mro
5.子类调用父类同名属性和方法
6.多层继承
7.super()
8.定义私有属性和方法（私有属性和方法不能被继承）
9.获取和修改私有属性

'''


class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


class School(object):
    def __init__(self):
        self.kongfu = '[黑马煎饼果子]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 单继承
class Prentice1(Master):
    # super调用父类的属性和方法
    def make_cake(self):
        super().__init__()
        super().make_cake()


# 多继承
class Prentice2(Master, School):
    pass


# daqiu = Prentice1()
# daqiu.make_cake()
#
# daqiu2 = Prentice2()

# 多个父类时默认使用第一个父类的同名属性和方法
# daqiu2.make_cake()

class Prentice3(Master, School):
    # 子类重写父类属性
    def __init__(self):
        self.kongfu = '[独创煎饼果子]'

    # 子类重写父类方法
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

    # 子类调用父类同名属性和方法,保证调用的方法使用父类的属性必须先父类属性初始化
    def make_master_make(self):
        # 父类属性初始化
        Master.__init__(self)
        Master.make_cake(self)


# 子类与父类有同名的属性和方法，默认使用子类
'''daqiu3 = Prentice3()
print('子类与父类有同名的属性和方法，默认使用子类：')
print(daqiu3.kongfu)
daqiu3.make_cake()
print('=============================================')'''

#  调用父类同名属性和方法
'''print('调用父类同名属性和方法：')
daqiu4 = Prentice3()
daqiu4.make_master_make()
print('=============================================')'''

# 显示继承关系
'''print('显示继承关系：')
print(Prentice3.__mro__)
print('=============================================')'''


# 多层继承
class grandson(Prentice3):
    pass


'''print('多层继承:')
xiaoqiu = grandson()
xiaoqiu.make_cake()
xiaoqiu.make_master_make()
print('=============================================')'''

# 属性初始化后数值被改变，后续的调用都沿用这个被初始化的数据
'''print('属性初始化后数值被改变，后续的调用都沿用这个被初始化的数据:')
xiaoqiu.make_cake()

superPrentice = Prentice1()
print('=============================================')

print('super快捷调用父类:')
superPrentice.make_cake()
print('=============================================')'''

'''
私有属性和方法定义
修改和访问私有属性

对象不能访问私有属性和方法
私有属性和方法不能被继承
私有属性和方法只能在类里面访问和修改
'''


class Private():
    # 定义私有属性变量名前面加__
    def __init__(self):
        self.__p1 = 100

    # 定义私有方法在方法名前面加__
    def __f1(self):
        print('调用私有类')

    # 修改和调用私有属性
    def modify(self):
        self.__p1 = 1000
        print(self.__p1)

    def modify_f1(self):
        self.__f1()


class InheritPrivate(Private):
    pass


'''ob1 = InheritPrivate()
ob2 = Private()'''

# 私有属性和方法不能被继承
'''
ob1.__p1
ob1.__f1()
'''

# 对象不能访问私有属性和方法
'''
ob2.__p1
ob2.__f1()
'''
# 私有属性和方法的调用
'''
ob2.modify()
ob2.modify_f1()
'''

'''
多态
类属性和类方法
修改类属性
静态方法

'''


# 多态：给对象的方法传入不同参数得出不同结果
class Person(object):
    def work_with_dog(self, dog):  # 类似复合函数传参
        dog.work()


class Dog(object):
    def work(self):  # 子类重写父类方法
        print('指哪去哪')


class ArmyDog(Dog):
    def work(self):
        print('追击敌人')


class DrugDog(Dog):
    def work(self):
        print('追查毒品')


'''d = Dog()
ad = ArmyDog()
dd = DrugDog()

daqiu = Person()
daqiu.work_with_dog(ad) # 调用Personn的方法并传入对象
daqiu.work_with_dog(dd)
daqiu.work_with_dog(d)'''


# ======================================
# 类属性、类方法

class dog(object):
    tooth = 10  # 创建类属性


'''wangcai = dog()
xiaohei = dog()

print(dog.tooth)
print(wangcai.tooth)
print(xiaohei.tooth)'''

# 修改类属性
'''dog.tooth = 30'''
'''print(wangcai.tooth)'''

# 不能通过对象修改类属性，这是创建了实例属性
'''wangcai.tooth = 20'''
'''print(wangcai.tooth)
print(xiaohei.tooth)'''


class dog_1(object):
    __tooth = 50

    @classmethod  # 创建类方法：配合私有类属性使用
    def get_tooth(cls):
        return cls.__tooth

    @staticmethod  # 创建静态方法
    def info_print():
        print('静态方法既可以使用对象访问也可以使用类访问')


'''wangcai = dog_1
result = wangcai.get_tooth()
print(result)

wangcai.info_print()
dog_1.info_print()'''

'''
异常


捕获指定异常
捕获异常描述信息
捕获所有异常
异常的else、finally
异常传递
自定义异常

'''

# =======================
# 捕获指定异常

'''
try:  # 尝试执行try下的代码（一般只有一行）
    print(num)
    # print(1/0)
except NameError:  # 如果try的代码执行错误且错误类型是NameError则执行expect，不一致则跳过并报错
    print('有错误')

try:
    print(num)
    print(1 / 0)
except (NameError, ZeroDivisionError):  # 捕获多个错误类型
    print('有错误')
'''
# ======================
#  捕获异常信息
'''
try:
    print(num)
    print(1 / 0)
except NameError as inf:  # 捕获异常信息并储存至inf变量
    print(inf)
'''
# ======================
# 捕获所有异常信息
'''
try:
    print(num)
    print(1 / 0)
except Exception as inf_2: # Exception是所有错误的父类
    print(inf_2)
'''
# =====================
# 异常的else、finally
'''
try:
    pass
except:
    pass
else:
    # print('无异常执行')
    pass
finally:
    # print('无论如何最后执行')
    pass
'''

# ===================
# 异常传递
'''
import time
try:
    f = open('test.txt')
    try:
        while 1:
            content = f.readlines()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    except:
        print('意外终止了读取')
    finally:
        f.close()
        print('关闭文件')
except:
    print('改文件不存在')
'''

# =====================
# 自定义异常
'''
class insufficientLength(Exception): # 自定义错误类继承错误类
    def __init__(self, l, ml):
        self.length = l
        self.min_len = ml

    def __str__(self): 
        return f'长度为{self.length}, 不能少于{self.min_len}'

def mian():
    try:
        con = input('请输入密码:')
        if len(con)< 3: 
            raise insufficientLength(len(con), 3) # raise抛出自定义类的异常

    except Exception as result: # 捕获异常
        print(result)

    else:
        print('输入成功')
mian()
'''

# =======================
'''

导入模块
模块别名,功能别名
制作模块,测试和调用模块
all列表
制作包
导入包

'''
# ==============
# 导入模块


# (1) import 模块名
'''
import math

print(math.sqrt(9))  # 调用模块:模块名.功能名
'''
# (2) from 模块名 import 功能名,功能名...

'''
from math import sqrt

print(sqrt(9))  # 调用: 功能名
'''
# (3) from 模块名 improt * (导入模块所有允许的功能)
'''
from math import *

print(sqrt(10))  # 调用: 功能名
'''
# ========================
# 模块别名,功能别名
'''
import time as te

te.sleep(2)
print('hello')
'''
# 功能别名

'''from time import sleep as slp

slp(3)
print('hello world')
'''
# ==================
# 制作模块 : 在另一个py文件里面编写方法
# 导入,测试,all列表
from learn_module import *  # 仅导入了__all__列表内的方法
'''
print(testA(3, 6))
'''


# =================
# 制作包: 模块的集合    新建 -> 包 -> 包里面新建模块
# 导入包:

# (1) import 包名.模块名
import learnpy.mod1

# 调用: 包名.模块名.功能名
learnpy.mod1.mod1_print()



# (2) from 包名 import *  (导入包内所有模块,!!!必须先在__init__.py中初始化__all__列表,同样受到__all__列表的限制)
from learnpy import *

# 调用: 模块名.功能名
mod2.mod2_print()
