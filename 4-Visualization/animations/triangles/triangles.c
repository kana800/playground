#include <stdio.h>


void plotSquare(int w, int h){
	// printing the first lines	
	for (int i = 0; i <= w; ++i ){
		printf("#");
	}
	printf("\n");
	
	for (int i = 0; i < h - 1; i++){	
		// printing the border
		printf("#");
		// printing the spaces
		for (int i = 0; i < w - 1; ++i ){
			printf("o");
		}
		printf("#\n");
	}

	
	// printing the last lines
	for (int i = 0; i <= w; ++i ){
		printf("#");
	}

	printf("\n");

}

int main() {
	plotSquare(5,5);
	return 0;
}
