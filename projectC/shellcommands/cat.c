/*
 * Implementation of Cat shell command
 * 
 * Display content inside a given file
 */
#include <stdio.h>
#include <stdlib.h>

#define BUFFER 1024

int main(int argc, char **argv){

	// if no files names are given
	// exit the program
	if (argc != 2){
		exit(0);	
	}

	FILE *fp; // file pointer
	char buffer[BUFFER];
	size_t read;

	// opening the file using fopen()
	fp = fopen(argv[1],"r");
	// check if the file exists
	if (fp == NULL){
		fprintf(stderr, "File Not Found");
		exit(-1);
	}else {
		char c;
		while ((read = fread(buffer, 1 , sizeof(buffer), fp)) > 0){
			fwrite(buffer, 1 , read, stdout);
		}
		fclose(fp);
	}

}
