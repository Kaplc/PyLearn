'''
语法:
    select * from 表名 where 约束

1- 比较运算符:
    =, >, <, >=, <=, !=

    例: 1, 查询编号大于3
            select * from students where id > 3;
        2, 编号不大于4
            select * from students where id <= 4;
        3, 姓名不是黄蓉的
            select * from students where name != "黄蓉";
        4, 没有被删除的学生
            select * from students where is_del = 0;

2- 逻辑运算符:
    and, or, not
    例: 1, 查询编号大于3的女生
            select * from students where id > 3 and gender = "女";
        2, 编号不大于4或没有被删除的学生
            select * from students where id <= 4 or is_del = 0;
        3, 年龄不在18-25之间
            select * from students where not(age >=18 and age <=25);

3- 模糊查询:
    1, like关键字
    2, %任意多个任意字符
    3, _任意一个字符
        例: 1, 查询姓"黄"
                select * from students where name like '黄%';
            2, 查询姓"黄"并且姓名是两个字
                select * from students where name like '黄_';
            3, 查询姓"黄"或名叫"靖"
                select * from students where name like '黄%' or '%靖';

4- 范围查询:
    1, between... and ...表示在一个连续的范围的查询
    2, in 表示在一个非连续的范围内查询
        例: 1, 查询编号 3-8
                select * from students where not(id between 3 and 8);
            2, 查询编号3, 5, 7
                select * from students where id in (3, 5, 7);
            3, 查询编号不是3, 5, 7
                select * from students where id not in (3, 5, 7);


5- 空判断查询:
    1, 判断为空: is null
    2, 判断非空: is not null
        例: 1, 查询没有填写身高的学生
                select * from students where height is not null;


'''