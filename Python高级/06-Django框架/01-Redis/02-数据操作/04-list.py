"""
list列表的元素类型为string
按照插⼊顺序排序
值的类型为string

添加:
    1- 在左侧插⼊数据: lpush key value1 value2 ...
        例: lpush a1 a b c

    2- 在右侧插⼊数据: rpush key value1 value2 ...
        例: rpush a1 0 1

    3- 在指定元素的前或后插⼊新元素: linsert key (before或after) 现有元素 新元素
        例: linsert key before或after 现有元素 新元素
查询:
    1- 返回列表里指定范围内的元素:
        1) start、stop为元素的下标索引
        2) 索引从左侧开始，第⼀个元素为0
        3) 索引可以是负数，表示从尾部开始计数，如-1表示最后⼀个元素
            lrange key start stop

            例: lrange a1 0 -1

修改:
    1- 设置指定索引位置的元素值, 索引从左侧开始，第⼀个元素为0, 索引可以是负数，表示尾部开始计数，如-1表示最后⼀个元素
        lset key index value

        例：修改键为a1的列表中下标为1的元素值为z
            lset a1 1 z

删除:
    1- 删除指定元素: 将列表中前count次出现的值为value的元素移除
        count > 0: 从头往尾移除
        count < 0: 从尾往头移除
        count = 0: 移除所有
        lrem key count value

        例: lpush a2 a b a b a b
            lrem a2 -2 b (从a2列表右侧开始删除2个b)
            lrange a2 0 -1

"""