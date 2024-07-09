def pal(n):
    temp = n
    newno = 0
    while(n!=0):
        digit = n%10
        newno = newno*10+digit
        n = n//10
    if(temp == newno):
        return 1
    else:
        return 0
    

n = int(input("Enter a number: "))
if pal(n):
    print("Palindrome")
else:
    print("Not palindrome")