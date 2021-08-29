#include <iostream>
#include "list.h"

// (constructor)
// Initialize the class with the 
// given capacity
List::List(int capacity){
	// maximum capacity of the array
	List::var_capacity = capacity;
	// initializing the length of the array
	List::var_len = 0;
	// initializing the data pointer of the arry
	List::data = (int*) malloc(capacity*sizeof(int));
}

// (destructor)
// Destroy the list by freeing its
// data
List::~List(){
	std::cout << "FREEING DATA"<< std::endl; 
	free(List::data);
}

// prints the list
void List::printlist(){
	int tSize = List::var_capacity;
	for (int i = 0; i < tSize; i++){
		std::cout << List::data[i] << '\t';
	}
	std::cout << std::endl;
}

// return;
// insert an item to the list using the given index
// returns error if the index is out of range
void List::insert(int index, int data){
	// check if the index is out of
	// range
	if (index > List::var_capacity - 1){
		fprintf(stderr, "Index out of range");
		return;
	}else {
		List::data[index] = data;
		// increment the length of the array
		List::var_len += 1;
	}
}

// return bool;
// check if the list is emoty
bool List::is_empty(){
	return List::var_len == 0;
}


// return int
// return the index of the item
int List::at(int index){
	if (index > List::var_capacity - 1){
		fprintf(stderr, "Index out of range");
		return -1;
	}else{
		return List::data[index];
	}
}

// return;
// insert an item to the list
void List::push(int item){
	// check if there is space in the array
	if (List::var_len >= List::var_capacity){
		// no space left
		// increment the current capacity
		int maxIndex = List::var_capacity;
		List::var_capacity += 1;
		// allocate the data to the end of the list
		insert(maxIndex, item);
	}else { 
		// increment the current capacity
		int maxIndex = List::var_len;
		// allocate the data to the end of the list
		insert(maxIndex, item);
	}
}

// return;
// remove item at given index
void List::deleteindex(int index){
	// checking if the index is over
	if (index > List::var_capacity - 1){
		fprintf(stderr, "Index out of range\n");
		return;
	}else {
		// move everything to left from the index value
		for (int i = index; i < List::var_capacity - 1; i++){
			List::data[i] = List::data[i + 1];
		}
		// allocating the last element as empty
		insert(0, List::var_capacity - 1);
		// reducing the len
		List::var_len -= 1;
	}
}
