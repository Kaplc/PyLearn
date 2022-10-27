import socket
import threading
import framework


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

    def server_star(self):
        while True:
            # 接收请求,创建新socket
            new_socket, ip_port = self.tcp_server_socket.accept()
            # 多线程
            server_threading = threading.Thread(target=self.server, args=(new_socket,), daemon=True)
            server_threading.start()

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
        rec_data_list_space = recv_data.split(' ', 2)
        request_path = rec_data_list_space[1]

        # 接收网页数据
        rec_data_list_rn = recv_data.split('\r\n\r\n', 2)
        # 网页数据非空执行写入数据库
        if rec_data_list_rn[len(rec_data_list_rn) - 1]:
            # 列表转字典
            dict_data = {}
            print(rec_data_list_rn[1])
            new_list = rec_data_list_rn[1].split('&')
            for i in new_list:
                key, val = i.split('=')
                dict_data[key] = val
            # print(write_data)
            if dict_data['requestType'] == 'add':
                framework.write_data(dict_data)
            elif dict_data['requestType'] == 'del':
                framework.del_data(dict_data)

        # 设置接收无路径时'/'打开首页
        if request_path == '/':
            request_path = '/index.html'

        # 判断动态资源请求
        if request_path.endswith(".html") or request_path.endswith(".css"):
            # 发送给web框架的信息用字典封装
            env = {
                "request_data_path": request_path
            }
            # env发送给框架返回响应状态
            status, headers, response_body = framework.handle_request(env)
            # 格式化输入
            response_line = "HTTP/1.1 %s\r\n" % status

            response_header = ""
            # 响应头有多行每一行一个元组保存在列表里, 取出要遍历列表
            for i in headers:
                response_header += "%s: %s\r\n" % i

            response = (response_line + response_header + '\r\n' + response_body).encode('utf-8')
            new_socket.send(response)
            new_socket.close()
        else:
            # 尝试查找对应资源, 找不到报错并返回 404 页面
            print("静态资源请求:" + 'static' + request_path)
            try:
                with open('static' + request_path, 'rb') as file:
                    file_data = file.read()
            except Exception as e:
                print(e)
            finally:
                # 响应行
                response_line = 'HTTP/1.1 200 OK\r\n'
                # 响应头
                response_header = 'Server: PWS/1.1\r\n'
                # # 响应体
                response_body = file_data
                # 打包所有数据为二进制发送
                response = (response_line + response_header + '\r\n').encode('utf-8') + response_body

                new_socket.send(response)
                new_socket.close()


if __name__ == '__main__':
    web_server = HttpWebServer()
    web_server.server_star()
