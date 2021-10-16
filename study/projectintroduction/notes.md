#### Lecture `1A`: Overview and Introduction to Lisp

### The Elements of Programming

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

### [Square Root of `X`](https://youtu.be/-J_xL4IGhJA?t=3546)

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

#### Lecture `1B`: Procedures and Processes; Substitution Model

> Substitution (Model) Rule
>
> To evaluate an application. Evaluate the operator to get procedure. Evaluate the operands to get arguments. Apply the procedure to the arguments. Copy the body of the procedure, substituting the arguments supplied for the formal parameters of the procedure. Evaluate resulting new body.
>
> Example:
>
> Written below is a procedure to get the sum of square of two numbers.
>
> ```lisp
> defun square(x)
> 	(* x x))
> 
> defun sos(x y)
> 	(+ (square x) (square y)))
> ```
>
>  ```lisp
> (sos 3 4)
> (+ (square 3) (square 4))
> (+ (* 3 3) (* 4 4))
>  ```

#### Exercises

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

  





