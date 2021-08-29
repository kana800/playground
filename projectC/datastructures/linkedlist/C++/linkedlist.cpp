#include <iostream>
#include "linkedlist.h"

// Initialize a node
// args: data -> number you want to include in your list
//		 index -> place you want to include your data
//       next -> next node
node::node(int data, int index){	
    // allocating data to the new index
	node::data = data;
	node::index = index;
	node::next = NULL;
}

// Initialize linkedlist
LinkedList::LinkedList(){
    headptr = NULL;
    tailptr = NULL;
}

// return int
// return the size of the array
int size(LinkedList list){
    int count;
    // checking if the head and tail is NULL
    if ((!list.headptr) && (!list.tailptr)) return -1;
    // temp head pointer
    node * temp = list.headptr;
    // iterate throught the linked list
    while (temp != NULL){
        count++;
        temp = temp->next;
    }
    return count;
}

// return int (bool)
// checks if the list is empty or not
int LinkedList::isEmpty(){
    // checking if the head and tail is NULL
    if ((!headptr) && (!tailptr)) return -1;
    return 1;
}

// return;
// pushes value to the front of the linked list
void LinkedList::push_front(LinkedList list, int value){
    // creating a node
    int index = 0;
    node *temp = new node(value, index);
    if ((!headptr) && (!tailptr)){
        headptr = temp;
        tailptr = temp; 
        return;
    }
    // linking the new head next with
    // the old head's pointer
    temp->next = headptr;
    headptr = temp;
    // grabbing the current pointer 
    // into a temp node
    node * temphead = headptr;
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

// return;
// prints the linked list
void LinkedList::print(LinkedList list){
	if ((!list.headptr) && (!list.tailptr)){
		std::cout << "EMPTY LINKED LIST\n";
		return;
	}
	node *temp_node = list.headptr;
	while (1){
		if (temp_node->next == NULL){
			printf("(%d,%d)->end\n",temp_node->index,temp_node->data);
			return;
		}
		printf("(%d,%d)->",temp_node->index,temp_node->data);
		temp_node = temp_node->next;
	}
}

// removes front item from the linked list
// and return its value
int LinkedList::pop_front(){
	node* newhead = headptr->next;
	int poppeditem = headptr->data;
	// overwrite new head with the old
	// head's pointer
	headptr = newhead;
	// reduce the index by one
	node *temphead = headptr;
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
void LinkedList::push_back(int value){
	// grabbing the current index from the tail pointer
	int index = tailptr->index;
	// creating a node
	node *temp_node = new node(value, index + 1);
	node *temptail = tailptr;
	if ((tailptr == NULL) && (headptr == NULL)){
		// checking if its a new
		// linked list
		headptr = temp_node;
		tailptr = temp_node;	
	}else{
		temptail->next = temp_node;
		tailptr = temp_node;
	}
}

//  removes the end item and
//  return its value
int LinkedList::pop_back(){
	int index = tailptr->index;
	int poppeditem = tailptr->data;
	// grab the address of the previous tail
	node* prevtail;
	node *temp_node = headptr;
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
	tailptr = prevtail;
	return poppeditem;
}

// return the front item
int LinkedList::front(){
	return headptr->data;
}

// return the end item
int LinkedList::back(){
	return tailptr->data;
}

// insert value at the given index
void LinkedList::insert(int index, int value){
	// creating a node
	node *temp_node = new node(value, index);
	if ((tailptr == NULL) && (headptr == NULL)){
		fprintf(stderr, "LINKEDLIST ISNT CREATED\n");
		return;
	}else{
		// checking if the given indexes are in range
		if ((headptr->index > index) || (tailptr->index < index)){
			fprintf(stderr, "INDEX OUT OF RANGE\n");
			return;
		}else if (index == 0){
			// check if the index value
			// is 0
			headptr->data = value;
		}else if (index == tailptr->index){
			// check if the index value
			// is MAX
			tailptr->data = value;
		}else{
			// within the index range
			// replace the earlier value with
			// new value
			node *temphead = headptr;
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
void LinkedList::erase(int index){
	// checking if the given indexes are in range
	if ((headptr->index > index) || (tailptr->index < index)){
		fprintf(stderr, "INDEX OUT OF RANGE\n");
		return;
	}else if (index == 0){
		// remove head
		pop_front();
	}else if (index == tailptr->index){
		// remove tail
		pop_back();
	}else{
		// create a node pointer and 
		// move the pointer until we
		// reach the desired index
		node *temphead = headptr;
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
void LinkedList::value_n_from_end(int n){
	int tailindex = tailptr->index;
	if (n > tailindex){
		fprintf(stderr, "INDEX OUT OF RANGE\n");
		return;
	}else if (n == 0){
		printf("value at %d-> %d",n,tailptr->data);
		return;
	}else{
		int index = tailindex - n;
		node *temphead = headptr;
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
void LinkedList::reverse(){
	if ((headptr == NULL) && (tailptr == NULL)){
		fprintf(stderr, "LINKEDLIST ISNT CREATED\n");
		return;
	}
	node *temp_node = headptr;
	node *node_ahead = NULL;
	node *node_passed = NULL;
	
	// changing tail
	tailptr = headptr;
	while (temp_node != NULL) {
		node_ahead = temp_node->next;
		// changing the current node pointer to before
		temp_node->next = node_passed;
		// node we passed becomes new node
		node_passed = temp_node;
		temp_node = node_ahead;
	}
	// changing head
	headptr = node_passed;
	// changing the indexes
	node *temphead = headptr;
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
void LinkedList::remove_value(int value){
	// create a node pointer and 
	// move the pointer until we
	// reach the desired index
	node *temphead = headptr;
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
