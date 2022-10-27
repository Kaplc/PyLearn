import threading

def dance():
    for i in range(10):
        print('dancing...')

def sing():
    for i in range(10):
        print('singing...')

if __name__ == '__main__':
    # 创建线程
    sing_thread = threading.Thread(target=sing)
    dance_thread = threading.Thread(target=dance)

    sing_thread.start()
    dance_thread.start()
    # 线程执行也是无序
