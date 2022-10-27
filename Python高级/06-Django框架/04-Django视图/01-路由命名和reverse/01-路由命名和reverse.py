"""

1- 路由命名
    1) 在使用include函数(在项目urls.py)定义路由时，可以使用namespace参数定义路由的命名空间
        路由别名: namespace='book'
        命名空间表示，凡是book.urls中定义的路由，均属于namespace指明的book名下
        re_path(r'^',include('book.urls',namespace='book'))

    2) 在定义普通路由(在子应用urls.py)时，可以使用name参数指明路由的名字
        re_path(r'^view$', index, name='view_index')

2- reverse动态获取路由: 使用reverse函数，可以根据路由名称，返回具体的路径

    语法: 对于未指明namespace的，reverse(name)
        对于指明namespace的，reverse(namespace:name)
    path = reverse(view_index)
    path = reverse('book: index')

"""