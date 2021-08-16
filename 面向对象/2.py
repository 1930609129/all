# class A:
#     def __init__(self):
#         self.age=1
#
#     def __getitem__(self, item):
#         self.age += 1
#         if self.age >= 6:
#             raise StopIteration('stop')
#         return self.age
#     # def __iter__(self):
#     #     # self.age=1
#     #     return self
#     # def __next__(self):
#     #     self.age += 1
#     #     if self.age>=6:
#     #         raise StopIteration('stop')
#     #     return self.age
# a=A()
# for i in a:
#     print(i)




# class A:
#     __x=10
#     def h(self):
#         print(A.__x)
#         print(self.__x)
# print(A.__dict__)
# print(A._A__x)




# class A:
#     def __init__(self):
#         self.__age=10
#
#     def setage(self,value):
#         if isinstance(value,int) and 0<value<150:
#             self.__age=value
#
#     def getage(self):
#         return self.__age
#
# # a=A()
# # a.__dict__['_A__age']=100
# # print(a.getage())
#
# # a.setage(20)
# # print(a.getage())



# class A:
#     def __setattr__(self, key, value):
#         print(key,value)
#         if key=="age" and key in self.__dict__.keys():
#             print('自读属性，不能修改')
#         else:
#             print('jj')
#             self.__dict__[key]=value
#
# a=A()
# a.age=18
# a.age=999
# print(a.age)
# print(a.__dict__)



# class A:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def __str__(self):
#         return "我是%s,%s" %(self.name,self.age)
#
#     def __repr__(self):
#         return 'hhh'
#
# a=A('wo',10)
# print(a)
#
# b=A('ni',18)
# print(b)
#
# print(repr(b))



# import datetime
# t=datetime.datetime.now()
# print(t)
# print(repr(t))
# tt=repr(t)
# print(eval(tt))



# class A:
#
#     def __call__(self, *args, **kwargs):
#         print(args,kwargs)
#
# a=A()
# a(123,name=18)



# def pen(color,pe):
#     print('%s,%s'%(pe,color))
#
# import functools
# ped=functools.partial(pen,pe='钢笔')
# ped('黑色')



# class A:
#     def __init__(self,pen):
#         self.pen=pen
#
#     def __call__(self,colar):
#         print('%s,%s'%(self.pen,colar))
#
# a=A('钢笔')
# a('黑色')
