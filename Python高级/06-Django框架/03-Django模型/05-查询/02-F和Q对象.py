"""

F对象: 两个属性比较使用(django.db.models)
    例: 查询阅读量大于等于评论量的图书
            from django.db.models import F
            BookInfo.objects.filter(readcount__gt=F('commentcount'))
        查询阅读量大于2倍评论量的图书(可以在F对象上使用算数运算)
            BookInfo.objects.filter(readcount__gt=F('commentcount')*2)

Q对象: Q对象可以使用&、|连接，&表示逻辑与，|表示逻辑或(Q对象被义在django.db.models)

    and查询: 需要使用Q()对象结合&运算符, 也可以多个过滤器逐个调用表示逻辑与关系
        例: 查询阅读量大于20，并且编号小于3的图书
            方法一, 使用&查询
                BookInfo.objects.filter(Q(readcount__gt=20)&Q(id__lt=3))

            方法二, 多个过滤器逐个调用
                BookInfo.objects.filter(readcount__gt=20,id__lt=3)
                或者
                BookInfo.objects.filter(readcount__gt=20).filter(id__lt=3)

    or查询: 需要使用Q()对象结合|运算符，
        例: 查询阅读量大于20，或编号小于3的图书，只能使用Q对象实现
            BookInfo.objects.filter(Q(readcount__gt=20)|Q(id__lt=3))

    not查询: 使用~操作符
        例: 查询编号不等于3的图书
            BookInfo.objects.filter(~Q(id=3))
"""