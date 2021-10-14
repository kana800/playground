; define a procedure that takes three numbers as arguments and returns the sum of the
; squares of the two larger numbers

; returns the maximum
(defun maximum (a b)
	(if (> a b)
	  a
	  b))

;returns the sum of squares
(defun square (a b)
	(+ (* a a) (* b b)))


(defun squaresoftwolargestnumber (a b c)
	(setq maxone (maximum a b))
	(if (= maxone a)
		(setq maxtwo (maximum b c))
		(setq maxtwo (maximum a c))
	  )
	(square maxone maxtwo)
  )

(write(squaresoftwolargestnumber 5 5 3))
