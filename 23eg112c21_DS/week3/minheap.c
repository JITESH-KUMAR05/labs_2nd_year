#include <stdio.h>
#include <stdlib.h>

#define MAX 20

void minheapify(int *, int, int); // Function to heapify the array in min heap order
int *buildheap(int *, int); // Function to build the min heap

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
    m = buildheap(a, n);
    printf("The min heap is\n");
    for (i = 0; i < n; i++)
    {
        printf("%d ", m[i]);
    }
}

int *buildheap(int a[], int n)
{
    int heapsize = n;
    int j;
    for (j = n / 2; j >= 0; j--)
    {
        minheapify(a, j, heapsize); // Call minheapify instead of maxheapify
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
        if((left < heapsize) && a[left] < a[i]) // Compare with < instead of >
            smallest = left;
        else
            smallest = i;
        if((right < heapsize) && a[right] < a[smallest]) // Compare with < instead of >
            smallest = right;
        if(smallest != i){
            temp = a[i];
            a[i] = a[smallest];
            a[smallest] = temp;
            minheapify(a,smallest,heapsize); // Call minheapify recursively
        }
    }
}
