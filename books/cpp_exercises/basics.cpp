#include <iostream>
#include <string.h>

int main(int argc, char* argv[]){


	/*question 11.1 : check what is wrong with code fragments 
	 * const char a = 'a';
	 * char *c = &a;*/
	const char a = 'a';
	const char *c = &a;
	/*
	 * const int i = 42;
	 * auto &j = i;
	 * ++j;
	 */
	const int i = 42;
	auto &j = i;
	/*question 12 : check what is the size of the array*/
	char s[] = "Hello";
	/*question 13: state the type of each of the following objects*/
	auto&& p = 0;
	/*question 16: print size and alignment of the variables*/
	std::cout << sizeof(int) << "\t" <<alignof(int) <<std::endl;
	std::cout << sizeof(long) << "\t"<< alignof(long) <<std::endl;
	std::cout << sizeof(float) << "\t"<< alignof(float) <<std::endl;
	std::cout << sizeof(double) << "\t"< alignof(double) <<std::endl;
	return 0;
}
