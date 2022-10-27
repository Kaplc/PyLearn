'''
0- 查看数据库所有表
    show tables;
1- 创建表
    create table 表名(字段名 字段类型 约束, ...)
    例: create table student(id int unsigned primary key auto_increment not null, name varchar(10) not null
        , age tinyint default 0, gender enum("男", "女") default "男");
        字段名: id
        字段类型: int unsigned(整数无符号)
        主键: primary key
        主键自增: auto_increment
        是否为空: not null

        字段名: name
        字段类型: varchar(10) (字符串10字符)
        是否为空: not null

        字段名: age
        字段类型: tinyint (小整型)
        默认值: default 0

        字段名: gender
        字段类型: enum("男", "女") (枚举类型)
        默认值: default "男"

2- 查看表的属性
    desc 表名;

3- 修改表
    添加字段: alter table 表名 add 字段名 类型 约束
    修改字段类型/约束: alter table 表名 modify 字段名 类型 约束
    修改字段名和字段类型/约束: alter table 表名 change 原名 新名 类型 约束
    删除字段: alter table 表名 drop column 字段名
    删除表: drop table 表名



'''