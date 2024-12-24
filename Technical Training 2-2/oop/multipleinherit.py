class A:
    def fun(self):
        print("HI")

class B():
    def fun(self):
        print("Hello")

class C(B,A):
    ''' here class B is inherited first so the priority of the methods of
        of class B will be higher than method A
        if we change the order from B,A to A,B then method of A will be having higher priority
     '''
    def fun1(self):
        print("hey")

x = C()
x.fun()