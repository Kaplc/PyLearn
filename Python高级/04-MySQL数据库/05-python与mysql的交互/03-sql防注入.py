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

    sql = "select id, name, age, gender from students where id in (%s, %s, %s);"
    try:
        # sql参数化防止注入
        cursor.execute(sql, (3, 5, 7))

        connect.commit()

    except Exception as e:
        connect.rollback()
    finally:

        # row = cursor.fetchone()
        # print(row)
        result = cursor.fetchall()
        for i in result:
            print(i)

        cursor.close()

        connect.close()
