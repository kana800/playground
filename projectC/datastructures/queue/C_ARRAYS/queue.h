#ifndef QUEUE_H
#define QUEUE_H


int * initQueue(int size); // return an pointer to the array
int empty(); // return 1 if the List is empty else return -1
int dequeue();// remove front item and return its value
void enqueue(int *arr, int value);// adds an item at the end
void print(int *arr);

#endif //QUEUE_H
