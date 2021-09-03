#include <stdio.h>
#include <stdlib.h>
#include "linkedlist.h"

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
int pop_front(){
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

// push node to the end of the list
void push_back(int value){
	// grabbing the current index from the tail pointer
	int index = tail->index;
	// creating a node
	node *temp_node = createnode(value, index + 1);
	node *temptail = tail;
	if ((tail == NULL) && (head == NULL)){
		// checking if its a new
		// linked list
		head = temp_node;
		tail = temp_node;	
	}else{
		temptail->next = temp_node;
		tail = temp_node;
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

//  removes the end item and
//  return its value
int pop_back(){
	int index = tail->index;
	int poppeditem = tail->data;
	// grab the address of the previous tail
	node* prevtail;
	node *temp_node = head;
	while (1){
		if (temp_node->index == index - 1){
			prevtail = temp_node;
			break;
		}else if (temp_node->next == NULL){
			fprintf(stderr, "UNABLE TO POP ITEM\n");
			return -1;
		}
		temp_node = temp_node->next;
	}
	// replacing prevtail's next pointer with null
	prevtail->next = NULL;
	// replacing the global tail's address with the new tails one
	tail = prevtail;
	return poppeditem;
}

// return the front item
int front(){
	return head->data;
}

// return the end item
int back(){
	return tail->data;
}

// insert value at the given index
void insert(int index, int value){
	// creating a node
	node *temp_node = createnode(value, index);
	if ((tail == NULL) && (head == NULL)){
		fprintf(stderr, "LINKEDLIST ISNT CREATED\n");
		return;
	}else{
		// checking if the given indexes are in range
		if ((head->index > index) || (tail->index < index)){
			fprintf(stderr, "INDEX OUT OF RANGE\n");
			return;
		}else if (index == 0){
			// check if the index value
			// is 0
			head->data = value;
		}else if (index == tail->index){
			// check if the index value
			// is MAX
			tail->data = value;
		}else{
			// within the index range
			// replace the earlier value with
			// new value
			node *temphead = head;
			while (1){
				if (temphead->index == index){
					temphead->data = value;
					break;
				}else if (temphead->next == NULL){
					// if we dont find the index
					// exit after exhaustion
					fprintf(stderr, "UNABLE TO POP ITEM\n");
					return;
				}
				temphead = temphead->next;
			}
		}
	}
	return;
}

// removes node from the given index
void erase(int index){
	// checking if the given indexes are in range
	if ((head->index > index) || (tail->index < index)){
		fprintf(stderr, "INDEX OUT OF RANGE\n");
		return;
	}else if (index == 0){
		// remove head
		pop_front();
	}else if (index == tail->index){
		// remove tail
		pop_back();
	}else{
		// create a node pointer and 
		// move the pointer until we
		// reach the desired index
		node *temphead = head;
		node *prevtail;
		while (1){
			if (temphead->index == index){
				break;
			}else if (temphead->index == index - 1){
				// grabbing the index of the previous
				// value
				prevtail = temphead;
			}else if (temphead->next == NULL){
				// if we dont find the index
				// exit after exhaustion
				fprintf(stderr, "UNABLE TO REMOVE ITEM\n");
				return;
			}
			temphead = temphead->next;
		}
		// replace the previous tail next pointer
		// to the temphead's next pointer
		prevtail->next = temphead->next;	
		return;
	}	
	return;
}

// return the value of the node
// at the nth posistion from the
// end of the list
void value_n_from_end(int n){
	int tailindex = tail->index;
	if (n > tailindex){
		fprintf(stderr, "INDEX OUT OF RANGE\n");
		return;
	}else if (n == 0){
		printf("value at %d-> %d",n,tail->data);
		return;
	}else{
		int index = tailindex - n;
		node *temphead = head;
		while (1){
			if (temphead->index == index){
				break;
			}else if (temphead->next == NULL){
				// if we dont find the index
				// exit after exhaustion
				fprintf(stderr, "UNABLE TO POP ITEM\n");
				return;
			}
			temphead = temphead->next;
		}
		printf("value at %d-> %d",n,temphead->data);
	}
	return;
}

// reverse the list
void reverse(){
	if ((head == NULL) && (tail == NULL)){
		fprintf(stderr, "LINKEDLIST ISNT CREATED\n");
		return;
	}
	node *temp_node = head;
	node *node_ahead = NULL;
	node *node_passed = NULL;
	
	// changing tail
	tail = head;
	while (temp_node != NULL) {
		node_ahead = temp_node->next;
		// changing the current node pointer to before
		temp_node->next = node_passed;
		// node we passed becomes new node
		node_passed = temp_node;
		temp_node = node_ahead;
	}
	// changing head
	head = node_passed;
	// changing the indexes
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
	return;
}

// remove the first item in the list
// with the value
void remove_value(int value){
	// create a node pointer and 
	// move the pointer until we
	// reach the desired index
	node *temphead = head;
	int index;
	while (1){
		// found the item
		if (temphead->data == value){
			index = temphead->index;
			break;
		}else if (temphead->next == NULL){
			// if we dont find the index
			// exit after exhaustion
			fprintf(stderr, "UNABLE TO REMOVE ITEM\n");
			return;
		}
		temphead = temphead->next;
	}
	erase(index);
	return;
}	
