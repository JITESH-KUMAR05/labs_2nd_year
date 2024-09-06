#include <stdio.h>

char a[5], t = -1;
int push(char x)
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
    char s[50];
    scanf("%d",s);
}