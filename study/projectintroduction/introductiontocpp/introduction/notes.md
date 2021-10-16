## What is a compiler?

> Computers understand only one language and that language consists of sets of instructions made of ones and zeros. This computer language is called as machine language.
>
> Because a computer can only understand machine language and humans wish  to write in high level languages high level languages have to be  re-written (translated) into machine language at some point. This is  done by special programs called compilers, interpreters, or assemblers  that are built into the various programming applications.
>
> [for more information about compilers](https://en.wikiversity.org/wiki/C%2B%2B/Introduction#Compiling_the_code)
>
> [References](https://cplusplus.com/doc/tutorial/introduction/)

### Compilation Process

Compilation is the process where we convert plain text into object file. compiler goes through several steps to create the object file. First step is called **preprocessing** followed up by **Tokenizing**, **parsing** which will create an **abstract syntax tree**.

Most common preprocessing statements:
- `#include <file>` are copied into the `c/c++` file mentioned.
- `#define INTEGER int` looks up the `INTEGER` in the `c/c++` file and replace it with `int`  
- `#if` - `#endif` let use include or exclude code based on a given condition

[References](https://www.youtube.com/watch?v=3tIqpEmWMLI&amp;list=PLlrATfBNZ98dudnM48yfGUldqGD0S4FFb&amp;index=6)

---

**Tokens** are minimal chunks of program that have meaning to the compiler.

There are different token types:

- Keywords : words with special meaning to the compiler (`int, double, for`)
- Identifiers : names of things that are not built into the language (`cout, std, x`)
- Literals : basic constant values whose value is specified directly in source code (`"Hello world!"`)
- Operators : mathematical or logical operators `(+,-, &&)`
- Punctuation/Separators : punctuation defining the structure of a program (`{ } ( ) , ;`)
- Whitespace : spaces of various sorts; ignored by the compilers

[more about parser tokens](https://youtu.be/eF9qWbuQLuw?t=169)

[References](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-096-introduction-to-c-january-iap-2011/lecture-notes/MIT6_096IAP11_lec01.pdf)

---

```cpp
// hello world program
#include <iostream>

int main() {
    std::cout << "Hello, World!\n"
}
```

>  What is a namespace?
>
> In `C++`, identifiers can be defined within a context - sort of a directory of names - called a namespace. When we want to access an identifier defined in a namespace, we tell compiler to look for it in that namespace using the *scope resolution oeprator* (`::`). Here, we are telling the compiler to look for `cout` in `std` namespace.
>
> [References](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-096-introduction-to-c-january-iap-2011/lecture-notes/MIT6_096IAP11_lec01.pdf)