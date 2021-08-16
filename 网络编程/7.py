# -*- coding:utf-8 -*-
from socketserver import *
import struct
import json
import os
file=r'D:\基础\chat\a\b'
class A(BaseRequestHandler):
    def handle(self):
        dic_len=self.request.recv(4)
        dlen=struct.unpack('i',dic_len)[0]
        dic=self.request.recv(dlen).decode('utf-8')
        dic=json.loads(dic)
        if dic['opt']=='xia':
            name=dic['name']
            filename=os.path.join(file,name)
            d={}
            if os.path.isfile(filename):
                d['size']=os.path.getsize(filename)
                d['isfile']=True
            else:
                d['isfile']=False
            strdic = json.dumps(d)
            bye = strdic.encode('utf-8')
            dlen = len(bye)
            byelen = struct.pack('i', dlen)
            self.request.send(byelen)
            self.request.send(bye)
            if d['isfile']:
                with open(filename,'rb') as f:
                    while d['size']>2048:
                        msg=f.read(2048)
                        self.request.send(msg)
                        d['isfile']-=len(msg)
                    else:
                        msg = f.read(2048)
                        self.request.send(msg)
s=ThreadingTCPServer(('127.0.0.1',9000),A)
s.serve_forever()