#include<stdio.h>
#include<stdlib.h>
//#include<conio.h>
struct node{
	int data;
	struct node *next;
}*temp,*front=NULL,*rear=NULL;

void enqueue(int);
void dequeue();
void peek();
void display();

void main(){
	int choice,value;
	while(1){
		printf("%\n 1 enqueue \n 2 dequeue \n 3 peek \n 4 display \n 5 exit\n");
		printf("Enter your Choice : \n");
		scanf("%d",&choice);
		switch(choice){
			case 1:
				printf("Enter value: \n");
				scanf("%d",&value);
				enqueue(value);
				break;
			case 2:
				dequeue();
				break;
			
			case 3:
				peek();
				break;
			
			case 4:
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


void enqueue(int value){
	struct node * newnode;
	newnode = (struct node *)malloc(sizeof(struct node));
	newnode -> data = value;
	newnode->next=NULL;
	if(front==NULL && rear == NULL){
		front = rear = newnode;
	}
	else{
		rear->next=newnode;
		rear =newnode;
	}
}
void dequeue(){
	if(front==NULL){
		printf("Empty queue\n");
		
	}
	else{
		temp=front;
		front = front->next;
		printf("Deleted %d\n",temp->data);
		free(temp);
	}
}
void peek(){
	if(front==NULL){
		printf("Empty queue\n");	
	}
	else{
		printf("Front element is %d\n",front->data);
	}
}
void display(){
	if(front==NULL){
		printf("Empty queue\n");
	}
	else{
		temp = front;
		while(temp->next!=NULL){
			printf("%d--->",temp->data);
			temp=temp->next;
		}
		printf("%d --->NULL",temp->data);
	}
}



