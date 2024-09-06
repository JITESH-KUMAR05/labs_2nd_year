def ispal(n):
    c = n
    new = 0
    while(n>0):
        digit = n % 10
        n = n // 10
        new = new * 10 + digit
    if c == new:
        return True
    else:
        return False

print(ispal(-121))
