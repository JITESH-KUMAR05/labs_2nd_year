# this code is giving the output but this is not the efficient way of solving this problem
# as i have used some unwanted variables as well


st = "ap$pl#e@s"
duml = list(st)
newst = []
hashl = []
# finalst = str()
for i in range(len(st)):

    if duml[i].isalpha():
        # st[i].join(newst)
        newst.append(st[i])
    else:
        hashl.append(i)
newst = newst[::-1]
for i in range(len(duml)):
    for j in hashl:
        if i == j:
            newst.insert(j,duml[i])
# finalst = str(newst)
# finalst = ""
# for i in newst:
#     finalst + i
finalst = "".join(newst)
print(duml)
print(newst)
print(hashl)
print(finalst)