(define (caar x) (car (car x))) ; first.first
(define (cadr x) (car (cdr x))) ; rest.first
(define (cadar x) (car (cdr (car x)))) ; first.rest.first
(define (cdar x) (cdr (car x))) ; first.rest
(define (cddr x) (cdr (cdr x))) ; rest.rest

;; Problem 14
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 14
  (define (helper s idx)
    (if (null? s)
      '()
      (cons (list idx (car s)) (helper (cdr s) (+ idx 1))) 
      )
    )
  (helper s 0)
  ; END PROBLEM 14
  )


;; Problem 15

;; Return the value for a key in a dictionary list
(define (get dict key)
  ; BEGIN PROBLEM 15
  (cond 
    ((null? dict) #f)
    ((equal? key (caar dict)) (cadar dict)) ; cadar dict return value, cdar returns (value)
    (else (get (cdr dict) key))
    )
  ; END PROBLEM 15
  )

;; Return a dictionary list with a (key value) pair
(define (set dict key val)
  ; BEGIN PROBLEM 15
  (cond 
    ((null? dict) (list (list key val)))
    ((equal? key (caar dict)) (cons (list key val) (cdr dict)))
    (else (cons (car dict) (set (cdr dict) key val)))
    )
  ; END PROBLEM 15
  )

;; Problem 16

;; implement solution-code
(define (solution-code problem solution)
  ; BEGIN PROBLEM 16
  (cond
    ((null? problem) '())
    ((equal? problem '_____) solution)
    ((list? problem) (cons (solution-code (car problem) solution) (solution-code (cdr problem) solution)))
    (else problem)
    )
  ; END PROBLEM 16
  )
