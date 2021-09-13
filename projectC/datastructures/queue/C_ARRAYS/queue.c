#include <stdio.h>
#include <stdlib.h>
#include "queue.h"

/*
 *return: void
 *args:
	size -> int -> size of the array
	arr -> double int pointer -> pointer
   	to the array
 *arr is pointer to the temparr, this array
 will have a size of (size)
 */
void intializeArray(int ***arr,int size){
	int **temparr = (int **)malloc(sizeof(int*) * size);
	// initialize all the elements in the
	// array to zero
	for (int i = 0; i < size; i++){
		temparr[i] = (int *)malloc(sizeof(int) * 2);
		for (int j = 0; j < 2; j++){
			temparr[i][j] = 0;
		}
	}
	*arr = temparr;
	return;
}

/*
 *return: void
 *args:
	size -> int -> size of the array
	arr -> array pointer
 *prints the array
 */
void printArray(int **arr, int size){
	for (int i = 0; i < size; i++){
		printf("element %d\n",arr[i][0]);
	}
}


/*
 * return: void
 * args:
	 arr -> double int pointer -> points to the array
	 size -> int -> size of array
 * removes the data to the rear of the array 
 */
void dequeue(int **arr, int size){
	/*
	 * checking if the first element is
	 * occupied if it isnt there is no 
	 * use of running the function
	 */
	 /* move all the contents
	  * to the left*/
	for (int i = 0; i < size - 1; i++){
		arr[i][0]=arr[i + 1][0];
	}
	arr[size - 1][0] = 0; 
	return;
}

/*
 * return: void
 * args:
	 size -> int -> size of array
	 arr -> double int pointer -> points to the array
	 value -> int -> value that need to added to the array	 
 * add data to the rear of the array 
 */
void enqueue(int **arr, int value, int size){
	/*
	 * checking if the rear element is
	 * full if its full dequeue the first
	 * element.
	 * arr (x, 0) -> not occupied
	 * arr (x, 1) -> occupied
	 */
	/*moving all the contents
	 * to the left*/
	int temp = arr[0][0];
	for (int i = 0; i < size - 1; i++){
		arr[i][0]=arr[i + 1][0];
	}
	arr[size -1][0] = value;
	return;
}

int main(int argc, char *argv[]){
	int **arr;
	int size = 4;
	intializeArray(&arr, size);
	enqueue(arr, 10, size);
	enqueue(arr, 10, size);
	enqueue(arr, 10, size);
	enqueue(arr, 1, size);
	printArray(arr, size);
	puts("---------------");
	dequeue(arr, size);
	printArray(arr, size);
}
