# -*- coding:utf-8 -*-
import socket
import json

s=socket.socket()
s.bind(('127.0.0.1',9000))
s.listen()
con,_=s.accept()

strdrs=con.recv(1024).decode('utf-8')
drs=json.loads(strdrs)
conn=con.recv(drs['zip'])
with open(drs['file'],'wb') as f:
    f.write(conn)
con.close()
s.close()