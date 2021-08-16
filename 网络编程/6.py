# -*- coding:utf-8 -*-

import socket
import hashlib
import time
def m(md5,ran):
    md = hashlib.md5(md5)
    md.update(ran)
    rs = md.hexdigest()
    return rs
def c(con):
    while True:
        con.send('hh'.encode('utf-8'))
        msg=con.recv(1024).decode('utf-8')
        print(msg)
        time.sleep(0.5)
s=socket.socket()
s.connect(('127.0.0.1',9000))
md5=b'1'

ran=s.recv(32)
h=m(md5,ran)
s.send(h.encode('utf-8'))
c(s)
s.close()




