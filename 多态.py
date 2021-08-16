class A():
    def eat(self):
        print("h")
class B(A):
    def eat(self):
        print("hh")
class C(A):
    def eat(self):
        print("hhh")
def a(x):
    return x.eat()
a(A())
a(B())
a(C())