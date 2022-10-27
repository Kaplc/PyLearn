"""
1- 查找, 参数支持正则表达式: keys pattern
    例: 查看所有键: keys *
        查看名称包含a的键: keys a*

2- 判断键是否存在, 存在返回1, 否则返回0: exists key1
    例: exists a1

3- 查看键对应的value的类型: type key
    例: type a1

4- 删除键及对应的值: del key1 key2
    例: del a2 a3

5- 设置过期时间，以秒为单位(如果没有指定过期时间则⼀直存在，直到使用del移除): expire key seconds
    例: expire a1 3

6- 查看有效时间，以秒为单位(值为-2为以过期): ttl key
    例: ttl bb

"""