:- use_module(library(clpfd)).                          %*

%unique(Row) :- sort(Row, Sorted), length(Row, Length), length(Sorted, Length).
%all_digits(Row) :- forall(between(1,9,X), memberchk(X, Row)).

all_different(L) => all_different(L,[]).

all_different([],Left) => true.
all_different([X|Right],Left) =>
outof(X,Left,Right),
all_different(Right,[X|Left]).

outof(X,Left,Right), var(X), {ins(X)} => true.
outof(X,Left,Right) => 
exclude_list(X,Left),exclude_list(X,Right).

sudoku(Rows) :-
    length(Rows, 9), maplist(same_length(Rows), Rows),  %1
    append(Rows, Vs), Vs ins 1..9,                      %2
    maplist(all_distinct, Rows),                        %3
    transpose(Rows, Columns),                           %4
    maplist(all_distinct, Columns),                     %5
    Rows = [A,B,C,D,E,F,G,H,I],
    blocks(A, B, C), blocks(D, E, F), blocks(G, H, I).  %6

blocks([], [], []).
blocks([A,B,C|Bs1], [D,E,F|Bs2], [G,H,I|Bs3]) :-        %7
    all_distinct([A,B,C,D,E,F,G,H,I]),
    blocks(Bs1, Bs2, Bs3).

checkLine(L) :- all_distinct(L).