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

