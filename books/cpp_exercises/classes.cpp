#include <iostream>


/*exercise 3*/
class Counter {
public:
	Counter(int c){
		counter = c;
		counterExistence++;
	}

	~Counter(){
		counterExistence++;
	}

	int getValue() const {
		return counter;
	}

	Counter& operator++(int) {
		counter++;
		return *this;
	}

	Counter& operator--(int) {
		counter--;
		return *this;
	}
	
	int getCounterExistence() const {
		return counterExistence;
	}

private:
	static int counterExistence; 
	int counter = 0;
};

int Counter::counterExistence = 0;

int main(){
	Counter c(1);
	Counter j(2);
	c++;
	j--;
	std::cout << c.getValue() << std::endl;
	std::cout << j.getValue() << std::endl;
	std::cout << c.getCounterExistence() << std::endl;
}
