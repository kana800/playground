#pragma once

class List {
	private:
		// variables
		int var_capacity; // stores the capacity of the array
		int var_len; // stores the length of the array
		int *data; // pointer to array of data
	public:
		// methods
		List(int capacity);// constructor
		~List(); // destructor
		void printlist(); // prints the list
		int size(); // return the number of items
		int capacity(); // return the capacity of the list
		bool is_empty(); // return True if the list is empty else False
		int at(int index); // return item at the given index
		void push(int data); // insert a item
		void insert(int index, int data); // insert item at a given index
		void prepend(int item); // insert item at index 0
		void deleteindex(int index); // remove item at the given index
		void removeitem(int item); // looks for value and removes item hold the value
		int find(int item);// returns the first index with that value -1 if not found
};
