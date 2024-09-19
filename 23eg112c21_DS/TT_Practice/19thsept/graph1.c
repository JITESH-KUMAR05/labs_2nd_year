#include<stdio.h>

int t=-1,h[1000]={0},g[5][5]={{0,1,1,1,0},{1,0,1,0,1},{1,1,0,1,1},{1,0,1,0,0},{0,1,1,0,0}},i,j,vist[5],v[5]={10,5,3,4,7};
int DFS(int x,int i)
{
	int j;
	vist[++t]=x;
	h[x]=1;
	// printf("%d ",x);
    if(x==7)
    {
        printf("\n");
        for(j=0;j<=t;j++)
        {
            printf("%d-> ",vist[j]);
        }
        printf("\n");
        t--;
        h[x]=0;
        return 0;
    }
	for(j=0;j<5;j++)
	{
		if(g[i][j]!=0 && h[v[j]]==0)
		{
			DFS(v[j],j);
		}
	}
    t--;
    h[x]=0;

}
int main()
{
	DFS(10,0);
}