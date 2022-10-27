__all__ = ['testA'] # 限制from 模块名 import * 导入方式,只能导入__all__列表的方法

def testA(a, b):
    return a + b


def testB(a, b):
    return a * b


if __name__ == '__main__': # 在本文件运行__name__的值为__main,即可规避在另外的py文件执行测试代码
    print(testA(1, 2))
