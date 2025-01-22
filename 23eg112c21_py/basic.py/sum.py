# factorial of a number 
num = int(input("Enter a number: "))
fac = 1
while num > 1:
    fac *= num
    num -= 1
print(fac)