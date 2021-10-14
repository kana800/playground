(defun square(x)
  "returns the square of the number"
  (* x x)
  )

(defun sumofsquares(x y)
  "returns the sum of the squares"
  (+ (square x) (square y))
  )

(write(sumofsquares 3 4))
