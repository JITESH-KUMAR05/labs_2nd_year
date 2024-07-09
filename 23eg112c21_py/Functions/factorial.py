# def fact(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return n*fact(n-1)
    
# num = int(input("Enter a number : "))
# if(num<0):
#     print("Sorry, factorial does not exist for negative numbers")
# else:
#     print(f"Factorial of {num} is {fact(num)}")
# def fact(n):
#     fac = 1
#     if n==1 or n==0:
#         print(fac)
#     else:
#         for i in range(n,1,-1):
#             fac = fac*i
#         print(fac)
    
def fact(n):
    fac = 1
    if n==1 or n==0:
        pass
    else:
        fac = n * fact((n-1))
    print("The factorial is",fac )
    
num = eval(input("Enter a number : "))
if(num<0):
    print("Sorry, factorial does not exist for negative numbers")
else:
    # print(f"Factorial of {num} is {fact(num)}")
    fact(num)