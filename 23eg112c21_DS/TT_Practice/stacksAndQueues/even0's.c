#include<stdio.h>

void main(){
    int arr[5] = {0,1,1,0,1};
    int c;
    for(int i = 0 ; i<5 ; i++){
        if(arr[i] == 0 ){
            if(arr[i%2] != 0){
                arr[i%2] = 0;
            }
        }
        else if(arr[i] == 1 ){
            if(arr[i%2] != 1){
                arr[i%2] = 1;
            }
        }
        
}
for(int i = 0 ; i < 5 ; i++){
    printf("%d\t",arr[i]);
}
}