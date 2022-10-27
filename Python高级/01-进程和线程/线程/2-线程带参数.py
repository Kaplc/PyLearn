import threading

def show_args(name, age):
    print(f'姓名:{name}, 年龄:{age}')

def show_kwargs(name, age):
    print(f'姓名:{name}, 年龄:{age}')

def show_args_and_kwargs(name, age):
    print(f'姓名:{name}, 年龄:{age}')


if __name__ == '__main__':
    show_args_process = threading.Thread(target=show_args, args=('张三', 20))
    show_kwargs_process = threading.Thread(target=show_args, kwargs={'name': '张三' , 'age': 21})
    # 元组和字典结合传参,第一个参数是元组
    show_args_and_kwargs_process = threading.Thread(target=show_args, args=('张三',), kwargs={'age': 22})

    show_args_process.start()
    show_kwargs_process.start()
    show_args_and_kwargs_process.start()