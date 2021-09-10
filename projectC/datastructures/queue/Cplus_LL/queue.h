#ifndef QUEUE_H
#define QUEUE_H

class node {
    public: // variables
        int index;
        int data;
        node * next;
    public: // methods
        // creates a node object
        node(int data, int index);
};

class LinkedList{
    public: // variables
        node * headptr;
        node * tailptr;
    public: // methods
        // constructor
        LinkedList();
        // destructor
        // ~LinkedList();
        int empty(); // return 1 if the list is empty else -1
        int dequeue(); // remove front item and returns its value
        void enqueue(LinkedList list,int value); // add an item at the end
        void print(LinkedList list); // prints the linked list
};

#endif // QUEUE_H