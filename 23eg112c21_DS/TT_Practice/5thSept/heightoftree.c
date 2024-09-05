#include<stdio.h>
#include<stdlib.h>

struct node {
    int data;
    struct node *left;
    struct node *right;
};

struct node *create(int data){
    struct node *newnode = (struct node *)malloc(sizeof(struct node));
    newnode->data = data;
    newnode->left = NULL;
    newnode->right = NULL;
    return newnode;
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

int heightoftree(struct node *root){
    if (root == NULL)
        return -1; // Base case: height of empty tree is -1
    
    // Recursive case: find the height of left and right subtrees
    int leftHeight = heightoftree(root->left);
    int rightHeight = heightoftree(root->right);
    
    // Return the greater height plus one for the current node
    return (leftHeight > rightHeight ? leftHeight : rightHeight) + 1;
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
        newNode = create(n);       
        if(root == NULL){
            root = newNode;
        }
        else{
            insert(root,newNode);
        }
        printf("Do you want to insert more nodes? (y/n): ");
        scanf(" %c",&ch);
    } while (ch == 'y' || ch == 'Y');
    printf("%d",heightoftree(root));
}