#include <stdio.h>

int a[5], t = -1;
int push(int x)
{
    t++;
    a[t] = x;
}
int pop()
{
    t--;
}
int main()
{
    pop();
    push(8);
    push(8);
    push(12);
    push(3);
    push(5);
    pop();
}