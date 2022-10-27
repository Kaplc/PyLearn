'''
1, 创建服务器socket
2, 绑定端口号
3, 设置监听
4, 等待接收客户端的链接请求
5, 接收数据
6, 发送数据
7, 关闭套接字

'''

import socket
import threading

def get_host_ip():
    """
    查询本机ip地址
    :return:
    """
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('8.8.8.8',80))
        ip=s.getsockname()[0]
    finally:
        s.close()

    return ip

def tcp_server_socket_function(new_socket, ip_port):
    # 接收ip地址
    ip_data, port_number = ip_port
    print('客户端ip:', ip_data, '已连接')
    while True: # 重复发送接收
        # 最大接收1024字节数据
        recv_endata = new_socket.recv(1024)
        if recv_endata: # 判断读取的数据是否为0, 0为客户端已断开

            # 接收的数据解码成utf-8
            recv_dedata = recv_endata.decode('utf-8')
            print(f'客户端({ip_data}): {recv_dedata}')

            send_dedata = input('本机: ')
            # 数据转码成utf-8发送
            send_endata = send_dedata.encode('utf-8')
            # 发送
            new_socket.send(send_endata)

        else:
            print(f'{ip_data}已下线')
            print('-----------')
            break
    # 关闭链接
    new_socket.close()

if __name__ == '__main__':
    print('服务器已启动,ip:', get_host_ip())

    # 创建socket
    # AF_INET: ipv4类型地址
    # SOCK_STREAM: tcp协议
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 设置端口复用, 否则退出程序要1~3分钟才释放端口号
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    # 设置服务器ip和端口号
    tcp_server_socket.bind(('', 8080))

    # 设置最大接收请求数
    tcp_server_socket.listen(128)

    while True: # 保持接收请求
        # 接收请求, 同时创建新socket链接每个客户端, 返回socket和ip, 端口号
        new_socket, ip_port = tcp_server_socket.accept()

        # 多线程服务多客户端
        tcp_server_thread = threading.Thread(target=tcp_server_socket_function, args=(new_socket, ip_port))
        tcp_server_thread.start()

