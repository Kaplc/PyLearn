"""
浅拷贝: copy函数是浅拷贝，只对可变类型的第一层对象进行拷贝，
       对拷贝的对象开辟新的内存空间进行存储，不会拷贝对象内部的子对象

深拷贝: deepcopy函数是深拷贝, 只要发现对象有可变类型就会对该对象到最后一个可变类型的每一层对象就行拷贝,
       对每一层拷贝的对象都会开辟新的内存空间进行存储

不可变类型有: 数字、字符串、元组
可变类型有: 列表、字典、集合

总结: 1)深浅拷贝对于不可变类型都不会创建新内存空间, 单纯引用.
     2)浅拷贝只复制第一层, 即使第一层是不可变类型, 后面层是可变类型也不会开辟内存空间按第一层判断
     3)深拷贝只要有一层是可变, 全部层都开辟新内存空间
"""

import copy


def shallow_copy_immutable():
    # 不可变类型浅拷贝
    print("不可变类型浅拷贝: 数字、字符串、元组")
    a1 = 123
    b1 = copy.copy(a1)

    # 查看内存地址
    print("数字:")
    print(hex(id(a1)))
    print(hex(id(b1)))

    print("字符串:")

    a2 = "字符串"
    b2 = copy.copy(a2)
    print(hex(id(a2)))
    print(hex(id(b2)))

    print("元组:")

    a3 = (2, 3)
    b3 = copy.copy(a3)
    print(hex(id(a3)))
    print(hex(id(b3)))

    print("不可变内含可变")
    a4 = (1, 2, ["hello", "world"])
    b4 = copy.copy(a4)

    print(hex(id(a4)))
    print(hex(id(b4)))
    print(hex(id(a4[2])))
    print(hex(id(b4[2])))


def shallow_copy_variable():
    # 可变类型浅拷贝
    print("不可变类型浅拷贝")
    a1 = [1, 2]
    b1 = copy.copy(a1)  # 使用copy模块里的copy()函数就是浅拷贝了
    # 查看内存地址
    print(id(a1))
    print(id(b1))

    print("-" * 10)

    a2 = {"name": "张三", "age": 20}
    b2 = copy.copy(a2)
    # 查看内存地址
    print(id(a2))
    print(id(b2))
    print("-" * 10)

    a4 = [1, 2, [4, 5]]
    # 注意：浅拷贝只会拷贝父对象，不会对子对象进行拷贝
    b4 = copy.copy(a4)  # 使用copy模块里的copy()函数就是浅拷贝了
    # 查看内存地址
    print(id(a4))
    print(id(b4))

    # 查看子对象内存地址
    print(id(a4[2]))
    print(id(b4[2]))


def deep_copy_immutable():
    a1 = 1
    b1 = copy.deepcopy(a1)  # 使用copy模块里的deepcopy()函数就是深拷贝了
    # 查看内存地址
    print(id(a1))
    print(id(b1))
    print("-" * 10)
    a2 = "张三"
    b2 = copy.deepcopy(a2)
    # 查看内存地址
    print(id(a2))
    print(id(b2))
    print("-" * 10)
    a3 = (1, 2)
    b3 = copy.deepcopy(a3)
    # 查看内存地址
    print(id(a3))
    print(id(b3))
    print("-" * 10)

    # 注意: 元组里面要是有可变类型对象，发现对象有可变类型就会该对象到最后一个可变类型的每一层对象进行拷贝
    a4 = (1, ("李四", [1, 2]))
    b4 = copy.deepcopy(a4)
    # 查看内存地址
    print(id(a4))
    print(id(b4))
    # 元组里面的可变类型子对象也会进行拷贝
    print(id(a4[1][1]))
    print(id(b4[1][1]))


def deep_copy_variable():
    a1 = [1, 2]
    b1 = copy.deepcopy(a1)  # 使用copy模块里的deepcopy()函数就是深拷贝了
    # 查看内存地址
    print(id(a1))
    print(id(b1))
    print("-" * 10)
    a2 = {"name": "张三"}
    b2 = copy.deepcopy(a2)
    # 查看内存地址
    print(id(a2))
    print(id(b2))
    print("-" * 10)
    a3 = {1, 2}
    b3 = copy.deepcopy(a3)
    # 查看内存地址
    print(id(a3))
    print(id(b3))
    print("-" * 10)

    a4 = [1, 2, ["李四", "王五"]]
    b4 = copy.deepcopy(a4)  # 使用copy模块里的deepcopy()函数就是深拷贝了
    # 查看内存地址
    print(id(a4))
    print(id(b4))

    # 查看内存地址
    print(id(a4[2]))
    print(id(b4[2]))
    a4[2][0] = "王五"
    # 因为列表的内存地址不同，所以数据不会收到影响
    print(a4)
    print(b4)


if __name__ == '__main__':
    # shallow_copy_immutable()
    # shallow_copy_variable()
    # deep_copy_immutable()
    deep_copy_variable()
