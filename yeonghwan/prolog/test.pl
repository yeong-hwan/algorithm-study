child(son1, lee).
child(son2, lee).
child(dau1, lee).
child(dau2, yoo).
male(lee).
male(son1).
male(son2).
female(yoo).
female(dau1).
female(dau2).
couple(lee,yoo).
couple(yoo,lee).
parent(Y,X) :- child(X,Y); child(X,Z), couple(Y,Z).
father(Y,X) :- child(X,Y), male(Y); child(X,Z), couple(Y,Z), male(Y).
mother(Y,X) :- child(X,Y), female(Y); child(X,Z), couple(Y,Z), female(Y).
son(X,Y) :- child(X,Y), male(X); child(X,Z), couple(Y,Z), male(X).
daughter(X,Y) :- child(X,Y), female(X); child(X,Z), couple(Y,Z), female(X).