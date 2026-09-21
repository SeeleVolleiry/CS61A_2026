(define (square n) (* n n))

(define (pow base exp) 
  (if (= exp 0)
    1
    (if (even? exp)
        (square (pow base (/ exp 2)))
        (* base (square (pow base (/ (- exp 1) 2))))))) 

(define (repeatedly-cube n x)
  (if (zero? n)
      x
      (begin (define y (* x x x)) (repeatedly-cube (- n 1) y))))

(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s))) ; return the second element of a list

(define (caddr s) (car (cdr (cdr s)))) ; return the third element of a list
