parent(john, mary).
parent(mary, ann).
parent(ann, tom).
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).