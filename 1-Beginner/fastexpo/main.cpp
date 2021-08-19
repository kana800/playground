/*
 * Ask the user to enter 2 integers a and b and 
 * output a^b
 */
#include <iostream>
#include <string>
#include <sstream>
#include <math.h>

// a -> base and b -> exponent
int forpow(int a, int b){
	// simple iteration using for loop
	int p = a;
	for (int i = 1; i < b; i++){
		p *= a;
	}	
	return p;
}

int main(int argc, char *argv[]){

	//mystring is used to store the content
	//inputted by the user
	std::string mystr;
	int a,b;

	std::cout << "Enter A: ";
	//getline(stream, variable)
	getline(std::cin, mystr);
	//stringstream convert str into num
	std::stringstream(mystr) >> a;
	std::cout << "Enter B: ";
	//getline(stream, variable)
	getline(std::cin, mystr);
	//stringstream convert str into num
	std::stringstream(mystr) >> b;

	int answer = pow(a,b);
	printf("The power of %d^%d=%d \n",a,b, answer);
	return 0;
}
