#ifndef LINKEDLIST_H_
#define LINKEDLIST_H_

// struct for a node in a
// linked list
typedef struct node {
	int index;
	int data;
	struct node * next;
} node;

// head pointer to keep intrack of the head
node* head = NULL;
// tail pointer to keep intrack of the tail
node* tail = NULL;

node * createnode(int data, int index); // returns a structure
int size(node* head); // returns the number of elements in the array
int isEmpty(node* head); // return 1 if the List is empty else return -1
int value_at(node* head, int index); // returns the value of the nth item (starting at 0 for first)
void push_front(int value);// adds an item to the front of the list
void pop_front();// remove front item and return its value
void push_back(int value);// adds an item at the end
void pop_back(node* head);// removes end item and returns its value
int front(node* head); // get value of front item
int back(node* head); // get value of end item
void insert(node* head, int index, int value); //insert value at index
void erase(node* head,int index); // removes node at given index
int value_n_from_end(node * head, int n);// returns the value of the node at nth position from the end of the list
void reverse(node * head); // reverses the list
void remove_value(node * haed , int value); // removes the first item in the list with this value
void print(); // prints the list


#endif //LINKEDLIST_H_
