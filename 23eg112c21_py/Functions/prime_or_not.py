def prime_or_not(n):
    factor = 0
    for i in range(1,n):
        if n%i == 0:
            factor += 1
    
    if factor==1:
        print("The number is prime")
    else:
        print("The number is not prime")

num = int(input("Enter a number: "))
prime_or_not(num)