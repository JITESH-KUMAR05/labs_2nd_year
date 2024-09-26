
l = [1,2,3,4,5,6,7,8,9,12]
a = 10
if a in l:
    print(l.index(a))
else:
    for i in range(len(l)):
        if l[i] > a:
            l.insert(i,a)
            print(i)
            break
print(l)