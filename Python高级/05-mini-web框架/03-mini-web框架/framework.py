import pymysql
import json

# 装饰器路由列表
decorator_route_list = []


def decorator_route(page_name):
    def out(func):
        page_path = page_name
        decorator_route_list.append((page_path, func))

        def inner():
            status, header, data = func()
            return status, header, data

        return inner

    return out


@decorator_route("/login.html")
def login():
    lg_status = "200 OK"
    lg_header = [("Server", "PWS/1,1")]
    with open("static/login.html", "r", encoding="utf-8") as file:
        page_data = file.read()

    return lg_status, lg_header, page_data


def index():
    index_status = "200 OK"
    index_header = [("Server", "PWS/1.1")]
    with open("static/index.html", "r", encoding="utf-8") as file:
        page_data = file.read()

        # 从数据库填入数据
        cn_sql = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="111111",
            database="stock_db",
            charset="utf8"
        )
        cursor = cn_sql.cursor()
        sql_command = "select * from info;"
        cursor.execute(sql_command)
        sql_data = cursor.fetchall()

        # 关闭游标,链接
        cursor.close()
        cn_sql.close()
        # 替换html中的数据标签
        # 一对双引号不可以换行, 3对可以换行
        replace_data = ""
        for i in sql_data:
            replace_data += """
            <tr>
                        <th>%s</th>
                        <th>%s</th>
                        <th>%s</th>
                        <th>%s</th>
                        <th>%s</th>
                        <th>%s(元)</th>
                        <th>%s</th>
                        <th>%s</th>
                        <th>
                            <input name='toAdd' stockId="%s" type="submit" value="添加">
                        </th>
                        
            </tr>
            """ % (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[1])

            # print(i)
        # print(replace_data)
    page_data = page_data.replace("{%content%}", replace_data)

    return index_status, index_header, page_data


def error():
    error_status = "404 Not Found"
    error_header = [("Server", "PWS/1.1")]
    with open("static/error.html", "r", encoding="utf-8") as file:
        page_data = file.read()

    return error_status, error_header, page_data


def center():
    ct_status = "200 OK"
    ct_header = [("Server", "PWS/1.1")]
    with open("static/center.html", "r", encoding="utf-8") as file:
        page_data = file.read()
    return ct_status, ct_header, page_data


def center_css():
    ctc_status = "200 OK"
    ctc_header = [("Server", "PWS/1.1"), ("Content-Type", "text/css")]
    with open("static/css/center.css", "r", encoding="utf-8") as file:
        page_data = file.read()
    return ctc_status, ctc_header, page_data


@decorator_route("/css/bootstrap.min.css")
def bm_css():
    ctc_status = "200 OK"
    ctc_header = [("Server", "PWS/1.1"), ("Content-Type", "text/css")]
    with open("static/css/bootstrap.min.css", "r", encoding="utf-8") as file:
        page_data = file.read()
    return ctc_status, ctc_header, page_data


@decorator_route("/center_data.html")
def center_data():
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="111111",
        database="stock_db",
        charset="utf8"
    )
    cursor = conn.cursor()
    command = "SELECT a.`code`, a.short, a.chg, a.turnover, a.price, a.highs, a.remarks from (SELECT i.`code`, " \
              "i.short, i.chg, i.turnover, i.price, i.highs, c.remarks, c.del_sign FROM center_data c left JOIN info " \
              "i on c.stock_id = i.`code`) a WHERE a.del_sign = 0; "
    cursor.execute(command)
    result = cursor.fetchall()
    # print(result)

    # 推导式元组转字典
    data_list = [{
        "code": i[0],
        "short": str(i[1]),
        "chg": i[2],
        "turnover": i[3],
        "price": str(i[4]),
        "highs": str(i[5]),
        "note_info": i[6]
    } for i in result]
    # JSON包转JSON格式数据, ensure_ascii=False控制台不以ascii编码
    json_data = json.dumps(data_list, ensure_ascii=False)

    cursor.close()
    conn.close()

    cd_status = "200 OK"
    cd_header = [("Server", "PWS/1.1")]

    return cd_status, cd_header, json_data


# 装饰器在加载模块的时候会执行
# 装饰器的inner函数在调用时才会执行
@decorator_route("/grand.html")  # grand <= inner <= out(grand) <= decorate_route("grand")
def grand():
    gd_status = "200 OK"
    gd_header = [("Server", "PWS/1.1")]
    with open("static/grand.html", "r", encoding="utf-8") as file:
        page_data = file.read()
    return gd_status, gd_header, page_data


route_list = [
    ("/index.html", index),
    ("/center.html", center),
    ("/css/center.css", center_css)
]


def handle_request(env):
    request_path = env["request_data_path"]
    print("动态资源请求: " + request_path)
    for path, func in decorator_route_list:
        if request_path == path:
            # print(path, func)
            return func()
    else:
        for path, func in route_list:
            if request_path == path:
                return func()
        else:
            return error()


def write_data(data):
    con_sql = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="111111",
        database="stock_db",
        charset="utf8"
    )
    cursor = con_sql.cursor()
    select_command = "select stock_id from center_data;"
    cursor.execute(select_command)
    result = cursor.fetchall()
    for i in result:
        if i[0] == data["StockId"]:
            try:
                update_command = "UPDATE center_data SET del_sign = 0 WHERE stock_id = %s;"
                cursor.execute(update_command, data["StockId"])
                con_sql.commit()
            except Exception as e:
                print(e)
                # 失败回滚
                con_sql.rollback()
            finally:
                cursor.close()
                con_sql.close()
                return
    else:
        insert_command = "insert into center_data VALUES(%s, default, default);"
        try:
            cursor.execute(insert_command, data["StockId"])
            # 修改数据都要提交事务
            con_sql.commit()
            print("添加数据: ", data)

        except Exception as e:
            print(e)
            # 失败回滚
            con_sql.rollback()
        finally:
            cursor.close()
            con_sql.close()


def del_data(data):
    con_sql = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="111111",
        database="stock_db",
        charset="utf8"
    )
    cursor = con_sql.cursor()
    command = "UPDATE center_data SET del_sign = 1 WHERE stock_id = %s;"
    try:
        cursor.execute(command, data["StockId"])
        # 修改数据都要提交事务
        con_sql.commit()
        print("删除数据: ", data)
    except Exception as e:
        print(e)
        # 失败回滚
        con_sql.rollback()
    finally:
        cursor.close()
        con_sql.close()


if __name__ == '__main__':
    write_data()
