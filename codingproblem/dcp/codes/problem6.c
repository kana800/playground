/*
 * Problem 6: XOR Linked List
*/
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

struct node *head = NULL;

struct node {
	int data;
	struct node* xorNode;
};

struct node* xorPointer(struct node* prev, struct node* next){
	uintptr_t temp = (uintptr_t)prev^(uintptr_t)next;
	struct node * ptr = (struct node *)temp;
	return ptr;
}

// creates a node
struct node* createNode(int num){
	struct node *tempnode = malloc(sizeof(struct node));

	tempnode->data = num;
	tempnode->xorNode = NULL;
}

// add a node to the tail
void add(int element){
	// if the list is empty
	struct node *tempnode = createNode(element);
	if (head == NULL){
		head = tempnode;
	} else {	
		// adding element to the list
		head->xorNode = xorPointer(tempnode, head);
		head = tempnode;	
	}
}

void printList(){
	
	struct node * temp = head;
	// next and prev pointer
	struct node * prev = NULL;
	struct node * next;

	while (temp != NULL){
		printf("%d\n",temp->data);
		next = xorPointer(prev, temp->xorNode);

		// changing the previous and next pointer
		prev = temp;
		temp = next;
	}
}


int main(int argc, char ** argv){

	head = NULL;
	add(5);
	add(3);

	printList();

	return 0;
}





