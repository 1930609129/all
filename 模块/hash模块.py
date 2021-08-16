import hashlib
# md5=hashlib.md5()
# md5.update("666".encode('utf-8'))
# d=md5.hexdigest()
# print(d)

# md5=hashlib.md5(b'1234567')
# md5.update('666'.encode('utf-8'))
# print(md5.hexdigest())

# def h(m,s):
#     md5=hashlib.md5(m)
#     md5.update(s.encode("utf-8"))
#     return md5.hexdigest()
# a=input('>>')
# b=input(">>")
# c=h(a.encode('utf-8'),b)
# fp=open('./1.txt','w',encoding='utf-8')
# fp.write(a)
# fp.write('\n')
# fp.write(c)
# fp.close()

# def ha(m,s):
#     md5=hashlib.md5(m)
#     md5.update(s.encode('utf-8'))
#     return md5.hexdigest()
# h = input('>>')
# hh = input(">>")
# c=ha(h.encode('utf-8'),hh)
# hhh=open('./1.txt','r',encoding='utf-8')
# a=hhh.readline().strip()
# b=hhh.readline().strip()
#
# if h==a and c==b:
#     print("登录")

# md5=hashlib.md5(b'12345')
# f=open('./t.txt','rb')
# for line in f:
#     md5.update(line)
# print(md5.hexdigest())

