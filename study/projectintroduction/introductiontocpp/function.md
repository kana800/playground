#### Why define your own functions?

> Readability : sqrt(5) is clearer than copy-pasting in an algorithm to compute the square root.
>
> Maintainability: To change the algorithm, just change the function
>
> Code reuse: let other people using algorithms you have implemented

#### Function Declaration Syntax

```cpp
int raiseToPower(int base, int exponent){
    int result = 1;
    for (int i = 0; i < exponent ; i++){
        result = result * base;
    }
    return result;
}
```

> - `raiseToPower` is the function name
> - `int raiseToPower(int base, int exponent)`: `int` is the return type and `int base, int exponent` are arguments and the argument data types are mentioned before the argument, example : `int base`, the base argument should be `int` type.
> - The content inside the function is called the `body`
> - we call this `function declaration`

```cpp
// this is function invocation
int main(){
    int threeExpFour = raiseToPower(3 ,4);
    std::cout << "3^4 is " << threeExpFour << std::end;
    return 0;
}
```

#### Function Overloading

```cpp
void printOnNewLine(int x){
    std::cout << "Integer: " << x << std::endl;
}

void printOnNewLine(char * x){
    std::cout << "String: " << x << std::endl;
}
```

> - Many functions with the same name, but different arguments and the function called when the invocation is the function that matches arguments.
> - `printOnNewLine(3)` prints `Integer: 3`
> - `printOnNewLine("hello")` prints `String: hello`

#### Function declaration

> Function declarations need to occur before invocations
>
> - reorder the function declarations
>
> - use a function prototype; informs the compiler you'll implement it later
>
>   ```cpp
>   int square(int);
>   
>   int cuber(int x){
>       return x * square(x);
>   }
>   
>   int square(int x){
>       return x * x;
>   }
>   ```
>
>   `int square(int)` is a function prototype.
>
>   Function prototypes are generally put into separate header files
>
>   ```cpp
>   // myLib.h - header
>   // contains prototypes
>   int square(int);
>   int cube(int);
>   ```
>
>   ```cpp
>   //myLib.cpp - implementation
>   #include "myLib.h"
>   
>   int cube(int x){
>       return x * square(x);
>   }
>   
>   int square(int x){
>       return x * x;
>   }
>   ```

#### Pass by value vs by reference

> passing by value: makes a copy of the variable changes to the variable within function don't occur outside the function.
>
> passing by reference: if you want to modify the original variables as opposed to making a copy, pass the variable by reference (`int &a` instead of `int a`)

#### Libraries

> Libraries are generally distributed as the header file containing the prototypes, and a binary `.dll`/`.so` file containing the implementation.

