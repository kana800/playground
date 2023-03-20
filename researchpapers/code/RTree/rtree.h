/*
This file contains an implementation for RTree
- Minimum number of nodes in a node (m) -> 1
- Maximum number of nodes in a node (M) -> 2
- The nodes will be 2D
- The minimum point and maximum point of rectangle will 
be stored in a tuple
*/
#ifndef RTREE_H
#define RTREE_H

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdarg.h>

typedef struct rect_ {
	double x0;
	double x1;
	double y0;
	double y1;
	double area; // stores the area
} rect;

typedef struct node_ node;

typedef struct nodeentry_ {
	node** ptr;
	char repr;
	int count;
	bool isFull;
}childpointer;

typedef struct node_ {
	char repr; // character to represent the node
	bool leaf; // is it a leaf node
	struct childpointer* arr; // holds the child pointers
	struct rect_* rect; // rectangle that contain all the child pointers
} node;

typedef struct r_tree {
	int height; // height of the tree
	node* rootnode; // pointer to root node
} rtree;

rect* createBoundingBoxes(double x0, double y0, double x1, double y1) {
	/*summary: create a rectangle in the heap
	args:
		double x0, y0 -> coordinate points [point 1]
		double x1, y1 -> coordinate points [point 2]
	ret:
		rect -> pointer to a rectangle
	*/
	rect* t = malloc(sizeof(rect));
	t->x0 = x0;
	t->y0 = y0;
	t->x1 = x1;
	t->y1 = y1;
	// calculating the area of the tuple;
	t->area =  (x1 - x0) * (y1 - y0);
	return t;
}

childpointer* createChildPointerArray() {
	/*summary: creates a child pointer array in the heap
	note:
		maximum number of items in a array would be M; which
		is 2
	ret:
		childpointer* -> pointer to childpointer array
	*/
	childpointer* cparr = malloc(sizeof(cparr));
	node* n = malloc(sizeof(node) * 2);
	cparr->ptr = n;
	cparr->ptr[0] = NULL;
	cparr->ptr[1] = NULL;
	cparr->count = 0;
	cparr->isFull = false;
	return cparr;
}

void printChildPointer(childpointer* arr) {
	/*summary: prints the childpointers
	args:
		childpointer* arr -> pointer to the array
	*/
	if (arr != NULL) {
		printf("--childpointer 0\n\trect: %.2f %.2f %.2f %.2f\n",
			arr->ptr[0]->rect->x0,
			arr->ptr[0]->rect->y0,
			arr->ptr[0]->rect->x1,
			arr->ptr[0]->rect->y1);
		if (arr->isFull) {
			printf("--childpointer 1\n\trect: %.2f %.2f %.2f %.2f\n",
				arr->ptr[1]->rect->x0,
				arr->ptr[1]->rect->y0,
				arr->ptr[1]->rect->x1,
				arr->ptr[1]->rect->y1);
		}
	}
}

bool addChildPointer(childpointer* arr, node* n) {
	/*summary: add node to childpointer arr
	args:
		childpointer* arr -> pointer to the array
		node* n -> pointer to the node
	ret:
		true -> success
		false -> fail
	possible reasons for fail;
		array is full
	*/
	int currcount = arr->count;
	if (arr->isFull) {
		fprintf(stderr, "child pointer array is full\n");
		return false;
	}
	arr->ptr[currcount] = n;
	arr->count++;
	if (arr->count > 1) arr->isFull = true;
	return true;
}

node* getBiggestChildNode(childpointer* cp) {
	/*summary: return the biggest node in the
	childpointer
	args:
		childpointer* cp -> pointer childpointer array
	ret:
		node * -> pointer to a node
	*/

	// if not full; return the
	// first node
	if (!cp->isFull) {
		return cp->ptr[0];
	}
	node* n1 = cp->ptr[0];
	node* n2 = cp->ptr[1];
	return n1->rect->area >
		n2->rect->area ? n1 : n2;
}

node* getSmallestChildNode(childpointer* cp) {
	/*summary: return the smallest node in the
	childpointer
	args:
		childpointer* cp -> pointer childpointer array
	ret:
		node * -> pointer to a node
	*/
	// if not full; return the
	// first node
	if (!cp->isFull) {
		return cp->ptr[0];
	}
	node* n1 = cp->ptr[0];
	node* n2 = cp->ptr[1];
	return n1->rect->area <
		n2->rect->area ? n1 : n2;
}

node* getCompatibleChildNode(childpointer* cp, rect* r) {
	/*summary: return the compatible child node for the
	rect *r
	args:
		childpointer* cp -> pointer childpointer array
	ret:
		node * -> pointer to a node
	*/

	// loop through all the child node [2] and then
	// obtain the node that make smallest rect
	double difference = 0;
	double prev_diff = cp->ptr[0]->rect->area;
	int arrindex = 0;
	// calculate input rect length and width
	//double input_length = r->x1 - r->x0;
	//double input_width = r->y1 - r->y0;
	for (int i = 0; i < 2; i++) {
		// area of the rectangle
		double a = cp->ptr[i]->rect->area;
		//double length = cp->ptr[i]->rect->x1
		//	- cp->ptr[i]->rect->x0;
		//double width = cp->ptr[i]->rect->y1
		//	- cp->ptr[i]->rect->y0;
		if (r->area > a) {
			// if input area is greater 
			// than current rect area skip
			continue;
		}
		else {
			difference = a - r->area;
			if (prev_diff > difference) {
				arrindex = i;
				prev_diff = difference;
			}
		}
	}
	return cp->ptr[arrindex];
}

void printNode(node* n) {
	/*summary: prints the node
	args:
		node* n
	*/
	if (n == NULL) {
		return;
	}
	printf("----------------------------------\n");
	printf("node %c: rect %.2f %.2f %.2f %.2f\n",
		n->repr,n->rect->x0,
		n->rect->x1,n->rect->y0,n->rect->y1);
	childpointer* c = n->arr;
	printChildPointer(c);
	printf("----------------------------------\n");
	return;
}

node* createNode(char repr, bool leaf, ...) {
	/*summary: create a node in the heap
	args:
		char* repr -> representation character of the node
		bool leaf -> is the node a leaf
	optional args:
			rect* -> pointer to a rect
			node* -> pointer for the child pointer
	ret:
		node* -> pointer to a node
	*/
	node* n = malloc(sizeof(node));
	n->repr = repr;
	// obtaining rect value
	va_list parameters;
	va_start(parameters, leaf);
	if (leaf) {
		n->rect = va_arg(parameters, struct rect_ *);
		va_end(parameters);
		// no child pointer for leaf node
		n->arr = NULL;
		n->leaf = true;
	}
	else {
		n->arr = createChildPointerArray();
		node* tempnode = va_arg(parameters, struct node_ *);
		addChildPointer(n->arr, tempnode);
		n->rect = tempnode->rect;
		n->leaf = false;
		va_end(parameters);
	}
	return n;
}

node* convertLeafNodeToNode(node* n) {
	/*summary: convert to leaf node
	args:
		node* n -> pointer to leaf node
	ret:
		node* -> pointer to a node with 
		child pointers
	*/
	// not a leafnode
	if (n->arr != NULL) {
		return n;
	}
	// creating child pointer
	n->arr = createChildPointerArray();
	return n;
}

rtree* createRTree() {
	/*summary: creates a r-tree in the heap; since the dimension is 2 
	this function doesnt much of use but we are going to use it anyways
	ret:
		rtree* -> pointer to a rtree
	*/
	rtree* r = malloc(sizeof(rtree));
	r->height = 0;
	r->rootnode = NULL;
	return r;
}

void printRTree(rtree* r) {
	/*summary: prints the rtree*/
	node* tempNode = r->rootnode;
	// printing biggest nodes
	while (tempNode != NULL) {
		printNode(tempNode);
		if (tempNode->arr == NULL) break;
		tempNode = getBiggestChildNode(tempNode->arr);
	}

	return;
}

void adjustNodeRect(node* n) {
	/*summary: Adjust the size of the node
	args:
		node* n -> pointer to a node
	*/
	// checking if the current rect
	// is already big enough
	node* tempNode = getBiggestChildNode(n->arr);
	if (tempNode->rect->area 
		>= n->rect->area) {
		n->rect = tempNode->rect;
	} 
	return;
}

void insert(rtree* r, char* repr, rect* rect) {
	/*summary: inserts the node to the tree structure
	args:
		rtree* r -> rtree
		char* repr -> representation of the node
		rect* rect -> rectangle
	*/

	// no root nodes present is rtree
	if (r->rootnode == NULL) {
		// rect will be added as the child pointer in
		// to the rtree and the rect in node will be
		// pointed to the rect
		node* rectNode = createNode(repr, true, rect);
		r->rootnode = createNode(repr, false, rectNode);
		return;
	}

	node* tempNode = r->rootnode;
	// traversing the child pointers 
	while (tempNode != NULL) {
		childpointer* tempcp = tempNode->arr;
		if (tempcp == NULL) {
			// no childpointer are present
			// currently tempnode is a leafnode
			convertLeafNodeToNode(tempNode);
			node* tempLeaf = createNode(repr, true, rect);
			addChildPointer(tempNode->arr, tempLeaf);
			break;
		}
		else if (!tempcp->isFull) {
			// not full; add it to the child pointer and
			// adjust the node's rect
			// creating a leaf node
			node* tempLeaf = createNode(repr, true, rect);
			addChildPointer(tempcp, tempLeaf);
			adjustNodeRect(tempNode);
			break;
		}
		// selecting next child pointer
		tempNode = getCompatibleChildNode(tempcp, rect);
	}
	return;
}


#endif // !RTREE
