"""
1- 日志等级可以分为5个，从低到高分别是:
    DEBUG
    INFO
    WARNING(默认大于warning才提示)
    ERROR
    CRITICAL

2- 在 logging 包中记录日志的方式有两种:

    1, 输出到控制台
    2, 保存到日志文件

"""
# 导包
import logging


# 控制台显示
def logging_console():
    logging.debug('这是一个debug级别的日志信息')
    logging.info('这是一个info级别的日志信息')
    logging.warning('这是一个warning级别的日志信息')
    logging.error('这是一个error级别的日志信息')
    logging.critical('这是一个critical级别的日志信息')


# 文件显示
"""
    1, level 表示设置的日志等级
    2, format 表示日志的输出格式, 参数说明: %(levelname)s: 打印日志级别名称
                                    %(filename)s: 打印当前执行程序名
                                    %(lineno)d: 打印日志的当前行号
                                    %(asctime)s: 打印日志的时间
                                    %(message)s: 打印日志信息
    3, filename="logging.word": 保存的文件名
    4, filemode="w": 文件的读写格式
"""


def logging_file():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s: in %(filename)s[line:%(lineno)d] %(levelname)s: %(message)s',
        filename="logging.txt",
        filemode="w", encoding="utf-8"
    )

    logging.debug('这是一个debug级别的日志信息')
    logging.info('这是一个info级别的日志信息')
    logging.warning('这是一个warning级别的日志信息')
    logging.error('这是一个error级别的日志信息')
    logging.critical('这是一个critical级别的日志信息')


if __name__ == '__main__':
    logging_file()
