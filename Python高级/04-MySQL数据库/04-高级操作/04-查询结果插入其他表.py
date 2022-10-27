"""
1- 创建商品分类表
    create table good_cate(
        id int not null primary key auto_increment,
        name varchar(50) not null
    );

2- 查询结果插入新表
    insert into goods_cate(name) select cate_name from goods group by cate_name;

"""