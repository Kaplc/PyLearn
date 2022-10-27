'''
1- 查询所有列数据
    select * from 表名;

2- 查询指定列数据
    select 列名, ... from 表名;

3- 添加数据
    全列插入: insert into 表名 values(0, ..., default);
        主键0是不指定系统自动分配
        default是默认值
        null为空
    部分列插入: insert into 表名(列名, ...) values(数据, ...);
        没有填写的数据自动填写默认值
    全列多行插入: insert into 表名 values(数据, ...), (数据, ...);
    部分列多行插入: insert into 表名(列名, ...) values(数据, ...), (数据, ...);

4- 修改数据
    update 表名 set 列名=新数据, ... where 定位列名=定位数据;

5- 删除数据
    delete from 表名 where 定位列名=定位数据;

    通常进行逻辑删除而不真正删除数据
    1, 创建新字段标识是否删除
    2, 将删除的数据在删除字段标识出来
    alter table students add is_del tinyint default 0;
    update students set is_del = 1 where id = 2;
'''