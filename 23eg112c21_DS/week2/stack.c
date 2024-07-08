#include<stdio.h>
#include<stdlib.h>

void push();
void pop();
void display();
void peek();

#define MAX 5

int top = -1;
int stack[50];

void main(){
	
	
	printf("Start the flow of stack implementation \n");
	
	while(1){
		int op;
		
		printf("Choose the option you want to execute \n 1. push \n 2. pop \n 3. display \n 4. peek \n 5.Exit \n");
		scanf("%d",&op);
		
		
		switch(op){
			case 1:
				push();
				break;
			case 2:
				pop();
				break;
			case 3:
				display();
				break;
			case 4:
				peek();
				break;
			case 5:
				exit(0);
				break;
			default :
			printf("Enter a valid option \n");	
			break;
		}
		
	}
	
}

void push(){
	if(top== MAX-1){
		printf("Overflow\n");
	}

	else{
		top++;
		int val;
		printf("Enter a value to push\n");
		scanf("%d",&val);
		stack[top] = val;
		
	}
	
}
void pop(){
	if(top==-1){
		printf("Underflow\n");
		
	}
	else{
		printf("The element poped is %d\n",stack[top]);
		top-=1;
	}
}

void display(){
	if(top==-1){
		printf("Underflow\n");
		
	}
	else{
		int i;
		for(i=top;i>=0;i--){
			printf("%d\n",stack[i]);	
		}
	}
	
}

void peek(){
	if(top==-1){
		printf("Underflow\n");
		
	}
	else{
		printf("%d\n",stack[top]);
	}
	
}








