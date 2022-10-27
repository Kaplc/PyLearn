"""
1- BASE_DIR
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    当前工程的根目录，Django会依此来定位工程内的相关文件，我们也可以使用该参数来构造文件路径
    1) __file__: 表示文件名字
    2) os.path.abspath(__file__): 获取文件的绝对路径
    3) os.path.dirname(): 路径的上一级
    os.path.join(BASE_DIR, 'templates')

    当前版本: Path(__file__).resolve().parent.parent
    # Path(__file__).resolve(): 获取当前文件的绝对路径
    # Path(__file__).resolve().parent: 获取当前文件的绝对路径上一级(父目录)
    # Path(__file__).resolve().parent.parent: 再上一级就是项目的根目录

2- DJango的DEBUG模式(在setting.py)
    DEBUG = True
    创建工程后初始值为True:
        1) 修改代码文件，程序自动重启
        2) Django程序出现异常时，向前端显示详细的错误追踪信息
        3) 而非调试模式下，仅返回Server Error (500)

    注意: 部署线上运行的Django不要运行在调式模式下，记得修改DEBUG=False和ALLOW_HOSTS

3- 静态文件
    CSS、图片、js都是静态文件需要创建目录来保存方便调用
    在项目根目录下，也可以放在应用的目录下，由于有些静态文件在项目中是通用的，所以推荐放在项目的根目录下，方便管理

    配置两个参数：
        STATICFILES_DIRS 存放查找静态文件的目录
        STATIC_URL 访问静态文件的URL前缀

4- 修改在admin子应用显示的名称: verbose_name = '书籍'
"""