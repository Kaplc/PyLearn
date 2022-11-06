"""
1- 安装django-redis

2- 配置Redis数据库
    default：
    默认的Redis配置项，采用0号Redis库。

    session:
    状态保持的Redis配置项，采用1号Redis库。

    SESSION_ENGINE:
    修改session存储机制使用Redis保存。

    SESSION_CACHE_ALIAS：
    使用名为"session"的Redis配置项存储session数据

"""
