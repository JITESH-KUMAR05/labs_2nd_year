#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node *left;
    struct node *right;
};

struct node *root = NULL;
struct node *newnode;

void create();
void insert(struct node *, struct node *);
void inorder(struct node *);
void preorder(struct node *);
void postorder(struct node *);

void create()
{
    int data;
    newnode = (struct node *)malloc(sizeof(struct node));
    if (newnode == NULL)
    {
        printf("Memory not allocated\n");
        return;
    }
    printf("Enter the data\n");
    scanf("%d", &data);
    newnode->data = data;
    newnode->left = NULL;
    newnode->right = NULL;
    printf("data saved successfully;\n");
    if (root == NULL)
    {
        root = newnode;
    }
    else
    {
        insert(root, newnode);
    }
}

void insert(struct node *root, struct node *newnode)
{
    char ch;
    printf("Do you want to insert at left or right? ");
    scanf(" %c", &ch);
    switch (ch)
    {
    case 'l':
    case 'L':
        if (root->left == NULL)
        {
            root->left = newnode;
        }
        else
        {
            insert(root->left, newnode);
        }
        break;
    case 'r':
    case 'R':
        if (root->right == NULL)
        {
            root->right = newnode;
        }
        else
        {
            insert(root->right, newnode);
        }
        break;
    default:
        printf("Invalid choice\n");
        free(newnode);
    }
}

void inorder(struct node *root)
{
    if (root == NULL)
        return;
    inorder(root->left);
    printf("%d\n", root->data);
    inorder(root->right);
}

void preorder(struct node *root)
{
    if (root == NULL)
        return;
    printf("%d\n", root->data);
    preorder(root->left);
    preorder(root->right);
}

void postorder(struct node *root)
{
    if (root == NULL)
        return;
    postorder(root->left);
    postorder(root->right);
    printf("%d\n", root->data);
}

int main()
{
    while (1)
    {
        int choice;
        printf("1. Create\n2. Inorder\n3. Preorder\n4. Postorder \n5.Exit\n");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            create();
            break;
        case 2:
            inorder(root);
            break;
        case 3:
            preorder(root);
            break;
        case 4:
            postorder(root);
            break;
        case 5:
            exit(0);
            break;
        default:
            printf("Invalid Choice\n");
            break;
        }
    }
    return 0;
}