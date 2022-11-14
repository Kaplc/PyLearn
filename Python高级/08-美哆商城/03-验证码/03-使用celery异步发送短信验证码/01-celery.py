"""
1- 生产者消费者设计模式
    生产者生成消息，缓存到消息队列中，消费者读取消息队列中的消息并执行

    生产者 --> 消息队列 <-- 消费者
    美哆商城 --> redis <-- celery

2- celery使用
    1) 安装pip install -U celery

    2) 创建celery_tasks包

    3) 定义main.py入口文件
        1. 导包celery
            from celery import Celery

        2. 创建celery实例
            celery_app = Celery('meiduo')

        3. 加载celery配置
            celery_app.config_from_object('celery_tasks.config')

        4. 注册任务
            celery_app.autodiscover_tasks(['celery_tasks.sms'])

    4) 创建配置文件config.py
        1. 定义消息队列
            broker_url= 'redis://127.0.0.1:6379/12'

    5) 创建软件包定义task.py任务文件
        1. 定义任务
        2. 装饰任务
            @celery_app.task(name='ccp_send_sms_code')

    6) 启动celery
        celery -A celery_tasks.main worker -l info

"""
