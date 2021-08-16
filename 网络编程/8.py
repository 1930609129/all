# -*- coding:utf-8 -*-
import socket
import struct
import json
import os
dir='D:\基础\chat\\a'
s=socket.socket()
s.connect(('127.0.0.1',9000))

lj=input(">>>").strip()
dic={'name':lj,'opt':'xia'}
strdic=json.dumps(dic)
bye=strdic.encode('utf-8')
dlen=len(bye)
byelen=struct.pack('i',dlen)
s.send(byelen)
s.send(bye)
dic_len=s.recv(4)
dlen=struct.unpack('i',dic_len)[0]
dic=s.recv(dlen).decode('utf-8')
dic=json.loads(dic)
if dic['isfile']:
    file=os.path.join(dir,lj)
    with open(file,'wb') as f:
        while dic['size']>2048:
            con=s.recv(2048)
            f.write(con)
            dic['size']-=len(con)
        else:
            while dic['size']:
                con=s.recv(dic['size'])
                f.write(con)
                dic['size'] -= len(con)
else:
    print("路径不存在")
s.close()