#ifndef LINKEDLIST_H_
#define LINKEDLIST_H_

// struct for a node in a
// linked list
typedef struct node {
	int index;
	int data;
	struct node * next;
} node;


node * createnode(int data, int index); // returns a structure
int size(node* head); // returns the number of elements in the array
int isEmpty(node* head); // return 1 if the List is empty else return -1
int value_at(node* head, int index); // returns the value of the nth item (starting at 0 for first)
void push_front(int value);// adds an item to the front of the list
int pop_front();// remove front item and return its value
void push_back(int value);// adds an item at the end
int pop_back();// removes end item and returns its value
int front(); // get value of front item
int back(); // get value of end item
void insert(int index, int value); //insert value at index
void erase(int index); // removes node at given index
void value_n_from_end(int n);// returns the value of the node at nth position from the end of the list
void reverse(); // reverses the list
void remove_value(int value); // removes the first item in the list with this value
void print(); // prints the list


#endif //LINKEDLIST_H_
