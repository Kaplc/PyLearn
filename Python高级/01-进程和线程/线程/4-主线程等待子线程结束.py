import threading
import time

def sub():
    for i in range(10):
        print(i)
        time.sleep(0.2)

if __name__ == '__main__':
    sub_process = threading.Thread(target=sub)

    # 方法一, 设置子线程为守护线程, 主线程结束子线程就销毁
    sub_process.daemon = True

    sub_process.start()
    time.sleep(0.5)

    # 方法二, 主线程结束前销毁子线程
    sub_process.terminate()
    print('over')

# 子线程结束主线程才能结束