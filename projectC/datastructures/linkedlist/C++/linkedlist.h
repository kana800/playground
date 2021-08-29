#ifndef LINKEDLIST_H_
#define LINKEDLIST_H_


class node{
    public: // variables
        int index;
        int data;
        node * next; // points to the next node
    public: // method
        node(int data, int index); // create a node
};

class LinkedList{
    public: // variables
        node * headptr;
        node * tailptr;
    public: // methods
        LinkedList();
        //~LinkedList();
        int size(); // returns the number of elements in the array
        int isEmpty(); // return 1 if the List is empty else return -1
        int value_at(int index); // returns the value of the nth item (starting at 0 for first)
        void push_front(LinkedList list, int value);// adds an item to the front of the list
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
        void print(LinkedList list); // prints the list
};
#endif //LINKEDLIST_H_