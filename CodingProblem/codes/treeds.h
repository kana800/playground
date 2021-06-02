#ifndef TREEDS_H
#define TREEDS_H

// node struct
struct node {
	int data;
	struct node *leftptr;
	struct node *rightptr;	
};

// foward declaration of the functions
struct node* create_node(int num);
struct node* addToTree(struct node *root, int num);
void printTree(struct node*root);

#endif
