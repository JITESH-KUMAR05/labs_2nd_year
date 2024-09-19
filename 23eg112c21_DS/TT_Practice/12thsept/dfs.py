v = [10,5,3,4,7]
g = [[0,1,1,1,0],[1,0,1,0,1],[1,1,0,1,1],[1,0,1,0,0],[0,1,1,0,0]]
t = 0
vis = []

def dfs(x,i):
    vis[t] = x
    t += 1
    print(x)
    for j in range(0,5):
        if g[x][j] != 0:
            if v[j] not in vis:
                dfs(j,i)