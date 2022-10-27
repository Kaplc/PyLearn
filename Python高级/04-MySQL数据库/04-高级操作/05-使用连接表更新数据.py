"""
1- 连表查询然后更新有关联的字段
    update goods g inner join goods_cate gc on g.cate_name = gc.name set g.cate_name = gs.id;

"""