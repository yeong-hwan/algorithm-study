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

; (printBoard #2a((0 0 0 0 0 0 0 0 0) (0 0 0 0 0 0 0 0 0) (0 0 0 0 0 0 0 0 0)
; (0 0 0 0 0 0 0 0 0) (0 0 0 0 0 0 0 0 0) (0 0 0 0 0 0 0 0 0) (0 0 0 0 0 0 0
; 0 0) (0 0 0 0 0 0 0 0 0) (0 0 0 0 0 0 0 0 0))) 

