import hashlib

def md5(pwd):#密码MD5加密        
    m= hashlib.md5()  #创建md5对象
    m.update(pwd.encode()) #生成加密串，其中password是要加密的字符串
    return m.hexdigest()  #打印经过md5加密的字符串

print(md5('A123'))

