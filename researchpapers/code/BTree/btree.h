/*
This file contains implementation B-Tree (Order: 3)
- Every node has at most 3 children
- Every node has at most 2 keys
*/

#ifndef BTREE_H
#define BTREE_H

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>

#define MAX_KEYS 2

typedef struct node_ {
	int keys[MAX_KEYS]; /*pointer to the keys*/
	struct node_* children[MAX_KEYS + 1]; // pointer to the child tree
	int n_key; // current number of keys
	bool isLeaf; // leaf node or not
} node;

typedef struct tree_ {
	node* rootnode; // pointer to the rootnode
	int height; // height of the tree 
} btree;

node* createNode(bool isleaf) {
	/*summary: creates a node in the btree
	args:
	ret:
		node* -> pointer to a node
	*/
	node* tempnode = malloc(sizeof(node));
	tempnode->isLeaf = isleaf;
	return tempnode;
}

void printNodeKeys(node* n) {
	/*summary: print all the keys in a node
	args:
		node* n -> pointer to a node
	*/
	if (n->n_key == 0) {
		printf("Empty Tree\n");
	}
	else {
		for (int i = 0; i < n->n_key; i++) {
			printf("%d ", n->keys[i]);
		}
	}
	return;
}

node* splitChildren(node* n){
	/*summary: split the children
	of the node into two sections
	args:
		node* n -> pointer to a node
	*/
	node* newhalfparent = createNode(n->isLeaf);
	// keys and children are split between two parents
	int halfed = newhalfparent->n_key = n->n_key / 2;

	for (int i = 0; i < n->n_key; i++) {
		newhalfparent->keys[i] = 
			n->keys[halfed + i];
	}

	if (n->isLeaf) {
		for (int i = 0; i < n->n_key + 1; i++) {
			newhalfparent->children[i] = 
				n->children[halfed + i];
		}
	}

	n->n_key = halfed;
	return newhalfparent;
}

void traversalInsertion(btree* t, int k) {
	/*summary: insert a new key to the btree
	args:
		int k -> new key value
	*/
}

void insertnode(btree* t, int k) {
	/*summary: insert a new key to the btree
	args:
		int k -> new key value
	*/
	
	// empty tree
	if (t->rootnode == NULL) {
		// creating a leaf node and add
		// key k to the keys and increment
		// key count by one
		t->rootnode = createNode(true);
		t->rootnode->keys[0] = k;
		t->rootnode->n_key = 1;
	}
	else {
		// checking if the root is full
		if (t->rootnode->n_key == MAX_KEYS) {
			// create a new root node
			// child of newroot is going to 
			// be the old root and split the old 
			// root and move median key to the top
			node* newroot = createNode(false);
			// get the median value;
			newroot->keys[0] = t->rootnode->keys[1];
			node* new_parent = splitChildren(t->rootnode);
			newroot->children[0] = t->rootnode;
			newroot->children[1] = new_parent;
			t->rootnode = newroot;
		}
		else {

		}
	}
}

#endif // BTREE_H
