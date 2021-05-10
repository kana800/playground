#include <stdio.h>

int option1(int *arr, int size, int k){
	
	// loop through the array
	for (int i = 0; i < size; i++){
		for (int j = 0; j < size; j++){
			if (arr[i]+arr[j] == k){
				return 0;
			}
		}
	}
	return 1;
}



int main() {
	
	// list of numbers
	int x[] = {10,15,3,7};
	int size = sizeof(x)/sizeof(x[0]);
	int k = 17;

	if (option1(x,size,k) == 0){
		printf("True");
	}
	

	return 0;
}
