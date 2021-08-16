# def add(a,b):
#     return a+b
# a=add(b=10,a=20)
# print(a)
# b=add(10,20)
# print(b)

# def a(x,y):
#     y.append(10)
#     x=100
#     print(x)
#     print(y)
# n=11
# n1=[11,22,33]
# a(n,n1)
# print(n)    #不可变对象，在函数体内修改不会影响实参值
# print(n1)   #可变对象，在函数体内修改会改变实参值

# def a(lis):
#     b=[]
#     c=[]
#     for i in lis:
#         if i %2:
#             b.append(i)
#         else:
#             c.append(i)
#     return b,c
# d=[11,22,33,44,55,66]
# print(a(d))      #如果返回值是多个返回类型为元组

# def b():
#     return "hello"
# print(b())
#
# def a():
#     return "hello","world"
# print(a())

# def c(a,b=10):
#     print(a,b)
# c(100)
# c(20,2)

# def a(*b):   #个数可变的位置形参
#     print(b)
# a(10)
# a("hello",10)
# def b(**a):     #个数可变的关键字形参
#     print(a)
# b(a=10,c=29)

# def c(*a,**b):
#     print(a,b)
# c(11,22,a=11,c=22)

# def h(a,b,c):
#     print(a)
#     print(b)
#     print(c)
# lis=[11,22,33]
# h(*lis)
# dic={"a":11,"b":22,"c":4}
# h(**dic)

# def h(a,b,*,c,d):    # 在*之后 调用函数只能用关键字参数传递
#     print(a)
#     print(b)
#     print(c)
#     print(d)
# h(11,22,c=2,d=1)

# name = 'hh'
# def h():
#     print(name)
# h()
# def c():
#     global age    # 使函数外也可调用，变为了全局变量
#     age=10
#     print(age)
# c()
# print(age)
import paddle
def reader_creator(file_path):
    def reader():
        with open(file_path,'r') as f:
            lines=f.readlines()
            for line in lines:
                yield line.replace('\n','')
    return reader
reader=reader_creator('./1.txt')
# 批次读取
random_reader=paddle.reader.shuffle(reader,buf_size=10)
batch_reader=paddle.batch(random_reader,batch_size=3)
for i,j in enumerate(batch_reader()):
    print(i)
    print(j)
