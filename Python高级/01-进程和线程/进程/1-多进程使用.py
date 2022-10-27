# 导包
import multiprocessing

'''
Process进程类说明

Process([group [, target [, name [, args [, kwargs]]]]])
group: 指定进程组,目前只能None
target: 执行目标任务名
name: 进程名字
args: 元组形式传参
kwargs: 字典形式传参

实例对象常用方法:
star(): 创建子进程
join(): 等待子进程执行结果
terminate(): 终止子进程

实例对象常用属性:
name: 当前进程名,默认Process-N N从1开始

'''
def dance():
    for i in range(10):
        print('dancing...')

def sing():
    for i in range(10):
        print('singing...')

if __name__ == '__main__':
    dance_process = multiprocessing.Process(target=dance)
    sing_process = multiprocessing.Process(target=sing)

    dance_process.start()
    sing_process.start()
# 进程执行顺序是无序的