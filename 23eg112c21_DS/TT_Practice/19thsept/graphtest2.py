v = [10,5,3,4,7]
g = [
    [0,7,9,11,0],
    [7,0,3,0,4],
    [9,3,0,2,5],
    [11,0,2,0,0],
    [0,4,5,0,0]]
t = 0
vis = []

def dfs(x,i):
    # global t
    vis.append(x)
    # t += 1
    # print(x)
    if x == 7:
        for i in range(len(vis)):
            print(f"{vis[i]}->",end=" ")
        print("\n")
        vis.pop()
        
        return 0

    for j in range(0,5):
        if g[i][j] != 0:
            if v[j] not in vis:
                dfs(v[j],j)
    # vis[t-1] = None
    # t -= 1
    vis.pop()
dfs(10,0)