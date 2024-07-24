#include<stdio.h>
#include<stdlib.h>

struct node{
    int data;
    struct node *next;
};

struct node *head = NULL;
struct node *temp;

void create(){
    temp = (struct node *)malloc(sizeof(struct node));
    printf("Enter the data: ");
    scanf("%d", &temp->data);
    temp->next = NULL;
    if(head == NULL){
        head = temp;
    }
    else{
        struct node *p;
        p = head;
        while(p->next != NULL){
            p = p->next;
        }
        p->next = temp;
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
}

void main(){
    create();
    create();
    create();
    display();
}