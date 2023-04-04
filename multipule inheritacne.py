class A:
    def fun1(self):
        print ("Class A")

class B(A):
    def fun1(self):
        print ("Class B")

class C(A):
    def fun1(self):
        print ("Class A")



class D(B,C):
    def fun1(self):
        print("D")

D1=D()
D1.fun1()