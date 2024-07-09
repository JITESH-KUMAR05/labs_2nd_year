def factorial(n, result=1):
    if n == 0:
        print(result)
    else:
        factorial(n-1, result * n)

num = int(input("Enter a number : "))
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
else:
    factorial(num)