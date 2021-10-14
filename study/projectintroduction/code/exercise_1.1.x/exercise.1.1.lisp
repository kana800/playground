;Below is a sequence of expressions.
;What is the result printed by the interpreter in response to each expression?
;Assume that the sequence is to be evaluated in the order in which it is presented.

10 ;interpreter prints 10
(+ 5 3 4) ;interpreter prints 12
(- 9 1) ;interpreter prints 8
(/ 6 2) ;interpreter prints 3
(+ (* 2 4) (- 4 6)) ;interpreter prints + 8 -2 -> 6
(define a 3) ;interpreter prints 'A', if we type (a) we will get 3 
(define b (+ a 1)) ;interpreter prints 'B', if we type (b) we will get 3 + 1 which is 4
(+ a b (* a b)) ;(3 * 4) -> 12, 3 + 4 + 12 -> 19
(= a b) ;interperter NIL
(if (and (> b a) (< b (* a b))) ; (>b a) -> True, (< b (* a b)) -> False. Interpreter will print a which is 3
    b ; prints if true
    a) ; prints if false
(cond ((= a 4) 6) ;false statement
      ((= b 4) (+ 6 7 a)); true statement will print (6 + 7 + 3) -> 16
      (else 25))
(+ 2 (if (> b a) b a)); interpreter prints 2 + b, 6
(* (cond ((> a b) a)
         ((< a b) b); true statement, interpreter printds (4 * (+ a 1)) -> 8
         (else -1))
   (+ a 1))
