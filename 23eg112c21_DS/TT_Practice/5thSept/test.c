#include<stdio.h>
int t;
int fun(int x){
    if(x==4){
        return 20;
    }
    printf("%d\n",x);
    t = fun(x+1);
    printf("%d\n",x);
    return t+x;
}
int main(){
    printf("%d",fun(1));
    return 0;    
}