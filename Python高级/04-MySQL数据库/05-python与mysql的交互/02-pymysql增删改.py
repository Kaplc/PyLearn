
import pymysql

if __name__ == '__main__':

    connect = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="111111",
        database="pylearn",
        charset="utf8"
    )

    cursor = connect.cursor()

    sql = "insert into classes(name) values('python');"
    # 可能出错使用try
    try:
        # 执行
        cursor.execute(sql)
        # 提交
        connect.commit()

    except Exception as e:
        connect.rollback()  # 失败回滚
    finally:

        row = cursor.fetchone()
        print(row)
        result = cursor.fetchall()
        print(result)

        cursor.close()

        connect.close()
