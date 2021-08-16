# -*- coding:utf-8 -*-
import socket
import os
import json
s=socket.socket()
s.connect(('127.0.0.1',9000))

file=input(">>>")
if os.path.isabs(file):
    name=os.path.basename(file)
    zi=os.path.getsize(file)
    dic={'file':name,'zip':zi}
    strdic=json.dumps(dic)
    s.send(strdic.encode('utf-8'))
    with open(file,'rb') as f:
        cos=f.read()
        s.send(cos)
s.close()