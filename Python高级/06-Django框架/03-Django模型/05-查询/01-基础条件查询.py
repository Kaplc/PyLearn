"""
1- 基本查询
    get查询单一结果，如果不存在会抛出模型类.DoesNotExist异常
    all查询多个结果
    count查询结果数量

    例:
        查询id=1
            BookInfo.objects.get(id=1)
        查询主键=2
            BookInfo.objects.get(pk=2)
        查询主键=20, 不存在会抛出模型类.DoesNotExist异常
            BookInfo.objects.get(pk=20)
        查询所有结果
            BookInfo.objects.all()
        查询查询数量
            BookInfo.objects.count()

2- 过滤查询(实现SQL中的where功能)
    filter过滤出多个结果
    exclude排除掉符合条件剩下的结果
    get过滤单一结果

    1) 精确查询 (exact：表示判等)
        例:
            查询编号为1的图书
                exact：表示判等
                    BookInfo.objects.filter(id__exact=1)
                简写:
                    BookInfo.objects.filter(id=1)

    2) 模糊查询 (contains：是否包含)
        例:
            查询书名包含'湖'的图书
                BookInfo.objects.filter(name__contains='传')

    3) 指定开头结尾 (startswith、endswith)
        例:
            查询书名以'部'结尾的图书
                BookInfo.objects.filter(name__endswith='部')

    4) 空查询 (isnull：是否为null)
        例:
            查询书名为空的图书
                BookInfo.objects.filter(name__isnull=True)

    5) 范围查询 (in：是否包含在范围内)
        例:
            查询编号为1或3或5的图书
                BookInfo.objects.filter(id__in=[1,3,5])

    6) 比较查询 {
        gt大于 (greater then)
        gte大于等于 (greater then equal)
        lt小于 (less then)
        lte小于等于 (less then equal)
        }
        例:
            查询编号大于3的图书
                BookInfo.objects.filter(id__gt=3)
            查询编号小于等于3的图书(使用exclude()过滤器)
                BookInfo.objects.exclude(id__gt=3)

    7) 日期查询 (year、month、day、week_day、hour、minute、second：对日期时间类型的属性进行运算)
        例:
            查询1980年发表的图书
                BookInfo.objects.filter(pub_date__year=1980)
            查询1990年1月1日后发表的图书(固定格式)
                BookInfo.objects.filter(pub_date__gt='1990-1-1')
"""