#include <stdio.h>
#include <stdlib.h>
#include "queue.h"


// head pointer to keep intrack of the head
node* head = NULL;
// tail pointer to keep intrack of the tail
node* tail = NULL;

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

// push node to the end of the list
void enqueue(int value){
	if ((tail == NULL) && (head == NULL)){
		// checking if its a new
		// linked list
		// creating a node
		int index = 0;
		node *temp_node = createnode(value, index);
		head = temp_node;
		tail = temp_node;
	}else{
		// grabbing the current index from the tail pointer
		int index = tail->index;
		// creating a node
		node *temp_node = createnode(value, index + 1);
		node *temptail = tail;
		temptail->next = temp_node;
		tail = temp_node;
	}
}

// checks if the queue is empty or not
int empty(){
	// checking if head and tail is NULL
	if ((!head) && (!tail)){
		return -1;	
	}else{
		return 1;
	}
}

// removes front item from the linked list
// and return its value
int dequeue(){
	node* newhead = head->next;
	int poppeditem = head->data;
	// overwrite new head with the old
	// head's pointer
	head = newhead;
	// reduce the index by one
	node *temphead = head;
	while (1){
		if (temphead->next == NULL){
			temphead->index -= 1;
			break;
		}
		temphead->index -= 1;
		temphead = temphead->next;
	}
	return poppeditem;
}

// prints the linkedlist
void print(){
	if ((head == NULL) && (tail == NULL)){
		printf("EMPTY QUEUE\n");
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


int main(int argc, char *argv[]){
	enqueue(5);
	print();
	enqueue(12);
	enqueue(13);
	enqueue(5);
	print();
	return 0;
}
