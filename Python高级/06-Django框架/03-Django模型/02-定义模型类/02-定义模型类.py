"""
1） 数据库表名:
    模型类如果未指明表名，Django默认以小写app应用名_小写模型类名为数据库表名。
    可通过db_table指明数据库表名。

2） 关于主键:
    django会为表创建自动增长的主键列，每个模型只能有一个主键列，
    如果使用选项设置某属性为主键列后django不会再创建自动增长的主键列。
    默认创建的主键列属性为id，可以使用pk代替，pk全拼为primary key。

3） 属性命名限制:
    1. 不能是python的保留关键字。
    2. 不允许使用连续的下划线，这是由django的查询方式决定的。
    3. 定义属性时需要指定字段类型，通过字段类型的参数指定选项，语法如下：

    属性=models.字段类型(选项)

4) 字段类型
        类型	                                    说明

    AutoField	        自动增长的IntegerField，通常不用指定，不指定时Django会自动创建属性名为id的自动增长属性
    BooleanField	    布尔字段，值为True或False
    NullBooleanField	支持Null、True、False三种值
    CharField	        字符串，参数max_length表示最大字符个数
    TextField	        大文本字段，一般超过4000个字符时使用
    IntegerField	    整数
    DecimalField	    十进制浮点数， 参数max_digits表示总位数， 参数decimal_places表示小数位数
    FloatField	        浮点数
    DateField	        日期， 参数auto_now表示每次保存对象时，自动设置该字段为当前时间，用于"最后一次修改"的时间戳，它总是使用当前日期，默认为False； 参数auto_now_add表示当对象第一次被创建时自动设置当前时间，用于创建的时间戳，它总是使用当前日期，默认为False; 参数auto_now_add和auto_now是相互排斥的，组合将会发生错误
    TimeField	        时间，参数同DateField
    DateTimeField	    日期时间，参数同DateField
    FileField	        上传文件字段
    ImageField	        继承于FileField，对上传的内容进行校验，确保是有效的图片

5） 选项

    选项	                说明
    null	    如果为True，表示允许为空，默认值是False
    blank	    如果为True，则该字段允许为空白，默认值是False
    db_column	字段的名称，如果未指定，则使用属性的名称
    db_index	若值为True, 则在表中会为此字段创建索引，默认值是False
    default	    默认
    primary_key	若为True，则该字段会成为模型的主键字段，默认值是False，一般作为AutoField的选项使用
    unique	    如果为True, 这个字段在表中必须有唯一值，默认值是False

6） 外键,在设置外键时，需要通过on_delete选项指明主表删除数据时，对于外键引用表数据如何处理，
    在django.db.models中包含了可选常量：

        CASCADE级联，删除主表数据时连通一起删除外键表中数据

        PROTECT保护，通过抛出ProtectedError异常，来阻止删除主表中被外键应用的数据

        SET_NULL设置为NULL，仅在该字段null=True允许为null时可用

        SET_DEFAULT设置为默认值，仅在该字段设置了默认值时可用

        SET()设置为特定值或者调用特定方法

        DO_NOTHING不做任何操作，如果数据库前置指明级联性，此选项会抛出IntegrityError异常
"""