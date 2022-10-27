'''
1, GET方式请求报文: 获取web服务器数据
2, POST方式请求报文: 向web服务器提交数据

3, ---http get请求报文

    ----请求行----
    GET / HTTP/1.1(\r\n) -> 请求方法(方式) 请求资源路径 http协议版本
    ---请求头---
    Host: www.sogou.com(\r\n) -> 服务器的主机IP地址和端口号, 看不见端口号默认是88
    Connection: keep-alive(\r\n) -> 和服务器保持长链接, 当客户端喝服务器有一段时间(3~5分钟)没有通信,服务器会主动断开连接
    Cache-Control: max-age=0(\r\n) ->
    Upgrade-Insecure-Requests: 1(\r\n) -> 让客户端请求不安全请求, 以后要用https
    User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36
    (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0(\r\n) -> 用户代理, 客户端程序名称
    Sec-Fetch-Dest: document(\r\n)
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9(\r\n)
    Sec-Fetch-Site: same-origin(\r\n)
    Sec-Fetch-Mode: navigate(\r\n)
    Sec-Fetch-User: ?1(\r\n)
    Referer: https://www.sogou.com/link?url=hedJjaC291OpGPpITUxm9xvx9Yiptv-_(\r\n)
    Accept-Encoding: gzip, deflate, br(\r\n) -> 服务端程序支持的压缩算法
    Accept-Language: zh-CN,zh;q=0.9(\r\n) -> 服务端程序支持的语言
    Cookie: SUV=00DE4C6271482DD35F51DCDB9FBFB036; SUID=D32D48713020910A000000005F51DE53; pgv_pvi=6246173696; ssuid=7632658812;
    tv_play_records=tvshow_2089318:20201111:20201112; wuid=AAHSGTbqMwAAAAqHSCnW5AAAkwA=; SGINPUT_UPSCREEN=1631941600186; osV=1;
    browerV=8; sw_uuid=4777851904; IPLOC=CN4406; YYID=AEE0B293414FD6880E0FDFE967BCD8B0; ABTEST=0|1657809044|v17;
    ad=Qm2yTyllll2AZ9S3lllllpazpUZllllltUkHAlllll9lllllVklll5@@@@@@@@@@; SNUID=0563033B4B4EAEBA8D81517B4B11EC6D;
    ld=bZllllllll2KUNiFgTrk3uaOQySKWml$tUkH1Zllllolllll4klll5@@@@@@@@@@; sst0=37; LSTMV=309%2C193; LCLKINT=2088(\r\n) -> 客户端用户身份的标识
    ---空行---
    \r\n

提示: 每项信息后面都有\r\n自动隐藏

4, ---http get请求报文格式---
    请求行\r\n
    请求头\r\n
    空行\r\n

    ---http post请求报文格式---
    请求行\r\n
    请求头\r\n
    空行\r\n
    请求体

    提示: 请求体就是服务器向浏览器发送的数据


'''