rate = float(input("Enter rate of interest : "))
time = int(input("Enter Time per principal : "))
principal = float(input("Enter principal amount : "))

# def si(p,r,t):
#     si = (p*r*t)/100
#     return si

# si1 = si(principal,rate,time)
# print(si1)
si = (principal*rate*time)/100
print("Simple Interest is : ",si)