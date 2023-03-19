#include <iostream>
#include <string.h>

using std::cout;

#define multiply(x, y) x * y
#define maximum(x,y) x > y ? x : y
#define factorial(x) ((x) * factorial((x) - 1))

void swap(int &r1, int &r2){
	/*summary: swap two numbers
	 * question 2.19*/
	int t = r1;
	r1 = r2;
	r2 = t;
}

void swap2(int* r1, int* r2){
	/*summary: swap two numbers
	 * question 2.19*/
	int* temp = r1;
	r1 = r2;
	r2 = temp;
}

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
	//std::cout << sizeof(int) << "\t" <<alignof(int) <<std::endl;
	//std::cout << sizeof(long) << "\t"<< alignof(long) <<std::endl;
	//std::cout << sizeof(float) << "\t"<< alignof(float) <<std::endl;
	//std::cout << sizeof(double) << "\t"< alignof(double) <<std::endl;
	int d = 4;
	int e = 5;
	swap(d,e);
	//swap2(d1, e1);
	//cout << "Hello World\n" << std::endl;	
	
	int m = multiply(2, 2);
	int k = maximum(2, 5);
	int q = factorial(2);

	cout << "k is " << k << std::endl;
	cout << "m is " << m << std::endl;

	return 0;
}
