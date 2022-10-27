"""
1-查询集QuerySet
    下面方法都是返回结果集合
    all()：返回所有数据
    filter()：返回满足条件的数据
    exclude()：返回满足条件之外的数据
    order_by()：对结果进行排序

    判断某一个查询集中是否有数据: exists()返回True则有, 否则无

  查询集的特性
    1) 惰性执行
        执行创建结果集不会查询数据库, 只有调用结果集才会查询
            books = BookInfo.objects.all() // 不会查询

            for book in books: // 使用才会查询
                print(book.name)
    2) 缓存
        将结果集保存在一个变量的时候, 第二次使用就会调用缓存不会重复进行查询
        from book.models import BookInfo

        // 不会调用缓存, 速度慢
        [book.id for book in BookInfo.objects.all()]

        [book.id for book in BookInfo.objects.all()]

        // 调用缓存查询, 速度快
        books=BookInfo.objects.all()

        [book.id for book in books]

        [book.id for book in books]

2- 限制查询集
    切片操作(不支持负数索引)
    books = BookInfo.objects.all()[0:2]


3- 分页
    #查询数据
    books = BookInfo.objects.all()
    #导入分页类
    from django.core.paginator import Paginator
    #创建分页实例 ("2"表示每页多少条数据)
    paginator=Paginator(books,2)
    #获取指定页码的数据 (从1开始)
    page_skus = paginator.page(1)
    # 页内的数据从0开始
    page_skus[0]
    page_skus[1]

    #获取分页页数
    total_page=paginator.num_pages

"""