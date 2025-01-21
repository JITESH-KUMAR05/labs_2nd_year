# notes

class qwer:
    def asd(self):
        print("HI")

# def asd():
#     print("Hello")

class zxc(qwer):
    def fun(self):
        print("Hello")
    def asd(self):
        print("Hey")
x = qwer()
x.asd()
# asd()
y = zxc()
y.fun()
y.asd() #here i implemented inheritance here zxc class inherited qwer now asd method is available in zxc
# here asd function was now declared in zxc so it is a error or polymorphism so it is handled with method overriding
# if this happens with method then method overriding and if it happens with constructor then it is called as
# constructor overloading and if happens with variable then variable overriding

# there are 2 types of polymorphism one is runtime and other is compile time
#  runtime is handled with method overriding
# compile time is handled with overloading
#  overiding happens in diffent class
# overloading happens in same class

class A:
    def fun(self):
        print("HI")

class B(A):
    def fun(self):
        print("Hello")

class C(B):
    def fun(self):
        print("hey")

x = C()
x.fun()