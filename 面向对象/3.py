# class A:
#     def __init__(self):
#         self.dic={}
#
#     def __setitem__(self, key, value):
#         self.dic[key]=value
#
#     def __getitem__(self, item):
#         return self.dic[item]
#
#     def __delitem__(self, key):
#         del self.dic[key]
#
# a=A()
# a['wo']=18
# print(a['wo'])
# del a['wo']




# import functools
# @functools.total_ordering
# class A:
#     # def __init__(self,a,b):
#     #     self.a=a
#     #     self.b=b
#
#     def __eq__(self, other):
#         print('eq')
#         pass
#
#     # def __ne__(self, other):
#     #     pass
#     #
#     # def __ge__(self, other):
#     #     pass
#     #
#     # def __gt__(self, other):
#     #     pass
#     #
#     # def __le__(self, other):
#     #     pass
#
#     def __lt__(self, other):
#         print('lt')
#         pass
# a=A()
# b=A()
# print(a<=b)



# class A:
#     def __init__(self):
#         self.age=10
#
#     def __bool__(self):
#         pass
#         # return self.age>=18
#         # return False
#         # return True
# a=A()
# if a:
#     print('hh')



# class A:
#     def __init__(self):
#         self.age=1
#
#     def __iter__(self):
#         # self.age=1
#         return self
#     # def __next__(self):
#     #     self.age += 1
#     #     if self.age>=6:
#     #         raise StopIteration('stop')
#     #     return self.age
#     def __call__(self, *args, **kwargs):
#         self.age += 1
#         if self.age >= 6:
#             raise StopIteration('stop')
#         return self.age
# a=A()
#
# p=iter(a,4)
# for i in p:
#     print(i)



# class A:
#     def __set__(self, instance, value):
#         print('set')
#         instance.v=value
#     def __get__(self, instance, owner):
#         print('get')
#         return instance.v
#     def __delete__(self, instance):
#         print('del')
#         del instance.v
# class B:
#     a=A()
# b=B()
# b.a=10
# print(b.a)
# # del b.a
# c=B()
# c.a=12
# print(c.a)
# print(b.a)




