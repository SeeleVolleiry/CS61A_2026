(define (over-or-under num1 num2) 
    (cond ((< num1 num2) -1)
          ((= num1 num2) 0)
          (else 1)
        )
    )

(define (composed f g) ( lambda (x) (f (g x)) ))

(define (repeat f n) 
    (lambda (x) 
        (if (= n 0) 
            x
            ( f ( (repeat f (- n 1)) x ) ) 
        )    
    )
)

(define lst 
    (cons (list 1) (cons 2 ( cons (cons 3 (cons 4 nil)) (cons 5 nil) )))
)

(define (without-duplicates lst) 
    (if (null? lst)
        '()
        (cons (car lst)
              (without-duplicates 
                  ( filter ( lambda (x) (not (= x (car lst))) ) (cdr lst) )
              )
        )
    )
)
