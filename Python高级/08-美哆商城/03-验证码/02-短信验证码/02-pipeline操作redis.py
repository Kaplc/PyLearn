"""
1- pipeline介绍
    原理:
        1) 队列先进先出原则

    作用: 1) 可以打包多条指令发送给redis, 同样redis执行完毕也打包返回结果
         2) 减低redis通信延迟

2- 实现
    # 创建管道
    pl = redis_conn.pipeline()
    # 打包指令到管道
    pl.setex('sms_%s' % mobile, constants.SMS_CODE_REDIS_EXPIRES, sms_code)
    pl.setex('send_flag_%s' % mobile, constants.SEND_SMS_CODE_INTERVAL, 1)
    # 执行请求
    pl.execute()

"""
