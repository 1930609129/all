import socket
# s=socket.socket()
# s.bind(('127.0.0.1',9000))
# s.listen()
# con,_=s.accept()
# con.send(b'hh')
# msg=con.recv(1024)
# print(msg)
# con.close()
# s.close()

# import socket
# s=socket.socket()
# s.bind(('127.0.0.1',9000))
# s.listen()
# con,_=s.accept()
# while True:
#     msg=con.recv(1024).decode('utf-8')
#     print(msg)
#     i=input('>>>').encode('utf-8')
#     con.send(i)

# import socket
# import json
# import hashlib
#
# def h(name,pwd):
#     md5=hashlib.md5(name.encode('utf-8'))
#     md5.update(pwd.encode('utf-8'))
#     return md5.hexdigest()
# s=socket.socket()
# s.bind(('127.0.0.1',9000))
# s.listen()
# con,_=s.accept()
#
# msg=con.recv(1024).decode('utf-8')
# dic=json.loads(msg)
# with open('1',encoding='utf-8') as f:
#     for i in f:
#         usr,pwd=i.strip().split('|')
#         if usr==dic['usr'] and pwd==h(dic['usr'],dic['pwd']):
#             di={'opt':'login','result':True}
#             break
#         else:
#             di = {'opt': 'login', 'result': False}
# d=json.dumps(di).encode('utf-8')
# con.send(d)
# con.close()
# s.close()










