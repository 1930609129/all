# import itertools as its
# import time
# words =input("输入字符:")
# cs =int(input("密码长度:"))
# r =its.product(words,repeat=cs)
# dd=len(words)
# dd**=cs
# print("有%r条" %dd)
# cc=(cs+2)*dd
# if cc < 1024:
#     print("大小为%d字节" %cc)
# elif 2**10>=cc or cc<2**20:
#     hh = cc/2**10
#     print("大小为" + str(hh) + "kB")
# elif 2**20>=cc or cc<2**30:
#     hh=cc/2**20
#     print("大小为"+str(hh)+"MB")
# elif 2**30>=cc or cc<2**40:
#     hh=cc/2**30
#     print("大小为"+str(hh)+"GB")
# else:
#     hh = cc / 2 ** 40
#     print("大小为" + str(hh) + "TB")
# sz=input("是否继续y/n")
# if sz=="y":
#     lj =int(input("路径写数字:"))
#     start=time.time()
#     dic = open("B:/%d.txt" % lj,"a")
#     for i in r:
#         dic.write("".join(i))
#         dic.write("".join("\n"))
#     dic.close()
#     end=time.time()
#     print(end-start)
# else:
#     pass
import itertools as its
words ='1234'
r =its.product(words,repeat=3)
dic = open("A:/1.txt","a")
for i in r:
    dic.write("".join(i))
    dic.write("".join("\n"))
dic.close()