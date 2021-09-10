#include <iostream>
#include "queue.h"

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

// return int (bool)
// checks if the list is empty or not
int LinkedList::empty(){
    // checking if the head and tail is NULL
    if ((!headptr) && (!tailptr)) return -1;
    return 1;
}

// removes front item from the linked list
// and return its value
int LinkedList::dequeue(){
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


// return;
// pushes value to the front of the linked list
void LinkedList::enqueue(LinkedList list, int value){
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


int main(int argc, char *argv[]){
	// creating a linkedlist
	LinkedList list = LinkedList();
	list.enqueue(list, 5);
	list.print(list);
	list.enqueue(list, 3);
	list.enqueue(list, 13);
	list.print(list);
	list.dequeue();	
	list.print(list);


	return 0;
}