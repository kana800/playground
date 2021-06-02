/*
 * Best DataStructure would be a BinaryTree
 */

#include <stdio.h>
#include <stdlib.h>
#include "treeds.h"

struct node* create_node(int num){
	struct node *temp_node = malloc(sizeof(struct node));

	temp_node->data = num;
	temp_node->leftptr = NULL;
	temp_node->rightptr = NULL;
	return temp_node;
}

struct node* addToTree(struct node *root, int num){
	// root node not present
	if (root == NULL){
		// creating a node
		struct node *temp_node = create_node(num);
		return temp_node;
	}else if(num <= root->data){
		// recursion
		root->leftptr = addToTree(root->leftptr, num);
	}else {
		root->rightptr = addToTree(root->rightptr, num);
	}
	return root;
}

// prints the tree
void printTree(struct node*root){
	if (root == NULL){
		return;
	}
	printTree(root->leftptr);
	printf("%c ",root->data);
	printTree(root->rightptr);
}

int main(int argc, char *argv[]){
	char *c = "hello";
	// EMPTY TREE
	struct node* root = NULL;
	root = addToTree(root, (int)(c[0]));
	root = addToTree(root, (int)(c[1]));
	root = addToTree(root, (int)(c[2]));
	root = addToTree(root, (int)(c[3]));
	
	printTree(root);
	printf("\n");

	return 0;	
}
