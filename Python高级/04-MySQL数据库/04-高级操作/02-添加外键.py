'''
1- 外键作用: 保证数据有效性, 数据只能填其他表的主键

2- 字段添加外键: alter table 表名 add foreign key(本表字段) references 另表名(主键);
    例: alter table students add foreign key(c_id) references classes(id);

3- 创建表添加外键:
    create table teachers(
        id int not null primary key auto_increment,
        name varchar(20),
        s_id int not null,
        foreign key(s_id) reference school(id)
    );

4- 删除外键:
    1,先获取外键名称, 名称系统自动生成, CONSTRAINT '约束名称'
        show create table 表名;
    2, 根据名称删除外键
        alter table 表名 drop foreign key 外键名;
'''
