# program for prime number
num = int(input("Enter a number: "))

fac = 0

for i in range(1,num):
    if(num%i==0):
        fac +=1
    
if(fac>1):
    print("The number is not prime")
else:
    print("The number is prime")