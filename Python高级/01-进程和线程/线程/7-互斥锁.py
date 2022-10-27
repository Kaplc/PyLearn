import threading
import time

g_num = 0

def add_1():
    lock.acquire()  # 上锁
    global g_num
    for i in range(10000000):
        g_num += 1
    print('add1', g_num)
    lock.release()  # 解锁

def add_2():
    lock.acquire()
    global g_num
    for i in range(10000000):
        g_num += 1
    print('add2:', g_num)
    lock.release()
if __name__ == '__main__':
    # 创建互斥锁
    lock = threading.Lock()

    add_1_thread = threading.Thread(target=add_1)
    add_2_thread = threading.Thread(target=add_2)

    add_1_thread.start()
    add_2_thread.start()
    time.sleep(5)
    print(g_num)

# 上锁可以让一个线程锁定全局变量先使用,其他线程等待, 使用完释放后其他线程才能使用和上锁