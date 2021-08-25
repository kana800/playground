#ifndef LIST_H_
#define LIST_H_

// capacity for an empty list
// emptylist() -> returns an pointer to 
// empty list
int EMPTYCAPACITY=5;

// struct to hold the important information
// about the array like len
typedef struct listinfo{
	// stores the current length of list
	int len;
	// stores the maximum capacity of the list
	int maxCapacity;
	// stores the pointer to the list
	int *data;
} listinfo;

// forward declartion of the functions
// creates an empty list
listinfo * createEmptyList();
// create an list with given data
listinfo * createList(int size);
// appends data to the list
void appendData(listinfo * templist, int data);
// prints the list
void printlist(listinfo * templist);
// return size of the list
int size(listinfo *templist);
// return capacity of the list
int capacity(listinfo *templist);
// return if the list empty or not
int is_empty(listinfo *templist);
// insert item at index, shifts that index's value
// and trailing elements to the right
void insert(listinfo *templist, int data, int index);
// return end value from the list
int pop(listinfo *templist);
// delete item at the index, shift all trailing elements
// left
void deleteitem(listinfo *templist, int index);
// looks for value and removes index holding it (even if in multiple places)
void removeitem(listinfo *templist, int data);
//looks for value and returns first index with that value, -1 if not found
int finditem(listinfo *templist, int item);

#endif // LIST_H_
