string = 'anur*a**guniv*'
lst = []
i = 0
for c in string:
    if c == '*':
        lst.pop()
    else:
        lst.append(c)

print(lst)