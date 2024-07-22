st = input("Enter a string : ")
print(st[1:-1])
new_st = "" + st[-1] + st[1:-1] + st[0]
print(new_st)