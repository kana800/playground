/*
This file contains an implementation on
fat nodes from the paper making data 
structures persistent; This an implemenation of
partial persistent data structure
*/
#ifndef FATNODE_H
#define FATNODE_H

#include <stdio.h>
#include <stdlib.h>


#define DEBUG 1

typedef struct fatnode_ {
	int versionstamp; // current version stamp of the node
	float nodevalue; // current node value
	struct fatnode_* nextnode;
} fatnode;


typedef struct node_ {
	int versionstamp; // latest version stamp
	float nodevalue; // latest node value
	fatnode* m_fatnode; // fatnode pointer
} node;


void printNode(node* m) {
	/*summary: prints the node structure*/

	printf("Current Version %d: NodeValue %.2f\n",
		m->versionstamp, m->nodevalue);

	if (m->m_fatnode != NULL) {
		fatnode* temp_fn = m->m_fatnode;
		while (temp_fn != NULL) {
			printf("----Previous Version %d: NodeValue %.2f\n",
				temp_fn->versionstamp,
				temp_fn->nodevalue);
			temp_fn = temp_fn->nextnode;
		}
	}
	return;
}


node* createNodeStructure(float val) {
	/*summary: creates a node structure
	args:
		float val -> node value
	ret:
		pointer to a node;
	*/
	int initversion = 1;
	node* m = malloc(sizeof(node));
	m->m_fatnode = NULL;
	m->nodevalue = val;
	m->versionstamp = initversion;
	return m;
}

void freeNodeStructure(node* m) {
	/*summary: free the node structure and
	the fat node
	args:
		node* m -> pointer to the node that
		want to be freed
	*/

	// freeing the fatnodes
	fatnode* temp_fn = m->m_fatnode;
	fatnode* allocnode = NULL;
	while (temp_fn != NULL) {
		allocnode = temp_fn;
		temp_fn = temp_fn->nextnode;
		free(allocnode);
	}
	// freeing the node structure
	free(m);
}

void updateNodeStructure(float val, node* m) {
	/*summary: update the node structure
	args:
		node *m -> pointer to the node
		float val -> value of the node
	*/
	// creating a new fatnode
	fatnode* fn = malloc(sizeof(fatnode));
	
	// adding "previous node" values 
	fn->nextnode = NULL;
	fn->versionstamp = m->versionstamp;
	fn->nodevalue = m->nodevalue;

	if (m->m_fatnode == NULL) {
		m->m_fatnode = fn;
	}
	else {
		int count = 0;
		fatnode* temp_fn = m->m_fatnode;
		// iterating to the last node
		// which contains the last value
		while (temp_fn->nextnode != NULL) {
			printf("%d prev value %d %.2f\n",
				count,
				temp_fn->versionstamp,
				temp_fn->nodevalue);
			temp_fn = temp_fn->nextnode;
			count++;
		}
		temp_fn->nextnode = fn;
	}
	// updating the current node
	m->nodevalue = val;
	m->versionstamp++;
	return;
}


#endif // !FATNODE_H
