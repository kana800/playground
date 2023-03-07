contains exercises from the book [cpp exercises](), This `page` will consist of answer for the `chapter2::Basics` 

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
