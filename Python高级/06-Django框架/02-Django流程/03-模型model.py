"""
1- 模型model: 控制数据库

2- Model中内嵌了ORM框架: 封装了各个数据库的指令需要切换数据库引擎进行使用

3- 实现流程:
    1) 定义模型类: 相当于创建表和字段 (类->表, 字段->属性)
        在models.py中定义模型类,继承自models.Model
    2) 模型迁移: 把定义的表生成
        1. 生成迁移文件：根据模型类生成创建表的语句: python manage.py makemigrations
            在migrations文件夹生成迁移文件
        2. 执行迁移：根据第一步生成的语句在数据库中创建表: python manage.py migrate
    3) 操作数据库: 调用相关方法操作数据库


默认采用sqlite3数据库来存储数据

"""