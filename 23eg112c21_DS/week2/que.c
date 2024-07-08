#include <stdio.h>
#include <stdlib.h>
#define MAX 5
int queue[MAX], F = -1, R = -1;
void enqueue();
void dequeue();
void display();
void main()
{
    int op;
    while (1)
    {
        printf("enter your choice \n");
        printf("1: enqueue\n 2: dequeue\n 3: display\n 4:exit\n");
        scanf("%d", &op);
        switch (op)
        {
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
            exit(0);
            break;
        default:
            printf("wrong option \n");
            break;
        }
    }
}
void enqueue()
{
    int num;
    if (R == MAX - 1)
    {
        printf("queue is overflow \n");
    }
    else
    {
        printf("\n enter value \n");
        scanf("%d", &num);
        if (F == -1 || R == -1)
        {
            F = 0;
            R = 0;
            queue[R] = num;
        }
        else
        {
            R = R + 1;
            queue[R] = num;
        }
    }
}
void dequeue()
{
    if (F == -1 || F > R)
    {
        printf("queue is underflow\n");
    }
    else
    {
        printf("deleted element %d", queue[F]);
        F = F + 1;
    }
}
void display()
{
    if (F = -1 || F > R)
    {
        printf("queue is under flow\n");
    }
    else
    {
    	int i;
        for (i = F; i <= R; i++)
            printf("%d\t", queue[i]);
    }
}
