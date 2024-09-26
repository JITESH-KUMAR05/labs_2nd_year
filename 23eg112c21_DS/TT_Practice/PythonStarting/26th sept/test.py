a = [4,5,6,3,2,3,4,2,4,6,4,6,7,7,7,3,4,4]
dict = {}
for i in range(len(a)):
    if a[i] not in dict.keys():
        dict[a[i]] = 1
    elif a[i] in dict.keys():
        dict[a[i]] = dict[a[i]] + 1
# print(dict)
for i in dict.keys():
    print(f"{i} - {dict[i]}")
