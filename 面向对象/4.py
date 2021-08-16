# def a(fun):
#     def b():
#         print('bbb')
#         fun()
#     return b
#
#
# @a
# def c():
#     print('ccc')
# # c=a(c)
# c()

def h(f):
    def hh(*args,**kwargs):
        a=args[0]*2
        f(a)
    return hh
@h
def g(a):
    print(a)
g(1)

# class A:
#     def __init__(self,c):
#         self.c=c
#
#     def __call__(self, *args, **kwargs):
#         print('aaa')
#         self.c()
#
# @A
# def b():
#     print('bbb')
# # b=A(b)
#
# b()



# import win32com.client
#
#
# class A:
#     def __say(self,word):
#         say = win32com.client.Dispatch('SAPI.SpVoice')
#         say.Speak(word)
#     def __check_mun(func):
#         def a(self,n):
#             if not isinstance(n,int):
#                 print("错误")
#             return func(self,n)
#         return a
#
#     @__check_mun
#     def __init__(self,mun):
#         self.__say(mun)
#         self.__mun=mun
#
#     @__check_mun
#     def jia(self,n):
#         self.__say(n)
#         self.__mun+=n
#
#     @__check_mun
#     def jian(self,n):
#         self.__say(n)
#         self.__mun-=n
#
#     @__check_mun
#     def cheng(self,n):
#         self.__say(n)
#         self.__mun*=n
#
#     def show(self):
#         self.__say(self.__mun)
#         return self.__mun
#
# a=A(2)
# a.jia(3)
# a.jian(1)
# a.cheng(3)
# print(a.show())




# import win32com.client
#
#
# class A:
#
#     def __check_mun(func):
#         def a(self,n):
#             if not isinstance(n,int):
#                 print("错误")
#             return func(self,n)
#         return a
#
#     def __say(self,word):
#         say = win32com.client.Dispatch('SAPI.SpVoice')
#         say.Speak(word)
#
#     def __say_zsq(word=""):
#         def __say_(func):
#             def say(self, n):
#                 self.__say(word + str(n))
#                 return func(self, n)
#
#             return say
#         return __say_
#
#     @__check_mun
#     @__say_zsq()
#     def __init__(self,mun):
#         self.__mun=mun
#
#     @__check_mun
#     @__say_zsq('加')
#     def jia(self,n):
#         self.__mun+=n
#         return self
#
#     @__check_mun
#     @__say_zsq("减去")
#     def jian(self,n):
#         self.__mun-=n
#         return self
#
#     @__check_mun
#     @__say_zsq('乘以')
#     def cheng(self,n):
#         self.__mun*=n
#         return self
#
#     def show(self):
#         self.__say(self.__mun)
#         return self.__mun
#
# a=A(2)
# a.jia(3).jian(1).cheng(3).jian(1).cheng(7)
# print(a.show())


