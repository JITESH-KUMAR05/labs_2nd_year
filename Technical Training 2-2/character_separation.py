inp = "hfs342@33#jk"
linp = list(inp)
alphas = []
nums = []
special = []
for i in range(len(linp)):
    if linp[i].isalpha():
        alphas.append(linp[i])
    elif linp[i].isnumeric():
        nums.append(linp[i])
    else:
        special.append(nums[i])

print("".join(alphas))
print("".join(nums))
print((""))
