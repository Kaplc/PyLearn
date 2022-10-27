# 目的:知道进程的父子关系
# os.getpid(): 读取当前进程编号
# os.getppid(): 获取父进程编号
import multiprocessing
import time
import os

def dance():
    # 获取当前子进程编号
    print(f'dance子进程编号: {os.getpid()}')
    # 获取dance父进程编号
    print(f'dance父进程编号: {os.getppid()}')

    for i in range(10):
        print('dancing...')


def sing():
    # 获取当前子进程编号
    print(f'sing子进程编号: {os.getpid()}')
    # 获取sing父进程编号
    print(f'sing父进程编号: {os.getppid()}')

    for i in range(10):
        print('singing...')




if __name__ == '__main__':
    # 获取当前主进程编号
    print(f'主进程编号: {os.getpid()}')


    dance_process = multiprocessing.Process(target=dance)
    sing_process = multiprocessing.Process(target=sing)

    dance_process.start()
    sing_process.start()

