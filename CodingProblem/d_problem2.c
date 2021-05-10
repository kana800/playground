#include <stdio.h>

void printarr(int *arr, int size){
	
	for (int i = 0; i < size; i++){
		printf("%d -",arr[i]);
	}
}

int productofarr(int *arr, int size){
	int sum = 1;
	for (int i = 0; i < size; i++){
		sum *= arr[i];
	}
	return sum;
}

void productarr(int *arr, int size){
	int product = productofarr(arr,size);
	for (int i = 0; i < size; i++){
		arr[i] = product / arr[i];
	}
}

int main(){

	int arr[] = {1,2,3,4,5};
	int size = sizeof(arr)/sizeof(arr[0]);
	productarr(arr,size);
	printarr(arr,size);
	return 0;

}
