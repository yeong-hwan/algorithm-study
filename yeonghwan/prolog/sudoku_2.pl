% -------------------------------------------------------------------------
 
sudoku(Puzzle) :- 
   printSudoku(Puzzle), nl, 
   connect(Spots),
   flag(counter,_,0),
   init(Puzzle,Spots),
   solve(Spots),
   printSudoku(Puzzle),
   flag(counter,N,N+1),
   fail.
sudoku(_) :- 
   flag(counter,N,N), nl, 
   printCounter(N).
 
% ---------------------------------------------------------------
 
% connect(Spots) :- Spots = [spot(_,R1,C1,S1),spot(_,R1,C2,S1),.....].
 
connect(Spots) :- 
   length(Spots,81),
   connectRows(Spots), 
   connectCols(Spots), 
   connectSquares(Spots).
 
% connectRows(Spots) :- connect the spots of all rows in the list Spot
 
connectRows([]).
connectRows(Spots) :- 
   connectRow(Spots,_,9),
   skip(Spots,9,Spots1), 
   connectRows(Spots1).
 
% connectRow(Spots,R,K) :- the first K elements of Spot
% are in the same row R
 
connectRow(_,_,0).
connectRow([spot(_,R,_,_)|Spots],R,K) :- K > 0,
   K1 is K-1, connectRow(Spots,R,K1).
 
% connectCols(Spots) :- connect the spots of the same column
 
connectCols(Spots) :- connectCols(Spots,9).
 
% connectCols(Spots,K) :- connect K more columns columns
 
connectCols(_,0) :- !.
connectCols(Spots,K) :- K > 0,
   connectCol(Spots,_),
   skip(Spots,1,Spots1), 
   K1 is K-1, connectCols(Spots1,K1).
 
% connectCol(Spots,C) :- connect the first spot in Spots with
% the other spots in its column C
 
connectCol([],_).
connectCol([spot(_,_,C,_)|Spots],C) :-
   skip(Spots,8,Spots1),
   connectCol(Spots1,C).
 
% connectSquares(Spots) :- connect all three bands
% The nine squares are arranged in three horizontal bands,
% three squares in each band. 
 
connectSquares(Spots) :- 
   connectBand(Spots),
   skip(Spots,27,Spots1),
   connectBand(Spots1),
   skip(Spots1,27,Spots2),
   connectBand(Spots2).
 
% connectBand(Spots) :- connect the next band (of three squares
 
connectBand(Spots) :- 
   connectSq(Spots,_),
   skip(Spots,3,Spots1),
   connectSq(Spots1,_),
   skip(Spots1,3,Spots2),
   connectSq(Spots2,_).
 
% connectSq(Spots,S) :- connect the spots of square S. In the Spots
%    list each square is composed of three spot-triplets which 
%    are separated by 6 spots. 
 
connectSq([],_).
connectSq(Spots,S) :- 
  connectTriplet(Spots,S),
  skip(Spots,9,Spots1),
  connectTriplet(Spots1,S),
  skip(Spots1,9,Spots2),
  connectTriplet(Spots2,S).
 
% connectTriplet(Spots,S) :- connect the next three spots in the Spots
%    list with the square S
 
connectTriplet([spot(_,_,_,S),spot(_,_,_,S),spot(_,_,_,S)|_],S).
 
% skip(List,N,List1) :- skip the first N elements from a List
%    and return the rest of the list in List1. If the List is
%    too short, then succeed and return [] as rest.
 
skip([],_,[]) :- !.
skip(Xs,0,Xs) :- !.
skip([_|Xs],K,Zs) :- K > 0, K1 is K-1, skip(Xs,K1,Zs). 
 
% -----------------------------------------------------------
 
% init(Puzzle,Spots) :- initialize the Spots list on the
%    basis of the problem statement (Puzzle) and link the
%    Puzzle list to the Spots list 
 
init([],[]).
init([X|Xs],[Sp|Spots]) :- initSpot(X,Sp), init(Xs,Spots).
 
% If X is not instantiated in the given puzzle, create a link
% between the variable in the puzzle and the corresponding 
% variable in the spot. Otherwise copy the given number from 
% the puzzle into the spot and insert it into the spots 
% correct row, column, and square, if this is legal.
 
initSpot(X,spot(X,_,_,_)) :- var(X), !.
initSpot(X,spot(X,R,C,S)) :- integer(X),
   insert(X,R),
   insert(X,C),
   insert(X,S).
 
% ----------------------------------------------------------
 
% solve(Spots) :- solve the problem using backtrack
 
solve([]).
solve([Spot|Spots]) :- bind(Spot), solve(Spots).
 
% bind(Spot) :- bind the data field in Spot to an 
% available non-conflicting digit.
 
bind(spot(X,_,_,_)) :- nonvar(X), !.
bind(spot(X,R,C,S)) :- var(X),
   between(1,9,X),  % try a digit
   insert(X,R),
   insert(X,C),
   insert(X,S).
 
% ---------------------------------------------------------
 
% insert(X,L) :- X can be inserted into the list without 
% conflict, i.e. X is not yet in the list, when insert/2
% is called. Otherwise the predicate fails.
 
insert(X,L) :- var(L), !, L = [X|_].
insert(X,[Y|Ys]) :- X \= Y, insert(X,Ys).
 
% ---------------------------------------------------------
 
printSudoku([]).
printSudoku(Xs) :- nl,
   printBand(Xs,Xs1),
   write('--------+---------+--------'), nl,
   printBand(Xs1,Xs2),
   write('--------+---------+--------'), nl,
   printBand(Xs2,_).
 
printBand(Xs,Xs3) :- 
   printRow(Xs,Xs1), nl,
   write('        |         |'), nl, 
   printRow(Xs1,Xs2), nl,
   write('        |         |'), nl, 
   printRow(Xs2,Xs3), nl.
 
printRow(Xs,Xs3) :-
   printTriplet(Xs,Xs1), write(' | '),
   printTriplet(Xs1,Xs2), write(' | '),
   printTriplet(Xs2,Xs3).
 
printTriplet(Xs,Xs3) :-
   printElement(Xs,Xs1), write('  '),
   printElement(Xs1,Xs2), write('  '),
   printElement(Xs2,Xs3).
 
printElement([X|Xs],Xs) :- var(X), !, write('.').
printElement([X|Xs],Xs) :- write(X).
 
printCounter(0) :- !, write('No solution'), nl.
printCounter(1) :- !, write('1 solution'), nl.
printCounter(K) :- write(K), write(' solutions'), nl.
 
% ---------------------------------------------------------
 
test(N) :- puzzle(N,P), sudoku(P).
 
puzzle(1,P) :- 
   P = [_,_,4,8,_,_,_,1,7, 6,7,_,9,_,_,_,_,_, 5,_,8,_,3,_,_,_,4,
        3,_,_,7,4,_,1,_,_, _,6,9,_,_,_,7,8,_, _,_,1,_,6,9,_,_,5,
	1,_,_,_,8,_,3,_,6, _,_,_,_,_,6,_,9,1, 2,4,_,_,_,1,5,_,_].
 
puzzle(2,P) :- 
   P = [3,_,_,_,7,1,_,_,_, _,5,_,_,_,_,1,8,_, _,4,_,8,_,_,_,_,_,
	_,_,6,2,_,_,3,_,_, _,_,1,_,5,_,8,_,_, _,_,3,_,_,8,2,_,_,
        _,_,_,_,_,3,_,4,_, _,6,4,_,_,_,_,7,_, _,_,_,9,6,_,_,_,1].
 
puzzle(3,P) :-
   P = [1,7,_,_,_,9,_,_,4, _,_,_,_,_,_,7,_,_, 5,_,_,3,_,_,2,_,_,
        _,8,_,_,_,_,5,3,6, _,_,_,_,8,_,_,_,_, 6,9,1,_,_,_,_,8,_,
        _,_,7,_,_,4,_,_,2, _,_,2,_,_,_,_,_,_, 3,_,_,5,_,_,_,7,1].
 
puzzle(4,P) :-
   P = [1,_,_,_,_,9,_,_,4, _,_,_,_,_,_,7,_,_, 5,_,_,3,_,_,2,_,_,
        _,8,_,_,_,_,5,_,6, _,_,_,_,8,_,_,_,_, 6,9,1,_,_,_,_,8,_,
        _,_,7,_,_,4,_,_,2, _,_,2,_,_,_,_,_,_, 3,_,_,5,_,_,_,7,1].
 
puzzle(5,P) :- 
   P = [_,6,5,_,_,_,7,2,_, 3,_,7,_,_,_,1,_,8, 2,9,_,_,1,_,_,3,4,
        _,_,_,5,_,7,_,_,_, _,_,1,_,_,_,8,_,_, _,_,_,2,_,1,_,_,_,
        8,1,_,_,2,_,_,5,7, 7,_,2,_,_,_,9,_,1, _,5,4,_,_,_,6,8,_].
 
puzzle(6,P) :- 
   P = [5,_,2,_,_,3,_,_,_, 4,6,_,_,7,_,9,_,_, _,_,3,4,_,_,_,_,_,
        9,5,_,_,6,_,_,_,_, _,4,_,_,_,_,_,9,_, _,_,_,_,9,_,_,1,7,
        _,_,_,_,_,7,2,_,_, _,_,9,_,4,_,_,3,5, _,_,_,3,_,_,7,_,6].
