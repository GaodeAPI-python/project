from flask import Flask,render_template
from flask import json
from flask import request
from flask import make_response
import pymysql
from flask import jsonify
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://house:123456@localhost:3306/house'
# db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/index')
def map():
    return render_template('index.html')

# # 下载房源坐标的路由
# @app.route("/install",methods=["POST"])
# def install_locations():
#     # 下载房源坐标
#     data = request.json
#     data = json.dumps(data)
#     with open("location.json", "w") as f:
#         f.write(data)
#     return "done"


# 地图加载完毕后,自动向后台请求所有房源的坐标点
# 这个函数,通过pymsql查出所有数据返还给前端
@app.route("/location_all")
def location_all():
    # 返回所有房源坐标
    con = pymysql.connect(host="localhost", port=3306, database="house", user="house", password="123456", charset="utf8")
    cur = con.cursor()
    sql = "select id,x,y from house_info;"
    cur.execute(sql)
    location_data = cur.fetchall()
    cur.close()
    con.close()
    data = []
    for (id, x, y) in location_data:
        location = [x,y]
        info = {'id':id,'address':location}
        data.append(info)

        final_data = {'result':data}
    return jsonify(final_data)

#     con = pymysql.connect(host="localhost", port=3306, database="house", user="house", password="123456", charset="utf8")
#     cur = con.cursor()
#     sql = "select id,x,y from houseinfo;"
#     cur.execute(sql)
#     location_data = cur.fetchall()
#     cur.close()
#     con.close()
#     data = []
#     for (code, location) in location_data:
#
#         location = json.loads(location)
#         info = { "code":code, "address": location }
#         data.append(info)
#         final_data = {"result": data}
#         return jsonify(final_data)

# 当前端点击房源时,查询数据库返回基本信息
@app.route("/infor/<code>")
def sendinfor(code):
    # print(code)
    con = pymysql.connect(host="localhost", port=3306, database="house", user="house", password="123456", charset="utf8")
    cur = con.cursor()
    sql_all = 'select title,location,money,url from house_info where id = %s;' % code
    # sql_p = "select money from house_info where id = %s;"%code
    # cur.execute(sql_p)
    # price = cur.fetchone()
    # sql_h = "select title from house_info where id = %s;"%code
    # cur.execute(sql_h)
    # title = cur.fetchone()
    # sql_more = "select url from house_info where id = %s;"%code
    # cur.execute(sql_more)
    # more = cur.fetchone()
    cur.execute(sql_all)
    window_info = cur.fetchone()
    cur.close()
    con.close()
    # data = {"price": price[0], "img_src": title[0], "more_href": more[0]}
    data = {"title1":window_info[0], "location1":window_info[1], "money":window_info[2], "url1":window_info[3]}
    return jsonify(data)


#   登录
@app.route('/login')
def login():
    dic = request.args
    name = dic['name']
    pwd = dic['pwd']
    con = pymysql.connect(host="localhost", port=3306, database="house", user="house", password="123456", charset="utf8")
    cur = con.cursor()
    # print(name,type(name))
    # print(pwd, type(pwd))
    sql = "select name,pwd from userinfo where name='%s' and pwd='%s';" % (name, pwd)
    # print(sql) % (name, pwd)

    cur.execute(sql)
    result = cur.fetchall()
    # result = 'ads'
    print(result)
    # print(name,pwd)
    cur.close()
    con.close()
    return str(result)

#  验证
@app.route('/regist')
def yanzhen():
    con = pymysql.connect(host="localhost", port=3306, database="house", user="house", password="123456", charset="utf8")
    cur = con.cursor()
    dic = request.args
    try:
        register_pwd  = dic['register_pwd']
    except KeyError:
        register_name = dic['register_name']
        sql = 'select name from userinfo where name="%s";' % register_name
        cur.execute(sql)
        result = cur.fetchall()
        # print(str(result),type(result))
        res = make_response(str(result))
        return res
    else:
        register_name = dic['register_name']
        register_email = dic['register_email']
        sql_insert = "insert into userinfo (name,pwd,mail) values('%s','%s','%s');" % (register_name, register_pwd, register_email)
        cur.execute(sql_insert)
        con.commit()
        return 'ok'
    finally:
        cur.close()
        con.close()


@app.route('/code')
def mail_code():
    con = pymysql.connect(host="localhost", port=3306, database="house", user="house", password="123456", charset="utf8")
    cur = con.cursor()
    dic = request.args
    try:
        code = dic['code']
    except KeyError:
        mail = dic['mail']
        sql_select = "select code from code1 where mail='%s';" % mail#查找数据库
        cur.execute(sql_select)
        result = cur.fetchall()
        return result
    else:
        mail = dic['mail']
        sql_insert = "insert into code1 (mail,code) values ('%s','%s');" % (mail, code)  # 加入数据库
        cur.execute(sql_insert)
        con.commit()
        return 'ok'
    finally:
        cur.close
        con.close



if __name__ == '__main__':
    app.run(debug=True, port=5009)


# test
# c3c2bd601f0ec6a02ed4a4e55cc15b0b