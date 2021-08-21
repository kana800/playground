/*
 * Implementation of an array datastructure in the heap
 */

#include <stdio.h>
#include <stdlib.h>
#include "list.h"

// returns a pointer list struct
// creates an empty list
listinfo * createEmptyList(){
	// create a listinfo struct with an empty
	// list
	listinfo * templistinfo = malloc(sizeof(listinfo));
	// assiging the variables in the struct
	templistinfo->len = 0;		
	templistinfo->maxCapacity = EMPTYCAPACITY;
	templistinfo->data = (int *)malloc(
		   	sizeof(int) * EMPTYCAPACITY);
	// letting the user know that we created an list
	printf("%p -> []\n",templistinfo->data);
	return templistinfo;
}	

// return a pointer list struct
// create a list with given size
// args : size - size of the array
listinfo * createList(int size){
	// create a listinfo struct with an empty
	// list
	listinfo * templistinfo = malloc(sizeof(listinfo));
	// assiging the variables in the struct
	templistinfo->len = 0;		
	templistinfo->maxCapacity = size;
	templistinfo->data = (int *)malloc(
		   	sizeof(int) * size);
	// preallocating the data in the list with NULL values
	for (int i = 0; i < size; i++){
		templistinfo->data[i] = 0;
	}
	// letting the user know that we created an list
	printf("%p -> []\n",templistinfo->data);
	// print the list
	printlist(templistinfo);
	return templistinfo;
}

// return nothing
// allocate data to the given list
// args: listinfo pointer
//		 data - data of the given list
//		 index - index where you want to allocate the data
//		 i.e. allocateData(templist, 5, 0)-> [5,0,0,0,0]
void allocateData(listinfo *templist, int data, int index){
	// checking whether the given index is out of range
	if (index > templist->maxCapacity - 1){
		fprintf(stderr, "Index out of range\n");
		return;
	}else{
		templist->data[index] = data;
		// increment the length of the array
		templist->len += 1;
		// print the list
		printlist(templist);
	}
}

// returns nothing
// appends data to the list by copying the
// old values into a new one.
// args: listinfo pointer
//		data - value you want to append 
void appendData(listinfo *templist, int data){
	// check if there is space in the array
	if (templist->len >= templist->maxCapacity){
		// no space left
		// increment the current capacity
		int maxIndex = templist->maxCapacity;
		templist->maxCapacity += 1;
		// allocate the data to the end of the list
		allocateData(templist, data, maxIndex);
	}else { 
		// increment the current capacity
		int maxIndex = templist->len;
		// allocate the data to the end of the list
		allocateData(templist, data, maxIndex);
	}
}


// returns size of the list
// args: lisinfo pointer
int size(listinfo *templist){
	return templist->len;
}

// returns maximum capacity of the list
// args: listinfo pointer
int capacity(listinfo *templist){
	return templist->maxCapacity;
}

// returns 0 or 1, 0 if False, 1 if True
// checks if the list is empty
int is_empty(listinfo *templist){
	if (templist->len == 0){
		return 0;
	}else{
		return 1;
	}
}

// returns the data at the index value
void at(listinfo *templist, int index){
	if (index > templist->maxCapacity - 1){
		fprintf(stderr, "Index out of range\n");
		return;
	}else{
		printf("index : %d - data : %d \n",index,templist->data[index]);
		return;
	}
}

// inserts item at index, shifts that index's value
// and trailing elements to the right
void insert(listinfo *templist, int data, int index){
	// checking if the index is over
	if (index > templist->maxCapacity - 1){
		fprintf(stderr, "Index out of range\n");
		return;
	}else if (templist->len == templist->maxCapacity){
		// check if there is any space left in array
		fprintf(stderr, "Array is Full\n");
		return;
	} else {
		// move everything to the right
		for (int i = templist->len; i > 0; i--){
			templist->data[i] = templist->data[i - 1];
		}
		templist->data[index] = data;
	}
	printlist(templist);
}

// return int
// remove from end, return value
int pop(listinfo *templist){
	// obtain the final index
	int index = templist->len - 1;
	// replace the integer with zero
	int temp = templist->data[index];
	templist->data[index] = 0;
	return temp;
}

//delete item at index, shifting all trailing elements left
void deleteitem(listinfo *templist, int index){
	// checking if the index is over
	if (index > templist->maxCapacity - 1){
		fprintf(stderr, "Index out of range\n");
		return;
	}else {
		// move everything to left from the index value
		for (int i = index; i < templist->maxCapacity - 1; i++){
			templist->data[i] = templist->data[i + 1];
		}
		// allocating the last element as empty
		allocateData(templist,0,templist->maxCapacity - 1);
		// reducing the len
		templist->len -= 1;
	}
	printlist(templist);
}

// looks for value and removes index holding it (even if in multiple places)
void removeitem(listinfo *templist, int data){
	// looping through the array and removing the
	// item
	for (int i = 0; i < templist->len; i++){
		if (templist->data[i] == data){
			// mark them as null
			templist->data[i] = 0;
		}
	}
	printlist(templist);
}


//looks for value and returns first index with that value, -1 if not found
int finditem(listinfo *templist, int item){
	// looping through the array and removing the
	// item
	for (int i = 0; i < templist->len; i++){
		if (templist->data[i] == item){
			return i;
		}
	}
	return -1;
}

// return nothing
// prints the data in the given list
// args: listinfo pointer
void printlist(listinfo *templist){
	int size = templist->maxCapacity;
	for (int i = 0; i < size; i++){
		printf("%d ", templist->data[i]);
	}
	printf("\n");
	return;
}


int main(){
	listinfo * list = createList(5);
	allocateData(list,1,0);
	allocateData(list,2,2);
	allocateData(list,2,3);
	allocateData(list,2,3);
	allocateData(list,5,4);
	removeitem(list, 2);
}
