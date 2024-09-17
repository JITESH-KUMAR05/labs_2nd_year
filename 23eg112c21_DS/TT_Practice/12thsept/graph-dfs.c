#include<stdio.h>

int v[5] = {10,5,3,4,7};
int g[5][5] = {
    {0,1,1,1,0},
    {1,0,1,0,1},
    {1,1,0,1,1},
    {1,0,1,0,0},
    {0,1,1,0,0}
};
int vis[5],t=0;

int dfs(int x, int i){
    vis[t++] == x;
    printf("%d");
}
