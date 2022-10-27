'''
0- 清屏
    system clear;
1- 聚合函数
    1) count(列): 指定列的总行数
    2) max(col): 最大值
    3) min(col): 最小值
    4) sum(col): 求和
    5) avg(col): 平均数
    例: 1, 查询学生个数
            select count(height) from students;
            通用写法不指定字段:
            select count(*) from students;
            不会对 null 进行统计 !!!
        2, 查询女生编号最大值
            select max(id) from students where gender= "女";
        3, 查询未删除学生最小编号
            select min(id) from students where is_del= 0;
        4, 男生总身高
            select sum(height) from students where gender= "男";
        5, 男生平均身高
            null忽略:
                select avg(height) from students where gender= "男";
            null算0:
                select sum(height)/ count(*) from students where gender= "男";
                select avg(ifnull (height, 0)) from students where gender= "男";

                ifnull: 如果为null, 使用默认值0;

2- 分组查询
    1) group by 列名: 按照列名分组
    2) having: 过滤分组后的数据
    3) with rollup: 显示统计结果
    4) group_concat(col): 统计分组完成后根据字段名信息集合
    例: 1, 查询性别种类
            select gender from students group by gender;
        2, 根据name和gender分组, 并查看分组信息
            select name, gender from students group by name, gender;
        3, 根据gender分组, 并查看分组的姓名信息
            select gender, group_concat(name) from students group by gender;
        4, 统计不同性别的平均年龄
            select gender, avg(age) from students group by gender;
        5, 统计不同性别人的个数
            select gender, count(*) from students group by gender;
        6, 根据gender分组, 统计分组条数大于2
            select gender, count(*) from students group by gender having count(*) > 2;
        7, 根据gender分组, 汇总总人数
            select gender, count(*) from students group by gender with rollup;
        8, 根据gender分组, 汇总所有人年龄
            select gender, group_concat(age) from students group by gender with rollup;





'''