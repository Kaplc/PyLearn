'''
1- 内连接(交集)
    连接共有部分
    select 表1.字段 表2.字段 ... from 表1 inner join 表2 on 表1.字段1 = 表2.字段2;
    例: 1, 使用内连接查询学生表和班级表
            select name, height, c_name from students s inner join classes c on s.c_id = c.id;

2- 左连接右连接
    左往右连接,右表没有为null
    select 字段  from 表1 left join 表2 on 表1.字段1 = 表2.字段2;
        例: select name, height, c_name from students s left join classes c on s.c_id = c.id;
    select 字段  from 表1 right join 表2 on 表1.字段1 = 表2.字段2;
        例: select name, height, c_name from students s right join classes c on s.c_id = c.id;

3- 自连接
    跟内连接一样, 一张表分成两张表写
    表内的附属关系
        例: select c.name p.name from cities c inner join cities p c.aid = p.id;

4- 子查询
    例: 1, 查询大于平均年龄的学生
            select * from students where age > (select avg(age) from students);
        2, 查询学生在班的所有班级名字
            select * from classes where id in(select c_id from students where c_id is not null);
        3, 查找年龄最大,身高最高的学生
            select * from students where age=(select max(age) from students) and
            height=(select max(height) from students);
'''