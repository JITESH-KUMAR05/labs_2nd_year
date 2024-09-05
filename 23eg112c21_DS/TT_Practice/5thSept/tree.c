#include<stdio.h>
#include<stdlib.h>

struct node
{
    int data;
    struct node *left;
    struct node *right;
};

struct node *createNode(int data)
{
    struct node *newNode = (struct node *)malloc(sizeof(struct node));
    newNode->data = data;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

void insert(struct node *root , struct node *newNode){
    
    
        if(newNode->data < root->data){
            if(root->left == NULL){
                root->left = newNode;
            }
            else{
                insert(root->left,newNode);
            }

        }
        else{
            if(root->right == NULL){
                root->right = newNode;
            }
            else{
                insert(root->right,newNode);
            }
        }
    }



int main(){
    int n;
    struct node *root = NULL;
    struct node *newNode;
    char ch;
    do
    {
        printf("Enter the Data to be inserted: ");
        scanf("%d",&n);
        newNode = createNode(n);       
        if(root == NULL){
            root = newNode;
        }
        else{
            insert(root,newNode);
        }
    } while (ch == 'y' || ch == 'Y');
    
}