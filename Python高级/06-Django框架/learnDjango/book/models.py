from django.db import models

# Create your models here.
"""

1. 定义模型类
    根据书籍表结构设计模型类:
        模型类：BookInfo
        书籍名称字段：name
    根据人物表结构设计模型类：
        模型类：PeopleInfo
        人物姓名字段：name
        人物性别字段：gender
        外键约束：book
            外键要指定所属的模型类book = models.ForeignKey(BookInfo)
    说明 :
        书籍-人物的关系为一对多. 一本书中可以有多个英雄.
        不需要定义主键字段, 在生成表时会自动添加, 并且值为自增长
"""


# 模型类：BookInfo
class BookInfo(models.Model):
    # models管理器重命名

    object = models.Manager()
    # 创建name字段char类型长度10

    name = models.CharField(max_length=10)

    # 优化在管理员页面的展示
    def __str__(self):
        return self.name


class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)

    # BooleanField: 布尔字段，值为True或False
    gender = models.BooleanField()

    # 创建外键
    """
    on_delete选项指明主表删除数据时，对于外键引用表数据如何处理，
    在django.db.models中包含了可选常量：

        CASCADE级联，删除主表数据时连通一起删除外键表中数据
        
        PROTECT保护，通过抛出ProtectedError异常，来阻止删除主表中被外键应用的数据
        
        SET_NULL设置为NULL，仅在该字段null=True允许为null时可用
        
        SET_DEFAULT设置为默认值，仅在该字段设置了默认值时可用
        
        SET()设置为特定值或者调用特定方法
        
        DO_NOTHING不做任何操作，如果数据库前置指明级联性，此选项会抛出IntegrityError异常
    """
    # on_delete=models.CASCADE
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
