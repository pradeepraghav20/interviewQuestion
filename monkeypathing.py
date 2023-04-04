class A:
    def fun1(self):
        print("this is A clss")

def monkey_dun(self):
    print("hii")

obj1=A()
A.fun1=monkey_dun

obj1.fun1()