# class A():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def hh(self):
#         print(self.name,self.age)
# class B(A):
#     def __init__(self,name,age,b):
#         super().__init__(name,age)   #调用父类
#         self.b=b
#     def hh(self):        #重写父类方法
#         super().hh()    #调用父类
#         print(self.b)
# class C(A):
#     def __init__(self,name,age,c):
#         super().__init__(name,age)
#         self.c=c
# d=B("wo",18,20)
# f=C("ni",20,20)
# d.hh()
# f.hh()

