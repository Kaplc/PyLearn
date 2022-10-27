"""
set类型:
    1) 无序集合
    2) 元素为string类型
    3) 元素具有唯⼀性，不重复
    4) 说明：对于集合没有修改操作

添加:
    1- 添加元素: sadd key member1 member2 ...
        例: sadd a3 zhangsan sili wangwu

查询:
    1- 返回所有的元素: smembers key
        例: smembers a3


删除:
    1- 删除指定元素: srem key
        例: srem a3 wangwu

"""