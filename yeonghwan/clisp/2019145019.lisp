; 1. printBoard
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

(printBoard #2a((0 0 0 0 0 0 0 0 0) (0 0 0 0 0 0 0 0 0) (0 0 0 0 0 0 0 0 0)
(0 0 0 0 0 0 0 0 0) (0 0 0 0 0 0 0 0 0) (0 0 0 0 0 0 0 0 0) (0 0 0 0 0 0 0
0 0) (0 0 0 0 0 0 0 0 0) (0 0 0 0 0 0 0 0 0))) 

(printBoard #2a((5 3 0 0 7 0 0 0 0) (6 0 0 1 9 5 0 0 0) (0 9 8 0 0 0 0 6 0)
(8 0 0 0 6 0 0 0 3) (4 0 0 8 0 3 0 0 1) (7 0 0 0 2 0 0 0 6) (0 6 0 0 0 0 2 8 0)
(0 0 0 4 1 9 0 0 5) (0 0 0 0 8 0 0 7 9 )))


; 2. checkBoard
(defun rowCheck (board index)
  (let ((result (make-array 9)))
    (dotimes (i 9)
      (setf (elt result i) (aref board index i)))
    result))

(defun colCheck (board index)
  (let ((result (make-array 9)))
    (dotimes (i 9)
      (setf (elt result i) (aref board i index)))
    result))

(defun boxCheck (board n m)
  (let ((result (make-array 9)))
    (dotimes (i 3)
      (dotimes (j 3)
        (setf (elt result (+ (* i 3) j)) (aref board (+ n i) (+ m j)))))
    result))


(defun checkBoard (board x y)
    (let ((result t))
        (dotimes (k 9)
            (when (or (> (count (1+ k) (rowCheck board x)) 1)
                (> (count (1+ k) (colCheck board y)) 1)
                (> (count (1+ k) (boxCheck board
                    (* (floor (/ x 3)) 3)
                    (* (floor (/ y 3)) 3))) 1))
        (setf result nil)))
    result))


(checkBoard #2a((1 3 5 4 6 9 2 7 8) (7 8 2 1 3 5 6 4 9) (4 6 9 2 7 8 1 3 5)
(3 2 1 5 4 6 8 9 7) (8 7 4 9 1 3 5 2 6) (5 9 6 8 2 7 4 1 3) (9 1 7 6 5 2 3
8 4) (6 4 3 7 8 1 9 5 2) (2 5 8 3 9 4 7 6 1)) 7 8) 

; 3. solveBoard
(defun solveBoard (board)
  (let ((filled t) x y)
    (dotimes (i 9)
      (dotimes (j 9)
        (when (= (aref board i j) 0)
          (setf filled nil x i y j))))
    (if filled
        (printBoard board)
        (dotimes (k 9)
          (setf (aref board x y) (1+ k))
          (when (checkBoard board x y)
            (solveBoard board))
          ; (setf (aref board x y) 0)))))


(solveBoard #2a((0 3 5 4 6 9 2 7 8) (7 8 2 1 0 5 6 0 9) (0 6 0 2 7 8 1 3 5)
(3 2 1 0 4 6 8 9 7) (8 0 4 9 1 3 5 0 6) (5 9 6 8 2 0 4 1 3) (9 1 7 6 5 2 0
8 0) (6 0 3 7 0 1 9 5 2) (2 5 8 3 9 4 7 6 0)))

(solveBoard #2a((0 3 5 4 6 9 2 7 8) (7 8 2 1 0 5 6 0 9) (0 6 0 2 7 8 1 3 5)
(3 2 1 0 4 6 8 9 7) (8 0 4 9 1 3 5 0 6) (5 9 6 8 2 0 4 1 3) (9 1 7 6 5 2 0
8 0) (0 0 0 0 0 0 0 0 0) (0 0 0 0 0 0 0 0 0)))