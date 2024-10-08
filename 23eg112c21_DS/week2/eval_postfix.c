#include <stdio.h>
#include <ctype.h>
#include<stdlib.h>
#include<math.h>
char stack[100];
int top = -1;

void push(char x)
{
    stack[++top] = x;
}
int pop()
{
    if (top == -1)
    {
        return -1;
    }
    else
    {
        return stack[top--];
    }
}
int main()
{
    char exp[20];
    char *e;
    int n1, n2, n3, num;
    printf("Enter the expression\n")                                                                                                                                                           ;
    scanf("%s", &exp);
    e = exp;
    while (*e != '\0')
    {
        if (isdigit(*e))
        {
            num = *e - 48;
            push(num);
        }
        else
        {
            n1 = pop();
            n2 = pop();
            switch (*e)
            {
            case '+':
                n3 = n1 + n2;
                break;
            case '-':
                n3 = n1 - n2;
                break;
            case '/':
                n3 = n1 / n2;
                break;
            case '*':
                n3 = n1 * n2;
                break;
            case '^':
                n3 = pow(n2, n1);
                break;
            default:
                printf("Invalid operator\n");
                break;
            }
            push(n3);
        }
        e++;

    }
    printf("The result of %s is %d \n",exp,pop());
    return 0;
}
