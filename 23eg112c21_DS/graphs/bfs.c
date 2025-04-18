#include<stdio.h>

int a[20][20] , visited[20] , n , q[20] , f = -1 , r = -1;
void bfs(int v){
    int i;
    q[++r] = v;
    visited[v] = 1;
    while(f < r){
        v = q[++f];
        for(i=0;i<n;i++){
            if(a[v][i] != 0 && visited[i] == 0){
                q[++r] = i;
                visited[i] = 1;
                printf("%d ", i);  // printing node number from 1 to n
            }
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
    scanf("%d",&v);
    v = v - 1;  // Adjust for 0-based indexing
    printf("Enter starting vertex: ");
    scanf("%d",&v);
    printf("BFS traversal from vertex %d: ", v);
    visited[v] = 1;
    printf("%d ", v);  // printing node number from 1 to n
    bfs(v);
}
}