"""
string储存结构:
string(字符串)类型可以接受任何格式的数据

最大长度512M

添加:
    1- 设置键值: set key value
        例: set name itcast
    2- 设置键值及过期时间(以秒为单位): setex key seconds value
        例: setex aa 3 aa

    3- 设置多个(m)键值: mset key1 value1 key2 value2...
        例: mset a1 python a2 java a3 c

    4- 追加值: append key value
        例4：向键为a1中追加值haha: append a1 haha

获取:
    1- 获取单个值: get key
        例: get name
    2- 获取多个值: mget key1 key2 ...
        例: mget a1 a2 a3
"""