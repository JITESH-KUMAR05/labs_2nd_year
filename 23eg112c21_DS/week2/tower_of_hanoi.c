#include<stdio.h>

void towers(int,char,char,char);

int main(){
	int num;
	printf("Enter no if disks: ");
	scanf("%d",&num);
	towers(num,'S','D','A');
	return 0;
	
}

void towers(int num,char source, char dist , char aux){
	if(num==1){
		printf("Move disk from %c to %c \n", source,dist);
		return;
	}
	towers(num-1,source,aux,dist);
	printf("move disk from %c to %c \n", source,dist);
	towers(num-1,aux,dist,source);
	
}
