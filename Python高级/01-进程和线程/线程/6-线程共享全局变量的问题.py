import threading
import time

g_num = 0

def add_1():
    global g_num
    for i in range(10000000):
        g_num += 1
    print('add1', g_num)

def add_2():
    global g_num
    for i in range(10000000):
        g_num += 1
    print('add2:', g_num)

if __name__ == '__main__':

    add_1_thread = threading.Thread(target=add_1)
    add_2_thread = threading.Thread(target=add_2)

    add_1_thread.start()

    # 可以加入线程等待解决
    add_1_thread.join()

    add_2_thread.start()
    time.sleep(0.2)
    print(g_num)

# 一个线程取值后还没有修改时第二个线程对全局变量取值成功, 导致重复加了一次所以总次数减少