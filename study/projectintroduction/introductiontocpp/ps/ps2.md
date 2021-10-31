2. A Simple Function

   > What would the following program print out?
   >
   > ```cpp
   > void f(const int a = 5){
   >     std::cout << a * 2 << "\n";
   > }
   > 
   > int a = 123;
   > int main(){
   >     f(1); // 2
   >     f(a); // 246
   >     int b = 3;
   >     f(b); // 6
   >     int a = 4;
   >     f(a); // 8
   >     f(); // 10
   > }
   > ```

3. Fix the Function

   > Identify the errors in the following programs, and explain how you would correct them to make them do what they were apparently meant to do.
   >
   > 1. ```cpp
   >    #include <iostream>
   >    
   >    int main(){
   >        printNum(35);
   >        return 0;
   >    }
   >    void printNum(int number) { std::cout << number; }
   >    ```
```cpp
#include <iostream>

int main(){
    printNum(35);
    return 0;
}
void printNum(int number) { std::cout << number; }
```

we can use the function declaration (prototyping) 

```cpp
#include <iostream>

void printNum(int number);

int main(){
    printNum(35);
    return 0;
}
void printNum(int number) { std::cout << number; }
```

we can move the `printNum` function above the `main` function.

> 2. ```cpp
>    #include <iostream>
>    void printNum() { std::cout << number; }
>    
>    int main(){
>    	int number = 35;
>        printNum(number);
>        return 0;
>    }
>    ```

we need to make sure that the function accepts arguments.

```cpp
void printNum(int number) { std::cout << number; }
```

make  `number` variable a global variable. Move it outside the `main` function

> 3. ```cpp
>    #include <iostream>
>    
>    void doubleNumber(int num){num = num * 2;}
>    
>    int main(){
>    	int num = 35;
>        doubleNumber(num);
>        std::cout << num; // should print 70
>        return 0;
>    }
>    ```

we can pass the address of the variable `num`

```cpp
#include <iostream>

void doubleNumber(int * num){num = num * 2;}

int main(){
	int num = 35;
    doubleNumber(&num);
    std::cout << num; // should print 70
    return 0;
}
```

> 4. ```cpp
>    #include <iostream>
>    #include <cstdlib> // contains some math functions
>    
>    int difference(const int x, const int y){
>        int diff = abs(x - y); // abs(n) returns absolute value of n
>    }
>    
>    int main(){
>        std::cout << difference(24, 1238);
>        return 0;
>    }
>    ```

```cpp
#include <iostream>
#include <cstdlib> // contains some math functions

int difference(const int x, const int y){
    int diff = abs(x - y); // abs(n) returns absolute value of n
	return diffl;
}

int main(){
    std::cout << difference(24, 1238);
    return 0;
}
```

> 5. ```c++
>    #include <iostream>
>    
>    int sum(const int x, const int y){
>        return x + y;
>    }
>    
>    int main() {
>        std::cout << sum(1,2,3); //should print 6
>        return 0;
>    }
>    ```

Add the three arguments together

```cpp
#include <iostream>

int sum(const int x, const int y, const int z){
    return x + y + z;
}

int main() {
    std::cout << sum(1,2,3); //should print 6
    return 0;
}
```

> 6. ```cpp
>    #include <iostream>
>    
>    const int ARRAY_LEN = 10;
>    
>    int main(){
>        int arr[ARRAY_LEN] = {10}; // Note implicit initialization of 
>        						   // other elements
>        int *xPtr = arr, yPtr = arr + ARRAY_LEN - 1;
>        std::cout << *xPtr << " " << *yPtr; // should output 10 0
>    }
>    ```

There should `*` symbol in the variable `yPtr`

4.  Sums

   > Make sure to use `const` arguments where appropriate throughout this problem (and all the others).

   > 1. Write a single `sum` function that returns sum of two integers. Also write the equivalent function for taking the sum of two `doubles`.

   ```cpp
   int sum(const int num1, const int num2){
       return num1 + num2;
   }
   
   double sum(const double num1, const double num2){
       return num1 + num2;
   }
   ```

   > 2. Explain why, given your functions from part 1, `sum(1, 10.0)` is a syntax error. 

   Since we have two function with the same name mixing the variable types will confuse the compiler on which function to call.

   > 3. Write 2 more functions such that you can find the sum of anywhere between 2 and 4 integers by writing `sum(num1, num2, ...)`.

   ```cpp
   int sum(const int a, const int b, const int c){
       return a + b + c;
   }
   
   int sum(const int num1, const int num2, const int num3, const int num4){
       return num1 + num2 + num3 + num4;
   }
   ```

   > 4. Now write just one function, using default arguments, allows you to take the sum of anywhere between 2 and 4 integers. What would happen if you put both this definition and you 3-arguments from part 3 into the same file, and called `sum(3,5,7)`? Why?

   ```cpp
   int sum(const int num1 = 0, const int num2 = 0, const int num3 = 0, const int num4 = 0){
       return num1 + num2 + num3 + num4;
   }
   ```

   Compiler would get confused on which function to call.
   
   > 5. Write a single **sum** capable of handling an arbitrary number of integers. It should take two arguments, include a loop, and return an integer. (Hint: What data types can you use to represent an arbitrarily large set of integers in two arguments?)
   
   ```c++
   int sum(const int numberlist[], const int length){
       int sum = 0;
       for (int i = 0; i < length; i++){
           sum += numberlist[i];
       }
       return sum;
   }
   ```
   
   > 6. Now rewrite your function from 5 to use recursion instead of a loop. The function signature should not change.
   
   ```cpp
   int sum(const int numberlist[], const int len){
   	if (len == 0){
           return 0;
       }else { 
       	return numberlist[0] + sum(numberlist + 1, len - 1);
       }
   }
   ```
   
5.  Calculating ![](https://latex.codecogs.com/png.latex?%5Cinline%20%5Cpi)

    > 1. Define variables to store the x and y coordinates of a particular dart throw. Initialize them to random **doubles** in range `[0, 1]`(simulating one dart throw)

    ``` cpp
    #include <cstdlib>;
    
    #define RAND_MAX 1
    
    double x = rand() % RAND_MAX;
    double y = rand() % RAND_MAX;
    ```

    > 2. Place your x and y declarations in a loop in simulate multiple dart throws. Assume you have a variable in **n** indicating how many throws to simulate. Maintain a count of how many darts have ended up inside the circle.

    ```cpp
    #include <cmath>
    
    int n = 5; /*number of throws that you need to simulate*/
    int throwsinsidecircle = 0;
    for (int i = 0; i < n; i++){
        double x = rand() % RAND_MAX;
    	double y = rand() % RAND_MAX;
        double d = sqrt((x**2) + (y**2));
        if (d < 1){
            throwsinsidecircle++;
        }
    }
    ```

    > 3. Now use your loop to build a ![](https://latex.codecogs.com/png.latex?%5Cinline%20%5Cpi)-calculating function. The function should take one argument specifying the number of dart throws to run. It should return the decimal value of pi. using the technique outline above.

    ```cpp
    double pi(int n){
        srand(time(0));
        int throwsinsidecircle = 0;
        for (int i = 0; i < n; i++){
            double x = rand() % RAND_MAX;
            double y = rand() % RAND_MAX;
            double d = sqrt((x**2) + (y**2));
            if (d < 1){
                throwsinsidecircle++;
            }
        }
        return throwsinsidecircle / (double) n * 4;
    }
    ```

6. Array Operations

   > 1. Write a function  `printArray` to print the contents of an integer array with string `", "` between elements 

   ```cpp
   void printArray(const int * arr,const int n){
       for (int i = 0; i < n - 1; i++){
           std::cout << i << ", ";
       }
       std::cout << arr[n - 1];
   }
   ```

   > 2. Write a `reverse` function that takes an integer array and its length as arguments. Your function should reverse the contents of the array, leaving the reversed values in the original array and return nothing.

   ```c++
   void reverse(const int * arr, const int n){
       for(int i = 0; i < n / 2; i++){
           int lefttemp = arr[i];
           int rightindex = n - i - 1;
           // swapping
           lefttemp = arr[rightindex];
           arr[rightindex] = lefttemp;
       }
   }
   ```

   > 3. Assume the existence of two constants `WIDTH` and `LENGTH`. Write a function with the following signature:
   >
   >    ```void transpose(const int input[][LENGTH], int output[][WIDTH]);```
   >
   >    Your function should transpose the `WIDTH x LENGTH` matrix in input, placing the `LENGTH x WIDTH` transposed matrix into `output`
   
   ```cpp
   void transpose(const int input[][LENGTH], int output[][WIDTH]){
       for(int i = 0; i < WIDTH, i++){
           for(int j = 0, j < LENGTH; j++){
               output[j][i] = input[i][j]
           }
       }
   }
   ```
   
   > 4. What would happen if, instead of having `output` be an *out argument*, we simply declared a new array within `transponse` and returned that array?
   
   If we make array inside the function (local variable for the function `transpose`), the array will be removed from the *memory* after the function is executed from the stack. we can make an array in the heap and return that pointer.
   
   > 5. Rewrite your function from part 2 to use pointer-offset notation instead of array-subscript notation
   
   ```cpp
   void reverse(const int * arr, const int n){
       for (int i = 0; i < n / 2; i++){
           int lefttemp = *(arr + i);
           int rightindex = n - i - 1;
           // swapping
           *(arr + i)  = *(arr + rightindex);
          	*(arr + rightindex) = lefttemp;
       }
   }
   ```
   
7.   Pointers and Strings

    > 1. Write a function that returns the length of a string (`char *`), excluding the final `NULL` character. It should not use any standard library functions. You may use arithmetic and dereference operators, but no indexing operators (`[]`).

    ```cpp
    int length(const char * string){
        int len = 0;
        const char * strpointer = string;
        while ((*strpointer) != '\0'){
            strpointer += len;
            len++;
        }
        return len;
    }
    ```

    > 2. Write a function that swaps two integer values using call by reference.

    ```cpp
    void swap(int &a, int  &b){
        int temp = a;
        b = a;
        a = temp;
        return;
    }
    ```

    > 3. Rewrite your function from part 2 to use pointers instead of references.

    ```cpp
    void swap(int *a, int *b){
        int temp = *a;
        *b = *a;
        *a = temp;
        return;
    }
    ```

    > 4. Write a function similar to the once in part 3, but instead of swapping two values, it swaps two pointer to point to each other's values.

    ```cpp
    void swap(int ** a, int ** b){
        int * temp = *a;
        *b = *a;
        *a = temp;
    }
    ```

    > 5. Assume that the following variable declaration has been already been made:
    >
    >    ```cpp
    >    char *oddOrEven = "Never odd or even";
    >    ```
    >
    >    Write a single statement to accomplish each of the following tasks (assuming for each one that the previous ones have already been run). Make sure you understand what happens in each of them

    > Create a pointer to a `char` value named `nthCharPtr` pointing to the 6th character of `oddOrEven`. Use the indexing operator;

    ```cpp
    char * nthCharPtr = oddOrEven[6];
    ```

    > Using pointer arithmetic, update `nthCharPtr` to point to the 4th character in `oddOrEven`

    ``` cpp
    nthCharPtr -= 2;
    ```

    > Print the value of the currently pointed to by `nthCharPtr`

    ```cpp
    std::cout << *nthCharPtr << std::endl;
    ```

    > Create a new pointer to pointer named `pointerPtr` that points to the `nthCharPtr`

    ```cpp
    char ** pointerPtr = &nthCharPtr;
    ```

    > Print the value stored in `pointerPtr`

    ```cpp
    std::cout << pointerPtr;
    ```

    > Using `pointerPtr`, print the value pointed to by `nthCharPtr`

    ```cpp
    std::cout << **pointerPtr;
    ```

    > Update the `nthCharPtr` to point to the next character in `oddOrEven`

    ```cpp
    nthCharPtr++;
    ```

    > Using pointer arithmetic, print out how far away from the character currently pointer by the `nthCharPtr` is from th start of the string.

    ```cpp
    std::cout << nthCharPtr - oddOrEven;
    ```
