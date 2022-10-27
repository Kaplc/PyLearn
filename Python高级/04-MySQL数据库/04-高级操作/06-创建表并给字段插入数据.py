"""
1- 创建新表同时插入数据
    create table goods_brands(
        id int unsigned not null primary key auto_increment,
        name varchar(50) not null
    ) select brand_name as name from goods group by brand_name;



"""