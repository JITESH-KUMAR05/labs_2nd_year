st = input("Enter a string : ")
lc = 0
uc = 0
dc = 0
sc = 0
for ch in st:
    if ch.islower():
        lc += 1
    elif ch.isupper():
        uc += 1
    elif ch.isdigit():
        dc += 1
    elif ch.isspace():
        sc += 1
print("Lower case characters : ", lc)
print("Upper case characters : ", uc)
print("Digits : ", dc)
print("Spaces : ", sc)
