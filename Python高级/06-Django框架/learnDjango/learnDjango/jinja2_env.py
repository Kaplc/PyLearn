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
