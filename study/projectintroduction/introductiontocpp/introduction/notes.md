### What is a compiler?

> Computers understand only one language and that language consists of sets of instructions made of ones and zeros. This computer language is called as machine language.
>
> Because a computer can only understand machine language and humans wish  to write in high level languages high level languages have to be  re-written (translated) into machine language at some point. This is  done by special programs called compilers, interpreters, or assemblers  that are built into the various programming applications.
>
> [compiler definition]: https://cplusplus.com/doc/tutorial/introduction/
>
> [for more information about compilers](https://en.wikiversity.org/wiki/C%2B%2B/Introduction#Compiling_the_code)

### Compilation Process

Compilation is the process where we convert plain text into object file. compiler goes through several steps to create the object file. First step is called **preprocessing** followed up by **Tokenizing**, **parsing** which will create an **abstract syntax tree**.

Most common preprocessing statements:
- `#include <file>` are copied into the `c/c++` file mentioned.
- `#define INTEGER int` looks up the `INTEGER` in the `c/c++` file and replace it with `int`  
- `#if` - `#endif` let use include or exclude code based on a given condition

[Compilation Process]: https://www.youtube.com/watch?v=3tIqpEmWMLI&amp;list=PLlrATfBNZ98dudnM48yfGUldqGD0S4FFb&amp;index=6	"Cherno How Compilers Work"

