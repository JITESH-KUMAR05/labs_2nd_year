#include<stdio.h>
#define MAX 10
#define INF 9999

int cost[MAX][MAX],visited[MAX],mincost=0;

void prims(int num){
    int i ,j , ne = 1, a, b, u, v, min;
    for(i = 1; i <= num; i++)
        visited[i] = 0;
    for(i = 1; i <= num; i++)
        for(j = 1; j <= num; j++)
            if(cost[i][j] == 0)
                cost[i][j] = INF;
    visited[1] = 1;
    while(ne < num){
        min = INF;
        for(i = 1 ; i<=num ; i++){
            if(visited[i] != 0){
                for(j = 1; j <= num; j++){
                    if(!visited[j] && min > cost[i][j]){
                        min = cost[i][j];
                        a = u = i;
                        b = v = j;
                    }
                }
            }
        }
        printf("\n%d edge (%d-%d) = %d\n",ne++,a,b,min);
        mincost += min;
        visited[b] = 1;
        cost[a][b] = cost[b][a] = INF;
    }
    printf("\nMin cost = %d\n",mincost);
    
}
int main(){
    int num,i,j;
    printf("Enter the number of vercices: ");
    scanf("%d",&num);
    printf("Enter the cost matrix: ");
    for(i = 1; i <= num; i++)
        for(j = 1; j <= num; j++)
            scanf("%d",&cost[i][j]);
    prims(num);
    return 0;
}