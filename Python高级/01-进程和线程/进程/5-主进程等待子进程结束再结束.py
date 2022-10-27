import multiprocessing
import time

def sub():
    for i in range(10):
        print(i)
        time.sleep(0.2)

if __name__ == '__main__':
    sub_process = multiprocessing.Process(target=sub)

    # 方法一, 设置子进程为守护进程, 主进程结束子进程就销毁
    sub_process.daemon = True

    sub_process.start()
    time.sleep(0.5)

    print('over')

# 子进程结束主进程才能结束