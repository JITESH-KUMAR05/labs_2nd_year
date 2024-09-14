#include <stdio.h>
#include <stdlib.h>

// Structure for a node
struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};

// Function to create a new node
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

// Function to find the depth of a node
int findDepth(struct Node* root, int key, int depth) {
    if (root == NULL) {
        return -1; // Node not found
    }
    if (root->data == key) {
        return depth; // Node found, return the depth
    }
    int leftDepth = findDepth(root->left, key, depth + 1);
    int rightDepth = findDepth(root->right, key, depth + 1);
    if (leftDepth != -1) {
        return leftDepth; // Node found in the left subtree
    }
    if (rightDepth != -1) {
        return rightDepth; // Node found in the right subtree
    }
    return -1; // Node not found
}

// Main function
int main() {
    // Create a binary tree
    struct Node* root = createNode(1);
    root->left = createNode(2);
    root->right = createNode(3);
    root->left->left = createNode(4);
    root->left->right = createNode(5);
    root->right->left = createNode(6);
    root->right->right = createNode(7);

    int key = 5; // Node to find the depth of
    int depth = findDepth(root, key, 0);
    if (depth != -1) {
        printf("Depth of node %d is %d\n", key, depth);
    } else {
        printf("Node not found\n");
    }

    return 0;
}