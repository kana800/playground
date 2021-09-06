#include <stdio.h>
#include <stdlib.h>
#include "queue.h"

// int pointer to keep in track of head pointer
int *head;
// global var to store the size of the array
int ROWS;
int COLS;


// return an pointer to the 2darray
// args: s -> int -> size of the array
int * initQueue(int cols){
	COLS = cols;
	int rows = ROWS;
	int (*arr)[cols] = malloc(sizeof(*arr) * rows);
    if (arr) {
        // initialize the matrix
        for (int i = 0; i < cols; i++) {
			arr[i][rows] = 0;
        }
        return &arr[0][0];
    }
    return NULL;
}

// add an item to the array
// args: *arr -> pointer to the array
//		 value -> value that needs to
//		 be inserted
void enqueue(int * arr, int value){
	// check if the 
}

// print the array
void print(int * arr){
	int cols = COLS;
	int rows = ROWS;
	// typecasting the array into a
	// 2d array
	int (*temparr)[cols] = (int (*)[cols]) arr;
	for (int i = 0; i < cols; i++){
		printf("%d ",temparr[i][ROWS]);
	}
}

int main(){
	int ROWS = 1;
	int COLS = 5;
	int (*arr)[COLS] = (int (*)[COLS]) initQueue(COLS);
	print(&arr[0][0]);

}
