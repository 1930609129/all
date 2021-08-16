# file=open('add.py','r')
# print(file.readline())   #读取  读取形式为列表
# print(file.read())   #读取全部内容
# print(file.read(1))   #读取全部指定内容
# file.close()

# file=open('a.txt','w')
# file.write("hello")     #写入
# file.close()

# file=open('a.txt','w')
# file.write("hello")     #追加
# file.close()

# # print("world",file=file)
# lis=["hh","he"]
# file.writelines(lis)
# file.close()

# file=open('a.txt','rb') #读
# file1=open('b.txt','wb') #写
# file1.write(file.read())   #边读边写
# file.close()
# file1.close()

# with open('a.txt','r') as file:
#     print(file.read())

# with open('a.txt','rb') as file:
#     with open('c.txt','wb') as file1:
#         file1.write(file.read())



