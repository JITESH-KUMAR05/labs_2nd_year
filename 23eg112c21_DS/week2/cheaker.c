#include<stdio.h>
char stack[20];
int top=-1;
void push(char ch)
{
	stack[++top]=ch;
}
void pop()
{
	if(top==-1)
	printf("stack is enpty\n");
	else
	stack[top--];
}
int checker(char e)
{
	if((e==')'&& stack[top]=='(')||(e==']'&& stack[top]=='[')||(e=='}'&& stack[top]=='{'))
	{
		pop();
		return 1;
	}
	else return 0;
}
void main()
{
	char exp[20];
	char*e;
	printf("enter expression\n");
	scanf("%s",exp);
	e=exp;
	while(*e!='\0')
	{
		if(*e='('||*e=='{'||*e=='[')
		{
			push(*e);
		}
		else
		{
			if(!checker(*e))
			{
				//printf("Not balanced")
				break;
			}
		}
		e++;
	}
	if(top==-1)
	printf("balanced");
	else
	printf("not balanced");
}
