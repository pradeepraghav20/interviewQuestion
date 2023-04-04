class Aba:
    a=20
    b=40
    def fun1(self):
        print("this is instance method")
    @classmethod
    def fun2(cls):
        print(cls.a)
        print(cls.b)
@staticmethod
def fun3():
    print(Aba.a)

ob1=Aba()
ob1.fun2()
Aba.a=33
ob1.fun2()
a
fun3()


