#include <stdio.h>
#include <ctype.h>

char stack[100];
int top = -1;

void push(char x)
{
    stack[++top] = x;
}

char pop()
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

int priority(char x)
{
    if (x == '(')
    {
        return 0;
    }
    if (x == '+' || x == '-')
    {
        return 1;
    }
    if (x == '$')
    {
        return 2;
    }
    if (x == '*' || x == '/')
    {
        return 3;
    }
    if (x == '^')
    {
        return 4;
    }
    return 0;
}

int main()
{
    char exp[100];
    char *e, x;
    printf("Enter an expression: ");
    scanf("%s", exp);
    e = exp;
    while (*e !='\0')
    {
        if (isalnum(*e))
        {
            printf("%c", *e);
        }
        else if (*e == '(')
        {
            push(*e);
        }
        else if (*e == ')')
        {
            while ((x = pop()) != '(')
            {
                printf("%c", x);
            }
        }
        else
        {
            while (priority(*e) <= priority(stack[top]))
            {
                printf("%c", pop());
            }
            push(*e);
        }
        e++;
    }
    while (top != -1)
    {
        printf("%c", pop());
    }
    return 0;
}
