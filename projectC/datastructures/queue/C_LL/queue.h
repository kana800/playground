#ifndef QUEUE_H
#define QUEUE_H

// struct for a node in a
// linked list
typedef struct node {
	int index;
	int data;
	struct node * next;
} node;

node * createnode(int data, int index); // returns a structure
int empty(); // return 1 if the List is empty else return -1
int dequeue();// remove front item and return its value
void enqueue(int value);// adds an item at the end

#endif //QUEUE_H
