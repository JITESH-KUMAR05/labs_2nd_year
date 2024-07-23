lst1 = ['linux','is','good']
lst2 = [0,1,1,2,0]
lst3 = []
for i in range(len(lst2)):
    val = lst1[lst2[i]]
    lst3.append(val)
print(lst3)
