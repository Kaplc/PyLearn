from django.db import models


# Create your models here.

# 准备书籍列表信息的模型类
class BookInfo(models.Model):
    # objects = models.Manager()
    # 创建字段，字段类型...
    # verbose_name在admin站点中显示的名称
    name = models.CharField(max_length=20, verbose_name='名称')
    pub_date = models.DateField(verbose_name='发布日期', null=True)
    readcount = models.IntegerField(default=0, verbose_name='阅读量')
    commentcount = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'bookinfo'  # 指明数据库表名
        verbose_name = '图书'  # 在admin站点中显示的名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.name


# 准备人物列表信息的模型类
class PeopleInfo(models.Model):
    # objects = models.Manager()
    # 选择有序字典
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )

    name = models.CharField(max_length=20, verbose_name='名称')
    # choices=GENDER_CHOICES枚举类型
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    description = models.CharField(max_length=200, null=True, verbose_name='描述信息')

    # 定义外键: models.ForeignKey(要关联的主表名, 删除主键时外键进行的操作, 后台显示的名称)
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')  # 外键
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物信息'

    def __str__(self):
        return self.name
