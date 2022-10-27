'''
1- 排序
    1) 先按照1列进行排序, 若1列相同则按照2列, 以此类推
    2) asc 小到大, 升序
    3) desc 大到小, 降序
    4) 默认按照asc升序排序
    例: 1, 查询未删除的男生, 按照学号降序
            select * from students where is_del = 0 and gender = "男" order by id desc;
        2, 显示所有学生信息, 先按照年龄大到小, 相同按照身高高到矮
            select * from students order by age desc, height desc;

2- 分页查询
    limit (x, y) : x是开始索引默认是0, y是查询条数
    例: 1, 查询前3行男生信息
            select * from students where gender = "男" limit 0, 3; (0可以省略)
        2, 查询学生表, 获取第 n 页数据
            select * from students limit (n-1) * y, y;

'''