# 1-导包
import pymysql

if __name__ == '__main__':
    # 2-创建链接对象
    connect = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="111111",
        database="pylearn",
        charset="utf8"
    )
    # 3-获取游标(相当于传输介媒)
    cursor = connect.cursor()
    # 4-执行sql语句
    sql = "select * from students;"
    cursor.execute(sql)
    # 5-获取结果, 都是元组类型
    row = cursor.fetchone()  # 获取单条数据
    print(row)
    result = cursor.fetchall() # 获取多条数据
    print(result)
    # 6-关闭游标
    cursor.close()
    # 7-关闭链接
    connect.close()

