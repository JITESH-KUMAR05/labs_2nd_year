#include<stdio.h>

int a[20][20] , visited[20] , n;
void dfs(int v){
    int i;
    for(i=0;i<n;i++){
        if(a[v][i] && visited[i] == 0){
            visited[i] = 1;
            printf("%d ", i);  // printing node number from 1 to n
            dfs(i);
        }
    }
}

int main(){
    int i,v,j;
    printf("Enter no of vertices: ");
    scanf("%d",&n);
    for(i = 0;i<n;i++){
        visited[i] = 0;
    }
    printf("Enter adjacency matrix: \n");
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            scanf("%d",&a[i][j]);
        }
    }
    printf("Enter starting vertex: ");
    scanf("%d",&v);
    printf("DFS traversal from vertex %d: ", v);
    visited[v] = 1;
    printf("%d ", v);  // printing node number from 1 to n
    dfs(v);
}