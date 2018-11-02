import pymysql
import requests

class getmail(object):
    def __init__(self,my_mail,code=None):#获取邮箱
        self.mail = my_mail
        self.code = code
        self.url = 'http://127.0.0.1:5009/code?'
        # self.db = pymysql.connect(host="localhost",user="root",
        #                   password="123456",database="study",
        #                   charset="utf8")
        # self.cursor = self.db.cursor()#游标

    def write(self):
        print(self.mail,self.code)
        insert_url = self.url + 'mail=%s&code=%s' % (self.mail,self.code)
        respon = requests.get(insert_url)
        if respon.text == 'ok':
            return True
        else:
            return False

    def read(self):
        select_url = self.url + 'mail=%s' % self.mail
        respon = requests.get(select_url)
        result = respon.text

        # self.tijiao(sql_select)
        # result = self.cursor.fetchall()
        return result

    # def tijiao(self,sql):
    #     #
    #     #     self.cursor.execute(sql)
    #     #     self.db.commit()

    
    # def __del__(self):
    #     # self.cursor.close()
    #     self.db.close()

# a=getmail('937527422@qq.com')
# print(a.read())



        
       
   

  

