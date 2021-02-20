/*
 *	Given a list of numbers and number k, return whether any two numbers from the list
 *	add up to k
 */
#include <stdio.h>


int iteration_through_list(int k, int *list, int size){
	
	for (int i=0; i < size; i++){
		for (int j = 0; j < size; j++){
			if (list[i] + list[j] == k){
				printf("True, Two number are %d + %d = %d\n",list[i],list[j], k );
				return 0;
			}	
		}
	}
	return 1;
}



int main() {
	int k = 17; // number that add up to
	int list[4] = {10, 15, 3, 7};
	
	if (iteration_through_list(k, list, 4) == 1){
		printf("False\n");
	}
	return 0;
}
