#include<stdio.h>
#include<stdlib.h>

struct node{
	int data;
	struct node *next;
	
}*temp,*top=NULL;

void push();
//void pop;
//void peek();
//void display();

int main(){
	int choice , value;
	
	while(1){
		int op;
		
		printf("Choose the option you want to execute \n 1. push \n 2. pop \n 3. display \n 4. peek \n 5.Exit \n");
		scanf("%d",&op);
		
		
		switch(op){
			case 1:
				push();
				break;
//			case 2:
//				pop();
//				break;
			case 3:
				display();
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
	int value;
	printf("Enter the value to enter\n");
	scanf("%d",&value);
	struct node *newnode;
	newnode = (struct node*)malloc(sizeof(struct node));
	newnode -> data = value;
	if(top==NULL){
		newnode->next=NULL;
	}
	else{
		newnode->next=top;
		
	}
	top = newnode;
}
void display(){
	if(top==NULL){
		printf("Stack is empty\n");
		
	}
	else{
		temp = top;
		
	}
	while(temp -> next !=NULL){
		printf("%d",temp->data);
		temp=temp->next;
		
	}
	printf("%d->NULL",temp->data);
	
}

void pop(){
	if(top==NULL){
		printf("Stack is empty\n");
		
	}
	else{
		temp = top;
		top = temp->next;
		printf("Deleted\n");
	}
}

