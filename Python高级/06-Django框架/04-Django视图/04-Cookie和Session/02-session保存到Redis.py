"""
1- session储存方式:
    1) Django默认保存session在数据库, 在django_session表中
        SESSION_ENGINE='django.contrib.sessions.backends.db'

    2)本地缓存
        SESSION_ENGINE='django.contrib.sessions.backends.cache'

    3) 混合存储( 优先从内存读取, 没有则读取数据库)
        SESSION_ENGINE='django.contrib.sessions.backends.cached_db'

注意: 丢失不能找回, 读取速度比数据库快

2- 将session储存到Redis
    1) 安装django-redis
        pip install django-redis

    2) 配置setting.py

        CACHES = {
            'default': {
                'BACKEND': 'django_redis.cache.RedisCache',
                'LOCATION': 'redis://127.0.0.1:6379/1',
                'OPTIONS': {
                    'CLIENT_CLASS': 'django_redis.client.DefaultClient',
                }
            }
        }
        SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
        SESSION_CACHE_ALIAS = 'default'



"""