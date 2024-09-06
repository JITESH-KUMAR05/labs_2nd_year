#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node *left;
    struct node *right;
};
struct node *create();
void insert(struct node *, struct node *);
void inorder(struct node *);
struct node *delete(struct node *, int);
struct node *findmin(struct node *);
int search(struct node *, int);
int main()
{
    char ch;
<<<<<<< HEAD
    struct node *root = NULL, *newnode;

    do
    {
=======
    struct node *root = NULL , *newnode;
    do{
>>>>>>> 56263702eb62a4b22b0ee37867569e0ee5cf8b14
        newnode = create();
        if (root == NULL)
            root = newnode;
        else
            insert(root, newnode);
        printf("Do you want to insert (y/n) ? ");
        getchar();
        scanf("%c", &ch);
    } while (ch == 'y' || ch == 'Y');
    printf("\nInorder Traversal\n");
    inorder(root);
    printf("\n");
    do
    {
        if (root == NULL)
        {
            printf("The Tree is empty\n");
            return;
        }
        else
        {
            int data;
            printf("Enter the element to delete\n");
            scanf("%d", &data);
            root = delete (root, data);
        }
    } while (ch == 'y' || ch == 'Y');
    printf("\nInorder Traversal After Deletion\n");
    inorder(root);
    printf("\n");

    printf("Searching \n");

    do
    {
        if (root == NULL)
        {
            printf("The Tree is empty\n");
            return;
        }
        else
        {
            int data;
            printf("Enter the element to search\n");
            scanf("%d", &data);
            search(root, data);
        }

    } while (ch == 'y' || ch == 'Y');

    return 0;
}
struct node *create()
{
    struct node *newnode = (struct node *)malloc(sizeof(struct node));
    int data;
    printf("Enter the data : ");
    scanf("%d", &data);
    newnode->left = newnode->right = NULL;
    newnode->data = data;
    return newnode;
}
void insert(struct node *root, struct node *newnode)
{
    if (newnode->data < root->data)
    {
        if (root->left != NULL)
            insert(root->left, newnode);
        else
            root->left = newnode;
    }
    if (newnode->data > root->data)
    {
        if (root->right != NULL)
            insert(root->right, newnode);
        else
            root->right = newnode;
    }
}
void inorder(struct node *root)
{
    if (root != NULL)
    {
        inorder(root->left);
        printf("%d\t", root->data);
        inorder(root->right);
    }
}

struct node *delete(struct node *root, int data)
{
    struct node *temp;
    if (root == NULL)
        return root;
    if (data < root->data)
        root->left = delete (root->left, data);
    else if (data > root->data)
        root->right = delete (root->right, data);
    else
    {
        if (root->left == NULL)
        {
            temp = root;
            root = root->right;
            free(temp);
            return root;
<<<<<<< HEAD
        }
        else if (root->right == NULL)
        {
            temp = root;
            root = root->left;
            free(temp);
            return root;
        }
        temp = findmin(root->right);
        root->data = temp->data;
        root->right = delete (root->right, temp->data);
    }
    return root;
}
struct node *findmin(struct node *root)
{
    while (root->left != NULL)
        root = root->left;
    return root;
}

int search(struct node *root, int data)
{

    while (root != NULL)
    {
        if (data == root->data)
        {
=======
            }
struct node * findmin(struct node *root){
       while(root->left != NULL)
       root = root->left;
       return root;
       }
int search(struct node *root , int data){
        while(root != NULL){
        	if(data == root->data){
>>>>>>> 56263702eb62a4b22b0ee37867569e0ee5cf8b14
            printf("The data is found \n");
            return 1;
        }
        else if (data < root->data)
        {
            search(root->left, data);
        }
        else if (data > root->data)
        {
            search(root->right, data);
        }
        
    }
    
        
            printf("The data is not found \n");
            return 0;
<<<<<<< HEAD
        
}
=======
        }
		}
}
>>>>>>> 56263702eb62a4b22b0ee37867569e0ee5cf8b14
