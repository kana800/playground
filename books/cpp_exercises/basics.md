> contains exercises from the book [cpp exercises](https://www.ece.uvic.ca/~frodo/cppbook/downloads/exercises_for_programming_in_cpp-2021-04-01.pdf), This `page` will consist of answer for the `chapter2::Basics` 

---

### Objects, Types, and Values

> 1. For each of the declarations below, do the following. State whether the declaration is also definition

[The key idea here is understand what is a declaration and what is a definition](https://stackoverflow.com/questions/1410563/what-is-the-difference-between-a-definition-and-a-declaration)
> A declaration introduces an indentifier and describes its type. A declaration is what a compiler needs to
accept references to that indentifier; A definition instantiates/implement this indentifier. This is what the liner needs to link the references to those entities.

- `int i = 5`: declaration and a definition
- `int abs(int x)`: declaration but not a definition
- `float sqr(float x) {return x * x};`: definition
    - `float sqr(float x)` would be the declarations
- `extern const double pi;`: declaration but not a definition
- `char s[] = "Hello";`: declaration and a definition
- `double x;` : declaration
- `int (*func)(int, int);`: declaration
- `template <typename T> T max(T x, Ty)`: declaration
- `template <typename T> bool is_negative(T x){return x < 0}`: definition
- `auto meaning_of_life = 42;` : declaration and definition

> 2. For each of the declarations below, do the following. State whether the declaration is also an initialization. If it is not an initialization, modify it so that it is one.

> Initialization is the assignment of an initial value for a data object or variable

- `int x;` : declaration
    - `int x = 5;` would an initialization
- `void (*f)();` : declaration
- `const double pi = 3.14;`: initialization

> 3. State whether each line of code below corresponds to a type declaration or definition

- `struct Point {double x; double y;};` : definition
- `struct Thing;` : declaration
- `enum Fruit: int {apple, orange, banana};` : definition
- `enum Color: int;` : declaration

> 4. Write a declaration for each of the entities listed below. Initialize each one

- a pointer to a `char`
    - `char* cptr = "Hello";`
- a pointer to a constant `char`
    - `char const* cptr = "Hello Again";`
- a constant pointer to a `char`
    - `char * const cptr = 'a';`
- a constant pointer to a constant `char`
    - `char const * const = 'a';`
- a pointer to a function taking a double parameter and returning an `int`
    - `int (*funptr)(double){return 9;};`
- a pointer to pointer to an `int`
    - `int** dp = {0,1};`
- a lvalue reference to an array of 16 `int`s
    - `int& lref[16] = {1};`
- a pointer to an array of 10 elements of type `std::string`
    - `std::string arr[10];`
- a lvalue reference to an array of 8 `int`s
    - `int &ref[8];`

> 5. Explain what is potentially wrong with the line of code below

- `char c = -1;`

Usually the compiler will try to assign letter related to value `-1` using ascii but there is no value `-1` in the ascii table, Hence you will get an error.

> 6. For each of the conditions below: state whether the condition must be true, must be false, or could be either true or false.

- `sizeof(char) == 1`: true
- `sizeof(int) == 2 || sizeof(int) == 4`: latter part is true

> 7. Using `typedef`, create a type alias for each of the types listed below

- a pointer to a `char`
    - `typedef char* cptr;`
- a pointer to a `const char`
    - `typedef const char* cnstptr;`
- a `const` pointer to a `char`
    - `typedef char*const cpc;`
- a pointer to a function taking a `float` parameter and returning an `int`
    - `typedef int (*funcptr)(float) fptr;`
- a pointer to an array of 16 elements of an array of 8 elements of type `long`
    - `typedef long somearr[16];`
- an lvalue reference to an array of 8 `int`s
    - `typedef int& ref[8];`
