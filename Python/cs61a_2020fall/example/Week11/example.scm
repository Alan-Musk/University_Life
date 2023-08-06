(define (count-stairways n)
  (cond 
    ((< n 2)
     0)
    ((= n 2)
     1)
    ((= n 3)
     1)
    (else
     (+ (count-stairways (- n 2))
        (count-stairways (- n 3))))))

(define (count-serpinski depth)
  (if (= depth 1)
      1
      (+ 2 (* 3 (count-serpinski (- depth 1))))))

(define (construct value lists)
  (if (null? lists)
      '()
      (cons (cons value (car lists))
            (construct value (cdr lists)))))

(define (repeat k fn)
  (if (> k 0)
      (begin (fn) (repeat (- k 1) fn))
      nil))

(repeat 5
        (lambda ()
        
          (fd 100)
          (repeat 5 (lambda () (fd 20) (rt 144)))
          (rt 144)))
