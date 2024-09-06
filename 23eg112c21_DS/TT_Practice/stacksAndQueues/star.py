string = 'anur**guni*v'
lst = []
i = 0
for c in string:
    lst.append(c)
# print(lst)
for c in lst:
    if c == '*':
        i = c.index(c)
        lst.remove(lst[i-1])
        # print(i)
        lst.remove(c)
        

print(lst)
