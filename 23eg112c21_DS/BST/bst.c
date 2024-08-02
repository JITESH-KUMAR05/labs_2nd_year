#include<stdio.h>
#include<stdlib.h>

struct node{
    int data;
    struct node* left;
    struct node* right;
};
struct node *create();
void insert(struct node * , struct node *);
void inorder(struct node *);
int main()
{
    char ch;
    struct node *root = NULL , *newnode;

    do{
        newnode = create();
        if(root == NULL)
        root = newnode;
        else
        insert(root , newnode);
        printf("Do you want to insert (y/n) ? ");
        getchar();
        scanf("%c",&ch);
    }while(ch =='y' || ch == 'Y');
    printf("\nInorder Traversal\n");
    inorder(root);
    return 0;
}
struct node *create(){
    struct node *newnode = (struct node*)malloc(sizeof(struct node));
    int data;
    printf("Enter the data : ");
    scanf("%d",&data);
    newnode->left = newnode->right = NULL;
    newnode->data = data;
    return newnode;
}
void insert(struct node *root , struct node * newnode){
    if(newnode->data < root->data){
        if(root->left != NULL)
        insert(root->left,newnode);
        else
        root->left = newnode;
    }
    if(newnode->data > root->data){
        if(root->right != NULL)
        insert(root->right ,newnode);
        else
        root->right = newnode;

    }
}
void inorder(struct node *root){
    if(root != NULL){
        inorder(root->left);
        printf("%d\t",root->data);
        inorder(root->right);
    }
}