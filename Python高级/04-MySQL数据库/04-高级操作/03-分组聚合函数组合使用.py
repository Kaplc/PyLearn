"""
1- 查询类型cate_name为'超极本' 的商品名称,价格
    select name, price from goods where cate_name = '超极本';

2- 显示商品分类
    select distinct cate_name from goods;
    select cate_name from goods group by cate_name;

3- 求所有电脑产品的平均价格, 并且保留2位小数
    select round(avg(price),2) from goods;

4- 显示每种商品的平均价格
    select cate_name, avg(price) from goods group by cate_name;
    select cate_name, round(avg(price), 2) from goods group by cate_name;

5- 查询每种类型的商品中最贵, 最便宜, 平均价, 数量
    select cate_name, max(price), min(price), avg(price), count(*) from goods group by cate_name;

6- 查询所有价格大于平均价格的商品, 并且按照价格降序排序
    select * from goods where price > (select avg(price) from goods) order by price desc;


"""