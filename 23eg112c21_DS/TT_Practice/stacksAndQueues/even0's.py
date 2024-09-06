a = [0,1,1,0,1]
c = 0

for i in range(len(a)):
    if a[i] == 0:
        if a[i%2] != 0:
            a[i%2] = 0
            c += 1
        
    elif a[i] == 1:
        if a[i%2] != 1:
            a[i%2] = 1
            c += 1

print(a)
print(c)