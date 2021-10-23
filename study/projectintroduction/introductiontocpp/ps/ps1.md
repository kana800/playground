> 2.1 	Write  a program that outputs "Hello, World!" by printing a `const char *` with value "Hello, World!"

```c++
#include <iostream>

int main(int argc, char **argv){
    const char * hello = "Hello, World!";
    std::cout << hello;
    return 0;
}
```

> 2.2 Write a program that outputs "Hello, World!" *n* times with:
>
> - a `for` loop.
> - a `while` loop.
> - a `do ... while` loop.

```c++
#include <iostream>

/*print helloworld n times using a for loop*/
void printforHello(int n){
    const char * hello = "Hello, World!";
    for (int i = 0; i < n ; i++){
        std::cout << hello;
    }
    return;
}

/*print helloworld n times using a while loop*/
void printwhileHello(int n){
    const char * hello = "Hello, World!";
	int i = 0;
    while (n > i){
        std::cout << hello;
        // decrementing n
        n--;
    }   
    return;
}

/*print helloworld n times using a do while loop*/
void printdoHello(int n){
    
}
```

> 3.1
>
> - Below is a sample program. Use it to answer the following question: what happens if we declare the same name twice within a block, giving it two different meanings

we would get error called `conflicting declaration`.

> - Below is a sample program. Use it to answer the following question: What happens if we declare an identifier in a block, and then redeclare the same identifier in a block nested within that block.

it would output `A`

> - Below is a sample program. Use it to answer the following question: Suppose  an 
>   identifier has two different declarations,  one in an outer block and one in a nested 
>   inner block. If the name is accessed within the outer block, but after the inner block, 
>   which declaration is used? 

it would output `-1`

> - Below  is  a  sample  program  that  will  not  compile. Why  not? By  moving  which  line 
>   can  we  get  the  code  to  compile?

Because `#include iostream` is at the bottom of the file. we need to have it at the top of the file.

> 3.2
>
> **Basic Statistics**
>
> - Given a list of *N* integers, find its mean (as a `double`), maximum value, minimum value and range. Your program will first ask for *N*, then number of integers in the list, which the user will input. Then the user will input *N* more numbers.

[answer](problemset_one_question3.cpp)

> 3.3
>
> - Write a program to read number *N* from the user and then find the first *N* primes.
