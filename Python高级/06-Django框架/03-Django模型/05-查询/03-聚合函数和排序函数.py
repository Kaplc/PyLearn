"""
1- 聚合函数:
    被定义在django.db.models中
    使用aggregate()过滤器调用聚合函数。聚合函数包括：Avg平均，Count数量，Max最大，Min最小，Sum求和，

    aggregate的返回值是一个字典类型
        例：查询图书的总阅读量
                from django.db.models import Sum
                BookInfo.objects.aggregate(Sum('readcount'))

            查询图书总数
            使用count时一般不使用aggregate()过滤器, count函数的返回值是一个数字
                BookInfo.objects.count()

2- 排序:
    order_by对结果进行排序,

        例: 默认升序
                BookInfo.objects.all().order_by('readcount')

            降序: 字段前面加'-'
                BookInfo.objects.all().order_by('-readcount')

"""