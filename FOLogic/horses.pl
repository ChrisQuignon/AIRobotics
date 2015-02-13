horse(X) :- mammal(X).
pig(X) :- mammal(X).
cow(X) :- mammal(X).

horse(bluebeard).

parent(bluebeard, Charlie).

parent(X, Y) :- offspring(Y, X).
mammal(X) :- parent(N, X).
