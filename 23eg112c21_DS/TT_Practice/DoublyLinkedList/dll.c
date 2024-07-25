#include<stdio.h>
#include<stdlib.h>

struct node{
    int data;
    struct node *prev;
    struct node *next;
};

struct node *head = NULL;
struct node *tail = NULL;
struct node *temp;

void create(){
    temp = (struct node *)malloc(sizeof(struct node));
    printf("Enter the data: ");
    scanf("%d", &temp->data);
    temp->next = NULL;
    temp->prev = NULL;
    if(head == NULL){
        head = temp;
        tail = temp;
    }
    else{
        tail->next = temp;
        temp->prev = tail;
        tail = temp;
    }
}

void display(){
    struct node *p;
    p = head;
    while(p != NULL){
        printf("%d -> ", p->data);
        p = p->next;
    }
    printf("NULL\n");
    
    printf("Reverse: ");
    p = tail;
    while(p != NULL){
        printf("%d -> ", p->data);
        p = p->prev;
    }
    printf("NULL\n");
}

void main(){
    create();
    create();
    create();
    display();
}