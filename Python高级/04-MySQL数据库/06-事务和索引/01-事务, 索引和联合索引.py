"""
1- mysql默认修改数据自动开启事务(insert, update, delete)

2- 修改数据后要提交才写入数据库才能被其他用户查看

3- 事务开启: begin和start transaction

4- 索引: 消耗磁盘空间, 提升查询性能

5- 添加索引: alter table students add index(name); -- 给students表的name字段添加索引

6- 联合索引: alter table students add index(name, age); -- 多个字段使用一个索引, 查询时只有最左边的字段有索引功能

7- 适用范围: 1) 查询次数多修改少的字段 2)不同值较多时 3) 数据量大

"""
