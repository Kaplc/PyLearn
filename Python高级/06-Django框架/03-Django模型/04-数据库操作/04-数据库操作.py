"""
在shell终端使用

objects无法使用安装
pip install django-stubs

添加数据:
    1) 通过创建模型类对象，执行对象的save()方法保存到数据库中
        from models_learn.models import BookInfo

        book = BookInfo(
            name='python入门',
            pub_date='2010-1-1'
        )
        # 要使用save()上传数据库
        book.save()
        book

    2) 通过模型类.objects.create()
        PeopleInfo.objects.create(
            name='itheima',
            book=book
        )

修改数据:
    1) 修改模型类对象的属性，然后执行save()方法
        person = PeopleInfo.objects.get(name='itcast')
        person.name = 'itcast'
        person.save()

    2)使用模型类.objects.filter().update()，会返回受影响的行数
        PeopleInfo.objects.filter(name='itcast').update(name='传智播客')

删除数据:
    1) 模型类对象delete
        person = PeopleInfo.objects.get(name='传智播客')
        person.delete()

    2) 模型类.objects.filter().delete()
        BookInfo.objects.filter(name='python入门').delete()
"""