"""
cookie流程:
    首次访问:
        1, 浏览器没有携带cookie信息访问服务器
        2, 服务器检测到没有cookie
        3, 返回响应的时候携带cookie

    以后访问:
        1, 有cookie信息后每次请求都会带有cookie
        2, 服务器检测cookie识别身份



cookie特点:
    1, 键值对储存
    2, 基于域名, 不同域名不能互相访问


1- 设置cookie


"""
