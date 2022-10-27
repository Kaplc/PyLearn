'''
1, 创建客户端socket对象
2, 和服务端socket链接
3, 发送数据
4, 接收数据
5, 关闭客户端socket

'''

import socket


if __name__ == '__main__':
    # 创建socket
    # AF_INET: ipv4类型地址
    # SOCK_STREAM: tcp协议
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 用socket链接的ip和端口号
    tcp_client_socket.connect(('192.168.1.6', 8080))
    print('链接成功!')
    while True: # 重复发送读取

        send_content = input('本机: ')

        if send_content == 'esc':
            # 输入esc关闭socket,并退出循环
            tcp_client_socket.close()
            break

        # 转码成utf-8发送
        send_data = send_content.encode('utf-8')
        tcp_client_socket.send(send_data)

        # 每次接收最大1024个字节的数据
        recv_data = tcp_client_socket.recv(1024)
        # 接收并转码成utf-8
        recv_dedata = recv_data.decode('utf-8')
        print('客户端: ', recv_dedata)


