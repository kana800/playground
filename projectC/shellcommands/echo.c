/*
 * Implementation of Echo shell command
 * 
 * Display a line of text
 */
#include <stdio.h>
#include <stdlib.h>


int main(int argc, char **argv){

	int count = argc - 1;
	int i = 1;
	while (count >= i){
		printf("%s",argv[i]);	
		i++;
	}	
	printf("\n");

}
