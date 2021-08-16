# 在类之外为函数，在类之内为方法
# class SB:
#     bb='hello'  #在类写的变量，称为类属性
#
#     def __init__(self,name,age):   #初始化
#         self.name=name   #self.name称为实例属性，将局部变量name赋值给实例属性
#         self.age=age
#
#     def eat(self):    #实例方法
#         print("吃饭")
#
#     @staticmethod
#     def hh():
#         print("使用staticmethod修饰，所以是静态方法")
#
#     @classmethod
#
#     def he(cls):
#         print("使用classmethon修饰，所以是类方法")

#创建SB类的实例对象
# sb=SB("卧槽",18)
# print(sb.name)
# print(sb.age)
# sb.eat()
# SB.eat(sb)  #方法名（类的对象）———>实际是方法定义处的self

# s=SB("我",1)
# b=SB("操",8)
# print(SB.bb)
# print(s.bb)
# print(b.bb)
# SB.bb="world"
# print(SB.bb)
# print(s.bb)
# print(b.bb)
# SB.he()
# SB.hh()

# class SB:
#     bb='hello'
#
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def eat(self):
#         print("%s吃饭" % self.name)
# sb=SB("我",18)
# sb.gender='嘿嘿'
# sb.eat()
# print(sb.name,sb.age,sb.gender)
# def sb1():
#     return "hh"
# sb.sb=sb1
# print(sb.name,sb.age,sb.gender,sb.sb())
