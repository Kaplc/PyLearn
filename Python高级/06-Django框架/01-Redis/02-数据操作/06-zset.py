"""
zset类型:
    1) sorted set，有序集合
    2) 元素为string类型
    3) 元素具有唯⼀性，不重复
    4) 每个元素都会关联⼀个double类型的score，表示权重，通过权重将元素从⼩到⼤排序
    5) 说明：没有修改操作

添加:
    1- 添加元素: zadd key score1 member1 score2 member2 ..
        例: zadd a4 4 lisi 5 wangwu 6 zhaoliu 3 zhangsan

查询:
    1- 返回所有的元素: zrange key start stop
        1) 返回指定范围内的元素
        2) start、stop为元素的下标索引
        3) 索引从左侧开始，第⼀个元素为0
        4) 索引可以是负数，表示从尾部开始计数，如-1表示最后⼀个元素
        例: zrange a4 0 -1

    2- 返回score值在min和max之间的成员: zrangebyscore key min max
        例: zrangebyscore a4 5 6

    3- 返回成员member的score值: zscore key member
        例: zscore a4 zhangsan

删除:
    1- 删除指定元素: zrem key member1 member2 ...
        例: zrem a4 zhangsan

    2- 删除权重在指定范围的元素: zremrangebyscore key min max
        例: zremrangebyscore a4 5 6

"""