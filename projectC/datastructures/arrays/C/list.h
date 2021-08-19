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

#endif // LIST_H_
