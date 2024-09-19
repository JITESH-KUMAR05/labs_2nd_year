v = [10,5,3,4,7]
g = [
    [0,7,9,11,0],
    [7,0,3,0,4],
    [9,3,0,2,5],
    [11,0,2,0,0],
    [0,4,5,0,0]]
t = 0
vis = []
summ = 0
small = 0


def dfs(x,i):
    vis.append(x)
    if x == 7:
        for i in range(len(vis)):
            print(f"{vis[i]}->",end=" ")
        print("\n")
        print(summ)
        if small == 0 or summ < small:
            small = summ
        vis.pop()
        
        return 0

    for j in range(0,5):
        if g[i][j] != 0:
            if v[j] not in vis:
                summ += g[i][j]
                dfs(v[j],j)
                summ -= g[i][j]
    vis.pop()
dfs(10,0)
print(small)