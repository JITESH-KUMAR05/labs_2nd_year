def sum_of_digits(num):
    sum = 0
    while(num!=0):
        digit = num%10
        sum = sum + digit
        num = num//10
    return sum
num = int(input("Enter a number: "))
if num>=0:
    sum = sum_of_digits(num)
    print("The sum of digits is:",sum)
else:
    print("Enter a valid number")