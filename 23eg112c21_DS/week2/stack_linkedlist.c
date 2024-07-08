#include<stdio.h>
#include<stdlib.h>


int queue[50];
#define size 5

int rear = -1;
int front = -1;

void enqueue();
void dequeue();
void display();
void peek();


void main(){
	
	while(1){
		int op;
		printf(" 1.Enqueue \n 2. Dequeue \n 3. display \n 4. peek \n 5.Exit\n ");
		scanf("%d",&op);
		
		switch(op){
			case 1:
				enqueue();
				break;
				
			case 2:
				dequeue();
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
			
			default:
				printf("Enter a valid option\n");
                break;
		}
	}
}


void enqueue(){
    if (rear == size)
    {
        printf("overflow\n");

    }
    else{
    	if(front==-1 && rear ==-1){
    		front=0;
        	rear=0;
		}
        printf("Enter the number to insert\n");
        int val;
        scanf("%d",&val);
        queue[rear]=val;
        rear++;
        printf("Value inserted :)\n");
    }
    
}


void dequeue(){
    if (front==-1 || rear ==-1 ||  front>=rear)
    {
        printf("Underflow");
    }

    else{
        printf("Element deleted is %d\n",queue[front]);
        front++;
    }
    
}

void peek(){
    if (front==-1 || rear ==-1 ||  front>=rear)
    {
        printf("Underflow");
    }
    else{
        printf("%d\n",queue[front]);
    }
}

void display(){
    if (front==-1 || rear ==-1 ||  front>=rear)
    {
        printf("Underflow\n");
    }

    else{
        int i;
        for(i=front;i<rear;i++){
            printf("%d\n",queue[i]);
        }
    }
}
