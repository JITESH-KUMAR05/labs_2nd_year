#include<stdio.h>
#include<stdlib.h>
int stack[10],val,ch;
struct node{
	int data;
	struct node *next;
}*new,*top=NULL,*temp;

int push()
{
	if(top==NULL)
	 printf("stack if full");
	else
	 printf("enter the value:");
	 scanf("%d",&val);
	 new=(struct node *)malloc(sizeof(struct node));
	 new->data=val;
	 new->next=NULL;
	 
}
int pop()
{
	if(top==NULL)
	 printf("stack is empty");
	else
	 temp=top;
	 temp=temp->next;
	 free(temp); 
}
void view()
{
	if(top==NULL)
	 printf("stack is empty");
	else
	 temp=top;
	 while(temp!=NULL)
	 {
	 	printf("%d\t",temp->data);
	 	temp=temp->next;
	 }
}
int main()
{
	printf("stack operations:");
	while(ch!=4)
	{
		printf("\n1.push\n2.pop\n3.view\n4.exit\n");
		printf("enter your choice:");
		scanf("%d",&ch);
		switch(ch)
		{
			case 1:push();break;
			case 2:pop();break;
			case 3:view();break;
			case 4:printf("EXIT......!!");
			default :printf("enter valid input....!!");
			
		}
	}
}

