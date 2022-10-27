"""
1-  由于文件读写时都有可能产生IOError，一旦出错，后面的 f.close()就不会调用。
    为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来解决
    with 语句执行完成以后自动调用关闭文件操作，即使出现异常也会自动调用关闭文件操作

"""


def misspellings():
    f = open('../03-mini-web框架/logging.txt', "w")
    f.write("hello world")
    # 以上代码出错下面关闭文件代码不会执行, 有风险
    f.close()


def safe_writing():
    # 即使出错也可以保证文件关闭
    try:
        file_safety = open('../03-mini-web框架/logging.txt', "w")
        file_safety.write("hello world")
    except Exception as e:
        print(e)
    finally:
        file_safety.close()


def with_sentence():
    # 等效try方式打开文件, 即使出错也可以保证文件关闭
    with open("1.txt", "w") as file_with:
        file_with.write("hello world")

