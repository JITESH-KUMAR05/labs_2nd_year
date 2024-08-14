// code for min heap
#include <stdio.h>
#include <stdlib.h>

#define MAX 20

void minheapify(int *, int, int);
int *buildminheap(int *, int);

void main()
{
    int i, t, n;
    int *a = calloc(MAX, sizeof(int));
    int *m = calloc(MAX, sizeof(int));
    printf("Enter the number of elements in the array\n");
    scanf("%d", &n);
    printf("Enter the elements of the array\n");
    for (i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }
    m = buildminheap(a, n);
    printf("The min heap is\n");
    for (i = 0; i < n; i++)
    {
        printf("%d ", m[i]);
    }
}

int *buildminheap(int a[], int n)
{
    int heapsize = n;
    int j;
    for (j = n / 2; j >= 0; j--)
    {
        minheapify(a, j, heapsize);
    }
    return a;
}

void minheapify(int a[], int i, int heapsize)
{
    int temp, smallest, left, right, k;
    left = (2 * i) + 1;
    right = (2 * i) + 2;
    if (left >= heapsize)
        return;
    else{
        if((left < heapsize) && a[left] < a[i])
            smallest = left;
        else
            smallest = i;
        if((right < heapsize) && a[right] < a[smallest])
            smallest = right;
        if(smallest != i){
            temp = a[i];
            a[i] = a[smallest];
            a[smallest] = temp;
            minheapify(a,smallest,heapsize);
        }
    }
}