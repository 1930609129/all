# -*- coding:utf-8 -*-
# import socket
# s=socket.socket()
# s.connect(('127.0.0.1',9000))
# msg=s.recv(1024)
# print(msg)
# s.send(b'qwe')
# s.close()

# import socket
# s=socket.socket()
# s.connect(('127.0.0.1',9000))
#
# while True:
#     i=input(">>>").encode('utf-8')
#     s.send(i)
#     msg=s.recv(1024).decode('utf-8')
#     print(msg)
#

# import socket
# import json
#
# urs=input('name: ')
# pwd=input('pwd: ')
# dic={'usr':urs,'pwd':pwd}
#
# strdic=json.dumps(dic)
#
# s=socket.socket()
# s.connect(('127.0.0.1',9000))
# s.send(strdic.encode('utf-8'))
# ret=s.recv(1024).decode('utf-8')
# ret_dic=json.loads(ret)
# if ret_dic['result']:
#     print('登录成功')
# s.close()


