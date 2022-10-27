'''
1, ---http 响应报文

    ---响应行(状态行)---
    HTTP/1.1 200 OK(\r\n) -> http协议版本 状态码 状态描述
    ---响应头---
    Server: nginx(\r\n) -> 服务器名称
    Date: Sat, 30 Jul 2022 16:15:19 GMT(\r\n)  -> 服务器的时间
    Content-Type: text/html; charset=utf-8(\r\n) -> 服务器发送给浏览器的内容类型及编码格式
    Transfer-Encoding: chunked(\r\n) -> 服务器发送给浏览器的数据不确定数据长度, 数据发送结束的接收标识, 若Transfer-Encoding: 200 则发送确定长度的数据
    Connection: keep-alive(\r\n) -> 和客户端保持长链接
    ---以下是自定义的头响应头信息
    Vary: Accept-Encoding(\r\n)
    Set-Cookie: black_passportid=; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT; domain=.sogou.com(\r\n)
    Pragma: No-cache(\r\n)
    Cache-Control: max-age=0(\r\n)
    Expires: Sat, 30 Jul 2022 16:15:19 GMT(\r\n)
    UUID: 15eafbc0-9562-4df7-94a6-ef18d9eafed8(\r\n)
    Content-Encoding: gzip(\r\n)
    ---空行---
    \r\n
    ---响应体---
    网页数据

2, ---http响应报文格式---
    响应行(\r\n)
    响应头(\r\n)
    空行(\r\n)
    响应体(\r\n)


'''