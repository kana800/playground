/*
 * Given a list of N integers, find its mean (as a double), maximum value, minimum value and range. Your program
 * will ask for N, then number of integers in the list, which the user will input. Then the user will input N more
 * numbers
 */
#include <iostream>
#include <list>
#include <iterator>

void showlist(std::list <int> tlist){
    std::list <int> :: iterator it;
    for (it = tlist.begin(); it != tlist.end(); it++){
        std::cout << "\t" << *it;
    }
    std::cout << "\n";
}

/*
 * calculates the mean of a given list
 * return -> int
*/
int calculateMean(std::list <int> tlist){
    double sumofintegers;
    int numberofelements = tlist.size();

    std::list <int> :: iterator it;
    for (it = tlist.begin(); it != tlist.end(); it++){
        sumofintegers += *it;
    }
    double mean = sumofintegers / numberofelements;
    return mean; 
}

int main(int argc, char *argv[]){
    
    /*asking the user for N*/
    int n;
    std::cout << "Enter N: ";
    std::cin >> n;

    std::list<int> integerlist;
    for (int i = 0; i < n; i++){
        int tempn;
        std::cin >> tempn;
        integerlist.push_back(tempn);
    }
    showlist(integerlist);
    std::cout << calculateMean(integerlist);
}
