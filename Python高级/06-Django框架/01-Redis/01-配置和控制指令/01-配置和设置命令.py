"""

                             Redis 配置

    1- 配置文件位置: Redis的配置信息在/etc/redis/redis.conf下

    2- 核心配置选项:
        绑定ip：bind 127.0.0.1 (如果需要远程访问，可将此⾏注释，或绑定⼀个真实ip)

        端⼝: port 6379 (默认为6379)

        是否以守护进程运⾏: daemonize yes

            (如果以守护进程运⾏，则不会在命令⾏阻塞，类似于服务
            如果以⾮守护进程运⾏，则当前终端被阻塞
            设置为yes表示守护进程，设置为no表示⾮守护进程
            推荐设置为yes)

        数据⽂件: dbfilename dump.rdb

        数据⽂件存储路径: dir /var/lib/redis

        ⽇志⽂件: logfile "/var/log/redis/redis-server.log"

        数据库，默认有16个: database 16

        主从复制，类似于双机备份: slaveof

                          服务端和客户端命令

    1- 运⾏测试命令: ping

    2- help查看帮助⽂档: redis-server --help

    3- 指定加载的配置文件: redis-server /etc/redis/redis.conf



"""
