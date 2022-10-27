"""
1- with语句实际上是个上下文管理器
2- 使用上下文管理器自动执行__enter__, __exit__方法

"""


# 自定义模拟with语句
# 实现方法一:
class File(object):
    def __init__(self, file_name, file_model):
        self.file_name = file_name
        self.file_model = file_model

    # 定义上文方法: __enter__表示上文方法，需要返回一个操作文件对象
    def __enter__(self):
        print("进入上文方法")

        self.file = open(self.file_name, self.file_model)
        return self.file

    # 定义下文方法: __exit__表示下文方法，with语句执行完成会自动执行，即使出现异常也会执行该方法
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("进入下文方法")
        self.file.close()


# 实现方法二(装饰器装饰函数):
from contextlib import contextmanager


@contextmanager
def my_open(path, model):
    try:
        print("进入上文方法")
        file_safety = open(path, model)
        file_data = file_safety.read()
        print(file_data)

        # yield前面是上文方法, 后面是下文方法
        # yield 后面的参数是函数的返回值
        yield file_safety

    except Exception as e:
        print(e)

    finally:
        print("进入下文方法")
        file_safety.close()


if __name__ == '__main__':
    # 方法一:不用创建实例
    # with File('../03-mini-web框架/logging.txt', "w") as file:
    #     file_data_I = file.read()
    #     print(file_data_I)
    # 方法二:
    with my_open('../03-mini-web框架/logging.txt', "w") as file:
        file_data_II = file.read()
        print(file_data_II)
