"""
优势: 速度比DJango快10倍+

1- 安装: pip install jinja2

2- 配置jinja2 (看文档)
    1) 创建jinja2_env.py
        from jinja2 import Environment

        def environment(**options):
            env = Environment(**options)

            return env

    2) 设置setting.py
        TEMPLATES =[
            'BACKEND': 'django.template.backends.jinja2.Jinja2', #修改1
            ....
            'environment': 'jinja2_env.environment',# 修改2

        ]

3- 使用
    大部分语句跟Django一样
    loop.index  当前循环次数从1开始
    loop.index0 当前循环次数从1开始
    loop.revindex   到循环结束需要迭代次数从1开始
    loop.revindex0  到循环结束需要迭代次数从0开始
    loop.first  是第一次迭代, 为true
    loop.last   是最后一次迭代, 为true
    loop.length 序列中项目数
    loop.cycle


4- jinja2过滤器



5- 在jinja2环境使用Django自带过滤器
    1) 子应用目录创建jinja2_env.py
        from django.template.defaultfilters import date
        from jinja2 import Environment

        # 更新Django过滤器在jinja2中使用
        def environment(**options):
            env = Environment(**options)

            # 更新指定Django过滤器
            env.globals.update({
                'data': date
            })

            return env


"""
