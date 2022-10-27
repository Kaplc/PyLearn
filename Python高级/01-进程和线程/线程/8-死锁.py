import threading
import time

def get_value(index):
    lock.acquire()
    v_list = [1, 3, 5, 7]
    if index >= len(v_list):

        print('ss')
        return # 退出时未解锁, 导致上锁资源不能访问, 程序无限等待
    lock.release()
    print(index)

if __name__ == '__main__':
    lock = threading.Lock()

    for i in range(10):
        get_value_thread = threading.Thread(target=get_value, args=(i,))
        get_value_thread.start()


