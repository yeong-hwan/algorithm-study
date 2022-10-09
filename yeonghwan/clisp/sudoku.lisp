(defun printBoard (board)
  (dotimes (row 9)
    (if (zerop (mod row 3))
          (format t "~%+---+---+---+---+---+---+~%|") 
        (format t "~%|"))
      (dotimes (col 9)
        (if (= 2 (mod col 3))
            (format t " ~a |" (aref board row col))
          (format t " ~a" (aref board row col)))))
  (format t "~%+---+---+---+---+---+---+~%~%")
)

; (printBoard #2a((5 3 0 0 7 0 0 0 0) (6 0 0 1 9 5 0 0 0) (0 9 8 0 0 0 0 6 0)
; (8 0 0 0 6 0 0 0 3) (4 0 0 8 0 3 0 0 1) (7 0 0 0 2 0 0 0 6) (0 6 0 0 0 0 2 8 0)
; (0 0 0 4 1 9 0 0 5) (0 0 0 0 8 0 0 7 9 )))



(defun checkBoard (board col row)
    (dotimes (num 9)
        (let ((r (* (truncate row 3) 3)) (c (* (truncate col 3) 3)))
                (dotimes (i 9 t)
                    (when (or (= (+ num 1) (aref board row i))
                            (= (+ num 1) (aref board i col))
                            (= (+ num 1) (aref board (+ r (mod i 3)) (+ c (truncate i 3))))
                            )
                        (return nil)
                    )
                )
        )
    )
)


(boardPrint #2a((1 3 5 4 6 9 2 7 8) (7 8 2 1 3 5 6 4 9) (4 6 9 2 7 8 1 3 5)
(3 2 1 5 4 6 8 9 7) (8 7 4 9 1 3 5 2 6) (5 9 6 8 2 7 4 1 3) (9 1 7 6 5 2 3
8 4) (6 4 3 7 8 1 9 5 2) (2 5 8 3 9 4 7 6 1)) 3 3)


(defparameter board #2a((1 6 0 1 0 4 0 5 0)
                        (0 0 8 3 0 5 6 0 0)
                        (2 0 0 0 0 0 0 0 1)
                        (8 0 0 4 0 7 0 0 6)
                        (0 0 6 0 0 0 3 0 0)
                        (7 0 0 9 0 1 0 0 4)
                        (5 0 0 0 0 0 0 0 2)
                        (0 0 7 2 0 6 9 0 0)
                        (0 4 0 5 0 8 0 7 1)))

(aref board 0 1) ; 6
(aref board 0 7) ; 5



(defun boardPrint (board col row)
    (aref board 0 1)
    (aref board 0 2))



(checkBoard #2a((1 3 5 4 6 9 2 7 8) (7 8 2 1 3 5 6 4 9) (4 6 9 2 7 8 1 3 5)
(3 2 1 5 4 6 8 9 7) (8 7 4 9 1 3 5 2 6) (5 9 6 8 2 7 4 1 3) (9 1 7 6 5 2 3
8 4) (6 4 3 7 8 1 9 5 2) (2 5 8 3 9 4 7 6 1)) 7 8)



(checkBoard #2a((5 3 0 0 7 0 0 0 0) (6 0 0 1 9 5 0 0 0) (0 9 8 0 0 0 0 6 0)
(8 0 0 0 6 0 0 0 3) (4 0 0 8 0 3 0 0 1) (7 0 0 0 2 0 0 0 6) (0 6 0 0 0 0 2 8 0)
(0 0 0 4 1 9 0 0 5) (0 0 0 0 8 0 0 7 9)) 3 3 )




; (solveBoard #2a((0 3 5 4 6 9 2 7 8) (7 8 2 1 0 5 6 0 9) (0 6 0 2 7 8 1 3 5)
; (3 2 1 0 4 6 8 9 7) (8 0 4 9 1 3 5 0 6) (5 9 6 8 2 0 4 1 3) (9 1 7 6 5 2 0
; 8 0) (6 0 3 7 0 1 9 5 2) (2 5 8 3 9 4 7 6 0)))