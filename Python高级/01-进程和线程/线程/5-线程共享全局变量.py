import threading

# 列表全局变量
g_list = []

def add():
    for i in range(10):
        g_list.append(i)
        print('add:', g_list)
def read():
    print('read:', g_list)

if __name__ == '__main__':
    add_thread = threading.Thread(target=add)
    read_thread = threading.Thread(target=read)

    add_thread.start()

    # 等待该线程结束再下一步
    add_thread.join()

    read_thread.start()
