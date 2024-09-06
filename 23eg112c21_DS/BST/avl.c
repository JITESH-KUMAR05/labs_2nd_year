#include<stdio.h>
#include<stdlib.h>
struct Node{
	 int key;
	 struct Node *left;
	 struct Node *right;
	 int height;
};
struct Node*insert (struct Node*node,int key);
struct Node*new node(int key);
struct Node*right rotate(struct Node*y);
struct Node*left rotate(struct Node*x);
int main()
