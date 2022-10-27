"""
hash储存结构: 大键里面含有小键-值
值的类型为string

添加:
    1- 设置单个属性: hset key(大键) field(小键) value(值)
        例: hset user name itheima

    2- 设置多个属性: hmset key field1 value1 field2 value2 ...
        例: hmset u2 name itcast age 11



查询:
    1- 获取指定(大)键所有的属性: hkeys key
        例: hkeys u2

    2- 获取⼀个属性的值: hget key field
        例: hget u2 name

    3- 获取所有属性的值: hvals key
        例: hvals u2

删除:
    1- 删除整个hash键及值，使用del命令(删除属性，属性对应的值会被⼀起删除): hdel key field1 field2 .
        例: hdel u2 age

"""