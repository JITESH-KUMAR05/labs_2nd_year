def swap_two_no(n1,n2):
    temp = n1
    n1 = n2
    n2 = temp
    print(n1,n2)

# def swap_two_no(n1,n2):
#     temp = n1
#     n1 = n2
#     n2 = temp
#     return n1,n2

num1 = int(input("Enter first number: "))
num2 = int(input("Enter Second number: "))
print(num1,num2)
print(swap_two_no(num1,num2))