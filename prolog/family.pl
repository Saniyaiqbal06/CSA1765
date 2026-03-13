parent(john, mary).
parent(john, tom).
parent(mary, ann).
parent(tom, ben).
male(john).
male(tom).
male(ben).
female(mary).
female(ann).
father(F, C) :- parent(F, C), male(F).
mother(M, C) :- parent(M, C), female(M).
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.