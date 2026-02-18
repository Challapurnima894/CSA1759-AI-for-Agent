parent(ram,ali).
parent(sita,ali).
male(ram).
female(sita).

father(X,Y):- parent(X,Y),male(X).
mother(X,Y):- parent(X,Y),female(X).
