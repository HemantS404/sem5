male(hemant).
male(shubham).
male(sahil).
male(dad).

female(khushi).
female(prachi).
female(mom).

parent(dad, hemant).
parent(dad, shubham).
parent(dad, khushi).
parent(dad, prachi).
parent(mom, hemant).
parent(mom, shubham).
parent(mom, khushi).
parent(mom, prachi).

mother(X, Y):-parent(X, Y),female(X).
father(X, Y):-parent(X, Y),male(X).

hasChild(X):-parent(X,_).

brother(X, Y):-parent(Z, X),parent(Z, Y),male(X),X\==Y.
sister(X, Y):-parent(Z, X),parent(Z, Y),female(X),X\==Y.