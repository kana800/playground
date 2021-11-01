### Lecture `1A`: Overview and Introduction to Lisp

#### The Elements of Programming

> Every powerful language has three mechanisms for combining simple ideas to form complex ideas.
>
> - primitive expressions, which represents the simplest entities the language is concerned with,
> - means of combination, by which compound elements are built from simpler ones,
> - means of abstraction,  by which compound elements can be named and manipulated as units.
>
> In programming we deal with two kinds of elements:
>
> - data: stuff we want to manipulate
> - procedures: rules for manipulating the data
>
> Therefore, any powerful programming language should be able to describe primitive data and primitive procedures and should have methods for combining and abstracting procedures and data.
>
> [primitive data in lisp](https://youtu.be/-J_xL4IGhJA?t=1830), for example we can take `3`, `17.4`, `5`. If we **combine** these **primitive data** with **operator**. `(+ 3 17.4 5)` we will get `25.4`. In this examples the **operands** will be `3 17.4` and `5`.
>
> ### Naming and the Environment
>
> In `Lisp`, we name things with `define` (variable).
>
> ```lisp
> (define size 2)
> size
> 2
> (* size)
> 10
> ```
>
> `define` is our language's simplest means of abstraction, for it allows us to use simple names to refer to the results of the compound operations.
>
> The possibility of associating values with symbols and later retrieving them means that the interpreter must maintain some sort of memory that keeps track of the name-object pairs. This memory is called the *environment* (*global environment*)
>
>  ### Compound  Procedures
>
> *Procedure definitions*, much more powerful abstraction technique which a compound operation can be given a name and then referred to as a unit.
>
> ```lisp
> (define (square x) (* x x))
> ```
>
> The general form of a procedure definition is 
>
> ```lisp
> (define (<name> <formal parameters>) <body>
> ```
>
> ### Conditional Expressions and Predicates
>
> This construct is called a *case analysis*, and there is a special form in Lisp for notating such a case analysis. Its called `cond`.
>
> ```lisp
> (defun abs(x)
>   (cond ((> x 0) x)
>         ((= x 0) 0)
>         ((< x 0) (- x))))
> ```
>
> The general form,
>
> ```lisp
> (cond (<p1> <e1>)
>       (<p2> <e2>)
> 
>       (<pn> <en>))
> ```
>
> Another way,
>
> ```commonlisp
> (define (abs x)
>   (if (< x 0)
>       (- x)
>       x))
> ```
>
> ```commonlisp
> (if <predicate> <consequent> <alternative>)
> ```

#### [Square Root of `X`](https://youtu.be/-J_xL4IGhJA?t=3546)

```lisp
(DEFINE (TRY GUESS X)
	(IF (GOOD-ENOUGH? GUESS X)
		GUESS
		(TRY (IMPROVE GUESS X) X))
)

(DEFINE (SQRT X)(TRY 1 X))
```

The above procedure is called a *recursive* definition. 

> [summary](https://youtu.be/-J_xL4IGhJA?t=4166)

#### Exercises

- [solutions for exercise 1.1, 1.2, 1.3](codes/exercise_1_1to1_4.lisp)

- > Observe that our model of evaluation allows for combinations whose operators are compound expressions.  Use this observation to describe the behavior of the following procedure:
  >
  > ```lisp
  > (define (a-plus-abs-b a b)  ((if (> b 0) + -) a b))
  > ```

  There is procedure called `a-plus-abs-b` which takes two parameters `a` and `b`, if `b` is greater than zero add it all numbers together (`b + a + b`) if not its going to be `b - a - b`.
  
- > Ben Bitdiddle has invented a test to determine whether the interpreter he is faced with is using applicative-order evaluation or normal-order evaluation.  He defines the following two procedures:
  >
  > ```lisp
  > (define (p) (p))
  > (define (test x y)
  >   (if (= x 0)
  >       0
  >       y))
  > ```
  >
  > Then he evaluates the expression
  >
  > `(test 0 (p))`
  >
  > What behavior will Ben observe with an interpreter that uses  applicative-order evaluation? What behavior will he observe with an  interpreter that uses normal-order evaluation? Explain your answer.

  An interpreter that uses **applicative-order evaluation** will first evaluate the arguments and then apply. when the expression `(test 0 (p))` is evaluated.  `test` will evaluate the procedure since `x` is `0`  our output will be `0`, if it isnt `(p)` will be calling `(p)` this will cause an infinite loop.

  In **normal-order evaluation** the interpreter will fully expand and then reduce, this will be written as :

  ```lisp
  (if (= 0 0))
  	0
  	(p)
  ```

  Here we replace the arguments of `test` function with the given parameters, since `x = 0` our output will be `0`, if its not `0` our output will be an infinite loop.

### Lecture `1B`: Procedures and Processes; Substitution Model

#### Substitution (Model) Rule

> To evaluate an application. Evaluate the operator to get procedure. Evaluate the operands to get arguments. Apply the procedure to the arguments. Copy the body of the procedure, substituting the arguments supplied for the formal parameters of the procedure. Evaluate resulting new body.
>
> Example:
>
> Written below is a procedure to get the sum of square of two numbers.
>
> ```lisp
>defun square(x)
> 	(* x x))
> 
> defun sos(x y)
> 	(+ (square x) (square y)))
> ```
> 
> ```lisp
>(sos 3 4)
>  (+ (square 3) (square 4))
> (+ (* 3 3) (* 4 4))
> ```

##### Exercises

- > Alyssa P. Hacker doesn't see why `if` needs to be provided as a special form.  "Why can't I just define it as an ordinary procedure in terms of `cond`?'' she asks. Alyssa's friend Eva Lu Ator claims this can indeed be done, and she defines a new version of `if`:
  >
  > ```lisp
  > (define (new-if predicate then-clause else-clause)
  >   (cond (predicate then-clause)
  >         (else else-clause)))
  > ```
  >
  > Eva demonstrates the program for Alyssa:
  >
  > ```
  > (new-if (= 2 3) 0 5)
  > 5
  > (new-if (= 1 1) 0 5)
  > 0
  > ```
  >
  > Delighted, Alyssa uses `new-if` to rewrite the square-root program:
  >
  > ```lisp
  > (define (sqrt-iter guess x)  
  > 	(new-if (good-enough? guess x)
  > 	guess
  > 	(sqrt-iter (improve guess x)
  >     			x))) 
  > ```
  >
  > What happens when Alyssa attempts to use this to compute square roots? Explain.

  In the above procedure,

  - `predicate` : `(good-enough? guess x)`
  - `then-clause`: `guess`
  - `else-clause`: `(square-iter (improve guess x) x)`

  If we replace the above parameters with `new-if`

  ```lisp
  (define (new-if predicate then-clause else-clause)
    (cond ((good-enough? guess x) guess)
          (else (sqrt-iter (improve guess x)
      			x))))
  ```

  this is a recursive function and the `new-if` will cause an infinite loop. since `new-if` is a procedure, it will not check if `(good-enough? guess x)` is true. what it will do is evaluate the arguments of the function, even when the `guess` is `good-enough`. 

#### [Linear Recursion and Iteration](https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-11.html#%_sec_1.2)

> Examining common *shapes* for processes generated by simple procedures. 

##### computing factorial using recursion

```lisp
(factorial 4)
(* 4 (factorial 3))
(* 4 ( * 3 (factorial 2)))
(* 4 ( * 3 (* 2 (factorial 1))))
(* 4 ( * 3 (* 2 1)))
(* 4 ( * 3 2))
(* 4 ( 6 ))
(* 4 6)
24
```

using the substitution method mentioned above, we have computed the factorial of `4`. If we look at the shape of the substitution, we can see that there is shape of expansion followed by contraction.

> The expansion occurs as the process builds up a chain of *deferred operations*. The contraction occurs as the operations are actually performed. This type of process, characterized by a chain of deferred operations is called **recursive process**. In above computation of `n!`, the length of the *deferred operations* grows linearly with *n*. Such a process is called **linear recursive process**. 

```lisp
(define factorial(n)
    (if (= n 1))
    	1
    	(* n (factorial (- n 1))))
```

##### [computing factorial using iteration](https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-4.html#%_toc_%_sec_1.2.1)

```lisp
(factorial 4)
(fact-iter 1 1 4)
(fact-iter 1 2 4)
(fact-iter 2 3 4)
(fact-iter 6 4 4)
(fact-iter 24 5 4)
24
```

using the substitution method mentioned above, we have computed the factorial of `4`. If we look at the shape of the substitution model, we  can see that it doesnt grow or shrink. We call this an **iterative process**.

> ```lisp
> (define (factorial n)
>   (fact-iter 1 1 n))
> 
> (define (fact-iter product counter max-count)
>   (if (> counter max-count)
>       product
>       (fact-iter (* counter product)
>                  (+ counter 1)
>                  max-count)))
> ```

##### Exercises

> - Each of the following two procedures defines a method for adding two positive integers in terms of the procedures `inc`, which increments its argument by 1, and `dec`, which decrements its argument by 1.
>
>   ```lisp
>   (define (+ a b)
>     (if (= a 0)
>         b
>         (inc (+ (dec a) b))))
>   
>   (define (+ a b)
>     (if (= a 0)
>         b
>         (+ (dec a) (inc b))))
>   ```
>
>   Using the substitution model, illustrate the process generated by each procedure in evaluation `(+ 4 5)`. Are these processes iterative or recursive ?

Illustration of the first function

```lisp
(+ 4 5); a is not zero
(inc (+ (dec 4) 5))
(inc (+ 3  5))
(inc (8))
9
```

Illustration of the second function

```lisp
(+ 4 5); a is not zero
(+ (dec 4) (inc 5)))
(+ 3 (inc 5))
(+ 3 6)
9
```

Processes are *iterative*.

> - The following procedure computes a mathematical function called Ackermann's function.
>
>   ```lisp
>   (define (A x y)
>     (cond ((= y 0) 0)
>           ((= x 0) (* 2 y))
>           ((= y 1) 2)
>           (else (A (- x 1)
>                    (A x (- y 1))))))
>   ```
>
>   What are the values of the following expressions?
>
>   - `(A 1 10)`
>   - `(A 2 4)`
>   - `(A 3 3)`
>
>   Consider the following procedures, where `A` is the procedure defined above:
>
>   - `(define (f n) (A 0 n))`
>   - `(define (g n) (A 1 n))`
>   - `(define (h n) (A 2 n))`
>   - `(define (k n) (* 5 n n))`
>
>   Give concise mathematical definitions for the functions computed by the procedures `f`, `g`, and `h` for positive integer values of *n*. For example, `(k n)` computes `5n^2`.

Expressions for:

- > `(A 1 0)`

  ```lisp
  (A 1 0) ; y is equal to zero
  0
  ```

- > `(A 2 4)`

  ```lisp
  (A 2 4)
  (A (- 2 1) (A 2 (- 4 1)))
  (A (- 2 1) (A 2 3))
  (A (- 2 1) ((A (- 2 1) (A 2 (- 3 1)))))
  (A (- 2 1) ((A (- 2 1) (A 2 2))))
  (A (- 2 1) ((A (- 2 1) (A (- 2 1) (A 2 (- 1 1))))))
  (A (- 2 1) ((A (- 2 1) (A (- 2 1) (A 2 0)))))
  (A (- 2 1) ((A (- 2 1) (A (- 2 1) 0)))) ; y is 0
  (A (- 2 1) ((A (- 2 1) (A 1 0))))
  (A (- 2 1) ((A (- 2 1) 0))) ; y is 0
  (A (- 2 1) ((A 1 0)))
  (A (- 2 1) 0); y is 0
  (A 1 0) ; y is 0
  0
  ```

- > `(define (f n) (A 0 n))`

  ```lisp
  (A 0 n); x is 0
  (* 2 n)
  ; f(n) would compute
  2n
  ```

- > `(define (g n) (A 1 n))`

  ```lisp
  (A 1 n); x is 1
  (A (- 1 1) (A 1 (- n 1)))
  (A (- 1 1) (A (- 1 1) (A 1 (- n-1 1))))
  (A (- 1 1) (A (- 1 1) (A 1 (n-2))))
  ```

  This would keep expanding till `n-N`.

#### [Tree Recursion](https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-4.html#%_toc_%_sec_1.2.2)

##### Exercises

> - A function *f* is defined by the rule that `f(n) = n` if `n < 3` and `f(n) = f(n-1) + 2f(n-2) + 3f(n-3)` if `n >= 3`. Write a procedure that computes *f* by means of a recursive process. Write a procedure that computes *f* by means of an iterative process

```cpp
#include <iostream>

// recursive process
int f(int n){
    if (n < 3){
        return n;
    } else {
        return f(n - 1) + 2 * f(n - 2) + 3 * f(n - 3)
    }
}
```

> - The following pattern of numbers is called *Pascal's triangle*
>
>   ```
>   		1
>   	1		1
>   1		2		1
>   ```
>
>   The numbers at the edge of the triangle are all `1`, and each number inside the triangle is the sum of two numbers above it. Write a procedure that computes elements of Pascal's triangle by means of a recursive process.

[code in action](ps/pascals_triangle.cpp)

> - Prove that `Fib(n)` is the closest integer to ![img](https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-G-D-11.gif)*n*/![img](https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-G-D-13.gif)5, where  ![img](https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-G-D-11.gif) =  (1 + ![img](https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-G-D-13.gif)5)/2.  Hint: Let ![img](https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-G-D-12.gif) =  (1 - ![img](https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-G-D-13.gif)5)/2.  Use induction and the definition of the Fibonacci numbers (see section [1.2.2](https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-11.html#%_sec_1.2.2)) to prove that  *Fib*(*n*) = (![img](https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-G-D-11.gif)*n* - ![img](https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-G-D-12.gif)*n*)/![img](https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-G-D-13.gif)5.

We can say that ![](https://latex.codecogs.com/png.latex?%5Cinline%20%5Ctextup%7Bfib%28n%29%7D%20%3D%20%5Ctextup%7Bfib%28n%20-%201%29%7D%20&plus;%20%5Ctextup%7Bfib%28n%20-%202%29%7D),

<p align="center">
	<img src="https://latex.codecogs.com/png.latex?%5Ctextup%7Bfib%28n%29%7D%20%3D%20%5Ctextup%7Bfib%28n%20-%201%29%7D%20&plus;%20%5Ctextup%7Bfib%28n%20-%202%29%7D%20%3D%20%5Cfrac%7B%5Cphi%5E%7Bn%20-%201%7D%20-%20%5Cpsi%5E%7Bn%20-%201%7D%20%7D%7B%5Csqrt%205%7D%20&plus;%20%5Cfrac%7B%5Cphi%5E%7Bn%20-%202%7D%20-%20%5Cpsi%5E%7Bn-2%7D%20%7D%7B%5Csqrt%205%7D"></img>
</p>

<p align="center">
<img src="https://latex.codecogs.com/png.latex?%5Ctextup%7Bfib%28n%29%7D%20%3D%20%5Ctextup%7Bfib%28n%20-%201%29%7D%20&plus;%20%5Ctextup%7Bfib%28n%20-%202%29%7D%20%3D%20%5Cfrac%7B%5Cphi%5E%7Bn%20-%201%7D%20-%20%5Cpsi%5E%7Bn%20-%201%7D%20%7D%7B%5Csqrt%205%7D%20&plus;%20%5Cfrac%7B%5Cphi%5E%7Bn%20-%202%7D%20-%20%5Cpsi%5E%7Bn-2%7D%20%7D%7B%5Csqrt%205%7D"></img>
</p>

<p align="center">
<img src="https://latex.codecogs.com/png.latex?%5Cfrac%7B%5Cphi%5E%7Bn%7D%20-%20%5Cpsi%5E%7Bn%7D%20%7D%7B%5Csqrt%205%7D%20%3D%20%5Cfrac%7B%5Cphi%5E%7Bn%20-%201%7D%20-%20%5Cpsi%5E%7Bn%20-%201%7D%20%7D%7B%5Csqrt%205%7D%20&plus;%20%5Cfrac%7B%5Cphi%5E%7Bn%20-%202%7D%20-%20%5Cpsi%5E%7Bn-2%7D%20%7D%7B%5Csqrt%205%7D"></img>
</p>

<p align="center">
<img src="https://latex.codecogs.com/png.latex?%5Cphi%5E%7Bn%7D%20-%20%5Cpsi%5E%7Bn%7D%20%3D%20%5Cphi%5E%7Bn%20-%201%7D%20-%20%5Cpsi%5E%7Bn%20-%201%7D%20&plus;%20%5Cphi%5E%7Bn%20-%202%7D%20-%20%5Cpsi%5E%7Bn-2%7D"></img>
</p>

<p align="center">
<img src="https://latex.codecogs.com/png.latex?%5Cphi%5E%7Bn%7D%20-%20%5Cpsi%5E%7Bn%7D%20%3D%20%28%5Cfrac%7B%5Cphi%5E%7Bn%7D%7D%7B%5Cphi%7D%20-%20%5Cfrac%7B%5Cpsi%5E%7Bn%7D%7D%7B%5Cpsi%7D%29%20&plus;%20%28%5Cfrac%7B%5Cphi%5E%7Bn%20%7D%7D%7B%5Cphi%5E2%7D%20-%20%5Cfrac%7B%5Cpsi%5E%7Bn%7D%7D%7B%5Cpsi%5E2%7D%29"></img>
</p>

<p align="center">
<img src="https://latex.codecogs.com/png.latex?%5Cphi%5E%7Bn%7D%20-%20%5Cpsi%5E%7Bn%7D%20%3D%20%5Cphi%28%5Cfrac%7B1%7D%7B%5Cphi%7D%20&plus;%20%5Cfrac%7B1%7D%7B%5Cphi%5E2%7D%29%20-%20%5Cpsi%5E2%20%28%5Cfrac%7B1%7D%7B%5Cpsi%7D%20&plus;%20%5Cfrac%7B1%7D%7B%5Cpsi%5E2%7D%29"></img>
</p>

It is given that ![](https://latex.codecogs.com/png.latex?%5Cinline%20%5Cphi%20%3D%20%5Cfrac%7B1%20&plus;%20%5Csqrt5%7D%7B2%7D%3B%20%5Cpsi%3D%5Cfrac%7B1%20-%20%5Csqrt5%7D%7B2%7D),

<p align="center">
<img src="https://latex.codecogs.com/png.latex?%5Cphi%5E%7Bn%7D%20-%20%5Cpsi%5E%7Bn%7D%20%3D%20%5Cphi%28%5Cfrac%7B1%7D%7B%5Cfrac%7B1%20&plus;%20%5Csqrt5%7D%7B2%7D%7D%20&plus;%20%5Cfrac%7B1%7D%7B%28%5Cfrac%7B1%20&plus;%20%5Csqrt5%7D%7B2%7D%29%5E2%7D%29%20-%20%5Cpsi%5E2%20%28%5Cfrac%7B1%7D%7B%5Cfrac%7B1%20-%20%5Csqrt5%7D%7B2%7D%7D%20&plus;%20%5Cfrac%7B1%7D%7B%28%5Cfrac%7B1%20-%20%5Csqrt5%7D%7B2%7D%29%5E2%7D%29"></img>
</p>

After some [simplification](https://www.wolframalpha.com/input/?i=1%2F%281%2Bsqrt%285%29%29%2F2),

<p align="center">
<img src="https://latex.codecogs.com/png.latex?%5Cphi%5E%7Bn%7D%20-%20%5Cpsi%5E%7Bn%7D%20%3D%20%5Cphi%5En%20-%20%5Cpsi%5En"></img>
</p>

We can say that ![](https://latex.codecogs.com/png.latex?%5Cinline%20%5Ctextup%7Bfib%28n%29%7D%20%3D%20%5Cfrac%7B%5Cphi%5E%7Bn%7D%20-%20%5Cpsi%5E%7Bn%7D%20%7D%7B%5Csqrt%205%7D) is true and [`-1 < \psi < 0` then `-1 < \psi^2 < 1`](https://math.stackexchange.com/questions/2717549/prove-that-operatornamefibn-is-the-closest-integer-to-frac-phin-s),

we can write `fib(n)` as two fractions,

<p align="center">
<img src="https://latex.codecogs.com/png.latex?%5Ctextup%7Bfib%28n%29%7D%20%3D%20%5Cfrac%7B%5Cphi%5E%7Bn%7D%7D%7B%5Csqrt5%7D%20-%20%5Cfrac%7B%5Cpsi%5En%7D%7B%5Csqrt%205%7D"></img>
</p>

<p align="center">
<img src="https://latex.codecogs.com/png.latex?%5Ctextup%7Bfib%28n%29%7D%20&plus;%20%5Cfrac%7B%5Cpsi%5E2%7D%7B%5Csqrt5%7D%20%3D%20%5Cfrac%7B%5Cpsi%7D%7B%5Csqrt5%7D"></img>
</p>

if we take the `\phi = (1 - \sqrt 5)/2` and since `\sqrt 5 > 2`,

<p align="center">
<img src="https://latex.codecogs.com/png.latex?-%5Cfrac%7B1%7D%7B2%7D%20%3C%20%5Cfrac%7B%5Cpsi%5E%7Bn%7D%7D%7B%5Csqrt5%7D%20%3C%20%5Cfrac%7B1%7D%7B2%7D"></img>
</p>

we can add `fib(n)`,
<p align="center">
<img src="https://latex.codecogs.com/png.latex?%5Ctextup%7Bfib%28n%29%7D%20-%20%5Cfrac%7B1%7D%7B2%7D%3C%20%5Ctextup%7Bfib%28n%29%7D%20&plus;%20%5Cfrac%7B%5Cpsi%5E2%7D%7B%5Csqrt5%7D%20%3C%20%5Ctextup%7Bfib%28n%29%7D%20&plus;%20%5Cfrac%7B1%7D%7B2%7D"></img>
</p>

we can say that,

<p align="center">
<img src="https://latex.codecogs.com/png.latex?%5Ctextup%7Bfib%28n%29%7D%20-%20%5Cfrac%7B1%7D%7B2%7D%3C%20%5Cfrac%7B%5Cphi%5E2%7D%7B%5Csqrt5%7D%20%3C%20%5Ctextup%7Bfib%28n%29%7D%20&plus;%20%5Cfrac%7B1%7D%7B2%7D"></img>
</p>

Above statement shows that ![](https://latex.codecogs.com/png.latex?%5Cinline%20%5Cfrac%7B%5Cphi%5E2%7D%7B%5Csqrt5%7D) will be closest integer to `fib(n)`.

#### Orders of Growth

##### Exercises

> - Draw the tree illustrating the process generated by the `count-change` procedure of section `1.2.2` in makings change for `11` cents. What are the orders of growth of the space and number of steps used by this process as the amount to be changed increases?



> - The sine of an angle (specified in radians) can be computed by making use of the approximation `sin x = x` if `x` is sufficiently small, and the trigonometric identity
><p align="center">
>   <img src="https://latex.codecogs.com/png.latex?%5Csin%20x%20%3D%203%20%5Csin%20%5Cfrac%7Bx%7D%7B3%7D%20-%204%20%5Csin%5E3%20%5Cfrac%7Bx%7D%7B3%7D"></img>
></p>
>   to reduce the size of the argument of `sin`. (For purposes of this exercise an angle is considered "sufficiently small" if its magnitude is not greater than 0.1 radians). These ideas are incorporated in the following procedures:
>
>   ```lisp
>   (define (cube x) (* x x x))
>   (define (p x) (- (* 3 x) (* 4 (cube x))))
>   (define (sine angle)
>      (if (not (> (abs angle) 0.1))
>          angle
>          (p (sine (/ angle 3.0)))))
>   ```
>
>   - How many times is the procedure `p` applied when `(sine 12.15)` is evaluated?
>   - What is the order of growth in space and number of steps (as a function of *a*) used by the process generated by the `sine` procedure when `(sine a)` is evaluated?
