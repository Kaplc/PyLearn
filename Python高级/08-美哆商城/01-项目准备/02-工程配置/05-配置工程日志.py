"""
1- 配置工程日志
    在setting.py下

2- 创建日志文件目录
    os.path.dirname(BASE_DIR): 表示BASE_DIR的父级目录

3- 测试日记记录器
    import logging
    # 创建日志记录器
    logger = logging.getLogger('django')
    # 输出日志
    logger.debug('测试logging模块debug')
    logger.info('测试logging模块info')
    logger.error('测试logging模块error')

4- 取消跟踪log文件仅跟踪文件目录的git配置
    git不允许储存空目录, 要在目录创建.gitkeep文件


"""
