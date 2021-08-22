#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "list.c"


int main(int argc, char *argv[]){
	
	int n = 5;
	time_t t;
	srand((unsigned) time(&t));
	
	// creating a list with argc values
	listinfo * list = createList(n);

	printf("----------------------------\n");
	printf("checking if the list is empty\n");
	// checking if the list is empty
	if (is_empty(list)){
		printf("List is Not Empty\n");
	}else{
		printf("List is Empty\n");
	}

	printf("----------------------------\n");
	printf("allocating random numbers to the list\n");
	// allocating random numbers
	for (int i = 0; i < n; i++){
		int randomnumber = rand() % 50;
		allocateData(list,randomnumber,i);
	}

	// checking the capacity of list, this should be n
	printf("----------------------------\n");
	printf("checking capacity of the list\n");
	printf("capacity of the list is %d; n = %d\n", capacity(list), n);

	// appending an element to the list and checking its 
	// capacity, now it should be n + 1
	appendData(list, 75);
	printf("----------------------------\n");
	printf("checking capacity of the list\n");
	printf("capacity of the list is %d; n + 1 = %d\n", capacity(list), n + 1);

	// checking the length of the list, this should be n + 1
	printf("----------------------------\n");
	printf("checking length of the list\n");
	printf("length of the list is %d; n + 1 = %d\n", size(list), n + 1);

	// removing the appended item
	printf("----------------------------\n");
	printf("remove an appended item\n");
	// finding the index of the 75
	deleteitem(list, n);
	return 0;
}
