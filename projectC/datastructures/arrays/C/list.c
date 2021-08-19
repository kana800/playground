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
		fprintf(stderr, "Index out of range");
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
	// TODO: Implementation Here	
}

// return nothing
// prints the data in the given list
// args: listinfo pointer
void printlist(listinfo *templist){
	int size = templist->maxCapacity;
	for (int i = 0; i < size; i++){
		printf("%d ", templist->data[i]);
	}
	return;
}


int main(){
	createList(5);
}
