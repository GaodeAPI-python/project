import smtplib,time
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import asyncio
import random
import pymysql1


class userinfo(object):
    def __init__(self,user,mail):


        self.my_sender='937527422@qq.com' # 发件人邮箱账号
        self.my_pass = 'idvjoyjkpnfjbffd' # 发件人邮箱密码
        # my_user=['568551861@qq.com'] # 收件人邮箱账号
        my_mail=[mail,]
        self.user=user
        self.mail=my_mail
        self.b=''
        self.obj = ''
        self.main()
        
    def getcode(self):
        if self.b:
            return self.b
        else:
            return False
    
    def mysql3(self,my_mail,code):       
        self.obj = pymysql1.getmail(my_mail,code)
        if self.obj.write():
            print('ok')
        else:
            print('false')
    
    def getmysqlcode(self,my_mail):
        a = self.obj.read()
        if a:
            return a
        else:
            return False


    def mail2(self,my_mail,tp=False):
        
        # print(my_mail,type(my_mail))
        if not tp:
            try:
                l3=[]
                for i in range(4):

                    l3.append(random.randint(1,9))
                b = ''.join([str(x) for x in l3])
                self.b = b

                print('此处是验证码',b)
                
                
                msgroot = MIMEMultipart('related',)#采用related定义内嵌资源的邮件体

                # msg=MIMEText('注册验证码[%s]<a href="www.shiliu005.com">这里是一个你想要的链接</a><h1>图片演示</h1><p><img src="4.jpg">\
                #     </p>'%l3,'html','utf-8')
                msg=MIMEText('%s您好！您的注册验证码为：[%s]'%(self.user,l3),'html','utf-8')

                msgroot.attach(msg)
                # msgroot['From']=formataddr(["来自孙大大",self.my_sender]) # 显示发件人
                msgroot['From']=formataddr(["来自在线租房系统",self.my_sender]) # 显示发件人
                msgroot['To']=formataddr(["FK",my_mail]) # 括号里的对应收件人邮箱昵称、收件人邮箱账号
                # msgroot['Subject']="来自孙爸爸的爱" # #=显示标题
                msgroot['Subject']="高德API在线租房" # #=显示标题
                server=smtplib.SMTP_SSL("smtp.qq.com",465) # 发件人邮箱中的SMTP服务器,端口是25,加密后为465
                # #*************发送图片
                # fp = open('101.jpg', 'rb')
                # msgImage = MIMEImage(fp.read())
                # fp.close()
                # # 定义图片 ID，在 HTML 文本中引用
                # msgImage.add_header('Content-ID', '<image1>')
                # msgroot.attach(msgImage)
                # #*************
                server.login(self.my_sender,self.my_pass) # 括号中对应的是发件人邮箱账号、邮箱密码
                server.sendmail(self.my_sender,[my_mail,],msgroot.as_string()) # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
                server.quit() # 关闭连接
                print("邮件发送成功")
                # self.mysql3(my_mail,b)
                print('插入成功')
            except Exception as e : # 如果 try 中的语句没有执行，则会执行下面的 ret=False
                print(e)
                print("邮件发送失败")
                with open('false1.txt','w+') as f:
                    f.write(my_mail)
            #         # f.write
    def main(self):

        # self.look = asyncio.get_event_loop()

        # a = []
        # b = True
        # t = time.time()

        # if len(self.mail)>1:
        #     for i in self.mail:
        #         a.append(self.mail(i))
        #         if len(a)>10:
        #             print('进来一次')
        #             self.look.run_until_complete(asyncio.wait(a))
        #             a=[]
        #             b = False
        #     if b:
        #         self.look.run_until_complete(asyncio.wait(a))
        # else:
        #     self.look.run_until_complete(self.mail2(self.mail[0]))
        
        # print(time.time()-t,'完成时间')
        
        
        # look.close()

        t=time.time()

        self.mail2(self.mail[0])
        print('发送时间：',time.time()-t)

    # def __del__(self):
    #     self.look.close()

        

# a=userinfo('user','2653524802@qq.com')
