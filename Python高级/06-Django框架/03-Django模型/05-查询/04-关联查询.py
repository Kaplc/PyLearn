"""
1- 关联查询
    一到多: 先查询少的表得到的数据再去多的表查
        查询书籍id为1的所有人物信息
            book = BookInfo.objects.get(id=1)
            # 系统默认生成的关联模型: 语法: 类名小写_set
            book.peopleinfo_set.all()
    多到一:
        查询人物id为1的书籍信息
            person = PeopleInfo.objects.get(id=1)
            # 事先定义的外键才能调用
            person.book
    访问属性
        person.book_id
        person.is_delete

2- 关联过滤查询
    语法: filter(关联模型类名小写_字段_运算符=值)
    例: 查询图书，要求图书人物为"郭靖"
            book = BookInfo.objects.filter(peopleinfo__name='郭靖')

        查询图书，要求图书中人物的描述包含"八"
            book = BookInfo.objects.filter(peopleinfo__description__contains='八')

        查询书名为“天龙八部”的所有人物
            people = PeopleInfo.objects.filter(book__name='天龙八部')

        查询图书阅读量大于30的所有人物
            people = PeopleInfo.objects.filter(book__readcount__gt=30)



"""