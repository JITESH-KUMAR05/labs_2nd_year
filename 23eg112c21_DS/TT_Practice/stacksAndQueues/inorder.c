#include<stdio.h>
#include<stdlib.h>

struct node{
    int data;
    struct node *left;
    struct node *right ;
    
};
int s = 0;

struct node *root = NULL;
struct node * create(int x){
    struct node *nn;
    nn = (struct node *)malloc(sizeof(struct node));
    nn->data = x;
    nn->left = NULL;
    nn->right = NULL;
    return nn;
}

int inorder(struct node *ro){
    if(ro != NULL){
        inorder(ro->left);
        printf("%d ",ro->data);
        inorder(ro->right);
    }

}

int preorder(struct node *ro){
    if(ro != NULL){
        printf("%d ",ro->data);
        preorder(ro->left);
        preorder(ro->right);
    }
}

int postorder(struct node *ro){
    
    if(ro != NULL){
        
        postorder(ro->left);
        postorder(ro->right);
        printf("%d ",ro->data);
        s = s+ro->data;
        // return s;
        
    }

}
int sum(struct node *ro){
    // int s=0;
    if(ro==NULL){
        return 0;
    }
    return ro->data + sum(ro->left) + sum(ro->right);
}

int evensum(struct node *ro){
    int s = 0;
    if(ro == NULL){
        return 0;

    }
    else{
        if(ro->data %2 == 0){
            // s += 


        }
    }
}

int main(){
    root = create(10);
    root->left = create(5);
    root->right = create(15);
    root->left->right= create(8);
    root->right->right = create(20);
    root->left->left = create(3);
    inorder(root);
    printf("\n");
    preorder(root);
    printf("\n");
    postorder(root);
    printf("\n");
    // printf("%d",sum(root));
    // printf("%d",s);
    printf("\n");
    printf("%d",sum(root));
    return 0;
}