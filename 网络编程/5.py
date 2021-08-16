# -*- coding:utf-8 -*-

import socket
import hashlib
import os
def m(md5,ran):
    md = hashlib.md5(md5)
    md.update(ran)
    rs = md.hexdigest()
    return rs
def c(con):
    while True:
        msg=con.recv(1024).decode('utf-8')
        print(msg)
        con.send(msg.upper().encode('utf-8'))
s=socket.socket()
s.bind(('127.0.0.1',9000))
s.listen()
while True:
    con,add=s.accept()
    md5=b'1'
    ran=os.urandom(32)
    con.send(ran)
    d=m(md5,ran)
    b=con.recv(32).decode('utf-8')
    if b==d:
        print('合法')
        c(con)
    else:
        print("不合法")
        con.close()
        s.close()

