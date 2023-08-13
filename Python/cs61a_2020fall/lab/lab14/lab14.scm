
(define (split-at lst n)
    (define (helper lst n so_far)
        (cond ((null? lst) so_far)
              ((= 0 n) (cons so_far (cons lst nil)))
              (else (helper (cdr lst) (- n 1) (cons (car lst) so_far))))
    )
(helper lst n nil)
)

(define (compose-all funcs)
  (if (null? funcs) (lambda (x) x)
      (lambda (x) ((compose-all (cdr funcs)) ((car funcs) x) ))
))

(split-at '(1 2 3 4 5) 3)
