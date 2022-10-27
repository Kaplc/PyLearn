import multiprocessing

# 列表全局变量
g_list = []

def add():
    for i in range(10):
        g_list.append(i)
        print('add:', g_list)
def read():
    print('read:', g_list)

if __name__ == '__main__':
    add_process = multiprocessing.Process(target=add)
    read_process = multiprocessing.Process(target=read)

    add_process.start()
    read_process.start()

# 创建进程相当于拷贝主进程的所有资源,进程资源互不影响