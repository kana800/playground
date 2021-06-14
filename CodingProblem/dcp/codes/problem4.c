/*
 * GIVEN AN ARRAY OF INTEGERS FIND THE FIRST MISSING POSITIVE INTEGER
 */
#include <stdio.h>
#include <stdlib.h>

// compare function for qsort
int compare(const void *a, const void *b){
	return *(int *)a - *(int *)b;
}

// returns the first positive index
int positiveIndex(int *arr, int n){
	for (int i = 0; i < n; i++){
		if (arr[i] > 0){
			return i;
		}
	}
}

// returns the missing positive integer
int missingPostiveInteger(int *arr, int size, int positiveIdx){
	// if the array starts from
	// a positive index
	int counter = 1;
	for (int i = positiveIdx; i < size; i++){
		if (counter != arr[i]){
			return counter;
		}else{
			counter++;
		}
	}

}

int main(int argc, char **argv){

	int arr[] = {3,4,-1,1};
	int n = sizeof(arr)/sizeof(arr[0]);

	qsort(arr, n, sizeof(int), compare);

	for(int i = 0; i < n; i++){
		printf("%d\n", arr[i]);
	}
	
	int p = positiveIndex(arr, n);

	int missingInteger = missingPostiveInteger(arr, n, p);
	printf("missing integer %d\n",missingInteger);

	return 0;
}
