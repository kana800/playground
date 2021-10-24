/*
 * Given a list of N integers, find its mean (as a double), maximum value, minimum value and range. Your program
 * will ask for N, then number of integers in the list, which the user will input. Then the user will input N more
 * numbers
 */
#include <iostream>
#include <list>
#include <iterator>
#include <algorithm>

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
double calculateMean(std::list <int> tlist){
    double sumofintegers;
    int numberofelements = tlist.size();

    std::list <int> :: iterator it;
    for (it = tlist.begin(); it != tlist.end(); it++){
        sumofintegers += *it;
    }
    double mean = sumofintegers / numberofelements;
    return mean; 
}

/*
 * returns the maximum element of the array
*/
int maxelement(std::list <int> tlist){
    int max = 0;
    std::list <int> :: iterator it;
    for (it = tlist.begin(); it != tlist.end(); it++){
        if (max < *it){
            max = *it;
        } 
    }
    return max;
}

/*
 * returns the minimum element of the list
*/
int minelement(std::list <int> tlist){
    int min = tlist.front();
    std::list <int> :: iterator it;
    for (it = tlist.begin(); it != tlist.end(); it++){
        if (min > *it){
            min = *it;
        } 
    }
    return min;
}

/*
 * return the range of the list
*/
int range(std::list<int> tlist){
    return maxelement(tlist) - minelement(tlist);
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
    std::cout << calculateMean(integerlist) << "\n";
    std::cout << "Max Element: " << maxelement(integerlist) << "\n";
    std::cout << "Min Element: " << minelement(integerlist) << "\n";
    std::cout << "Range: " << range(integerlist) << "\n";
}