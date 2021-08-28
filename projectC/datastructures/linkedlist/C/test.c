#include <stdio.h>
#include <stdlib.h>
#include "linkedlist.c"

int main(){
	puts("---------------------------------");
	puts("creating an linked list");
	for (int i = 23; i < 35; i++){
		push_front(i);
	}
	// printing the linked list
	print();
	puts("---------------------------------");
	puts("testing pop_front & pop_back");
	int front = pop_front();
	printf("Output from pop_front() -> %d\n", front);
	printf("Output should be -> %d\n", 34);
	int back = pop_back();
	printf("Output from pop_back() -> %d\n", back);
	printf("Output should be -> %d\n", 23);
	puts("---------------------------------");
	return 0;
}



