import socket
import threading


class HttpWebServer(object):
    def __init__(self):
        # 创建web服务器套接字
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 端口复用
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 指定服务器端口号
        tcp_server_socket.bind(('', 80))
        # 设置服务器最大等待数
        tcp_server_socket.listen(128)
        # 把tcp服务器的socket作为属性
        self.tcp_server_socket = tcp_server_socket

    @staticmethod
    def server(new_socket):
        # 接收4096字节数据并转码
        recv_data = new_socket.recv(4096).decode('utf-8')
        # print(recv_data)

        # 判断接收的数据是否为空, 防止一直占用资源
        if len(recv_data) == 0:
            new_socket.close()
            return

        # 接收的是请求报文, 空格分割取出请求的资源路径
        request_data_list = recv_data.split(' ', 2)
        request_data = request_data_list[1]
        print(request_data)
        # 设置接收无路径时'/'打开首页
        if request_data == '/':
            request_data = '/index.html'

        # 尝试查找对应资源, 找不到报错并返回 404 页面
        try:
            with open('static' + request_data, 'rb') as file:
                file_data = file.read()
        except FileNotFoundError:
            with open('static/error.html', 'rb') as file:
                file_data = file.read()
        finally:
            # 响应行
            response_line = 'HTTP/1.1 200 OK\r\n'
            # 响应头
            response_header = 'Server: PWS/1.0\r\n'
            # 响应体
            response_body = file_data
            # 打包所有数据为二进制发送
            response = (response_line + response_header + '\r\n').encode('utf-8') + response_body
            new_socket.send(response)

        new_socket.close()

    def server_star(self):
        while True:
            # 接收请求,创建新socket
            new_socket, ip_port = self.tcp_server_socket.accept()
            # 多线程
            server_threading = threading.Thread(target=self.server, args=(new_socket,), daemon=True)
            server_threading.start()


if __name__ == '__main__':
    web_server = HttpWebServer()
    web_server.server_star()
