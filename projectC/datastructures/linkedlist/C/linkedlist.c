#include <stdio.h>
#include <stdlib.h>
#include "linkedlist.h"


// returns node struct pointer
// args: data -> number you want to include in your list
//		 index -> place you want to include your data
node* createnode(int data, int index){	
	// creating a temp node pointer
	// allocating in heap
	node *temp_node = malloc(sizeof(struct node));
	temp_node->data = data;
	temp_node->index = index;
	temp_node->next = NULL;
	return temp_node;
}

// pushes the nodes into the head
// args: node* head -> current head
//		 value -> (data)
void push_front(int value){
	// index = 0 because we are replacing the first index
	int index = 0;
	// creating a node
	node *temp_node = createnode(value, index);
	if ((tail == NULL) && (head == NULL)){
		// checking if its a new
		// linked list
		head = temp_node;
		tail = temp_node;	
		return;
	}else{
		// linking the new head next with
		// the old head's pointer
		temp_node->next = head;
		head = temp_node;
		node *temphead = head;
		int indexcounter = 0;
		while (1){
			if (temphead->next == NULL){
				temphead->index = indexcounter;
				break;
			}
			temphead->index = indexcounter;
			temphead = temphead->next;
			indexcounter++;
		}
	}
	return;
}

// removes front item from the linked list
// and return its value
void pop_front(){
	node* newhead = head->next;
	// overwrite new head with the old
	// head's pointer
	head = newhead;
	// reduce the index by one
	node *temphead = head;
	while (1){
		if (temphead->next == NULL){
			break;
		}
		temphead->index -= 1;
		temphead = temphead->next;
	}
}

// push node to the end of the list
void push_back(int value){
	// grabbing the current index from the tail pointer
	int index = tail->index;
	// creating a node
	node *temp_node = createnode(value, index);
	node *temphead = head;
	if ((tail == NULL) && (head == NULL)){
		// checking if its a new
		// linked list
		head = temp_node;
		tail = temp_node;	
	}else{
		temp_node->next = head;
		head = temp_node;
	}
	while (1){
		if (temphead->next == NULL){
			temphead->index += 1;
			break;
		}
		temphead->index += 1;
		temphead = temphead->next;
	}
	
}

// prints the linkedlist
void print(){
	if ((head == NULL) && (tail == NULL)){
		printf("EMPTY LINKED LIST\n");
		return;
	}
	node *temp_node = head;
	while (1){
		if (temp_node->next == NULL){
			printf("(%d,%d)->end\n",temp_node->index,temp_node->data);
			break;
		}
		printf("(%d,%d)->",temp_node->index,temp_node->data);
		temp_node = temp_node->next;
	}
}







int main(){
	push_front(8);
	push_front(18);
	print();
	pop_front();
	print();
}



