# class A:
#     __slots__ = ['age']
# a=A()
# a.age=1
# print(a.age)



# class A:
#     _x=10   # 受保护的属性    __x=10  #受保护的私有属性
#     def hh(self):
#         print(self._x)
# class B(A):
#     def h(self):
#         print(self._x)
#     def hh(self):
#         print('重写')
# a=A()
# a.hh()
# print(a._x)
# print(A._x)
#
# b=B()
# b.hh()
# b.h()
# print(B._x)
# print(b._x)




# class A:
#     def __init__(self):
#         self.__age=10
#     @property
#     def age(self):
#         return self.__age
# a=A()
# print(a.age)

# class A:
#     def __init__(self):
#         self.__age=10
#     def getage(self):
#         return self.__age
#     def setage(self,value):
#         self.__age=value
#     age=property(getage,setage)
# a=A()
# print(a.age)
# a.age=29
# print(a.age)




# class A:
#     def __init__(self):
#         self.__age=18
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self,value):
#         self.__age=value
#
# a=A()
# print(a.age)
# a.age=10
# print(a.age)
# print(a.__dict__)
