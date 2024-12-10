# this is more efficient way we can do the problem 

st = "ap$pl#e@s"
lst = list(st)
i = 0
j = len(lst) - 1
while i<j:
    if lst[i].isalnum() and lst[j].isalnum():
        temp = lst[i]
        lst[i] = lst[j]
        lst[j] = temp
        i = i + 1
        j = j - 1
    elif(not lst[i].isalnum()):
        i = i + 1
    elif (not lst[j].isalnum()):
        j = j - 1

print("".join(lst))