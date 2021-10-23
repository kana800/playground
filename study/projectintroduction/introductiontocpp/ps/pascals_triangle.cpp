/*
* prints the pascal triangle using recursion
*/
#include <iostream>

/*
* params:
*   n -> nth row of the pascal triangle
*   k -> kth col of the pascal triangle
*/
int printPascalTriangle(int n, int k){
    if (k == 0){
        return 1;
    }else if (n == 0) {
        return 0;
    }else {
        return printPascalTriangle(n - 1, k) + printPascalTriangle(n - 1, k - 1);
    }
}


int main(int argc, char **argv){
    std::cout << printPascalTriangle(2, 2);
    return 0;
}