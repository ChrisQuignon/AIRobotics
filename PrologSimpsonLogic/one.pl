man(abraham).
man(herbert).
man(homer).
man(clancy).
man(bart).
women(mona).
women(lisa).
women(maggie).
women(jacqueline).
women(marge).
women(patty).
women(selma).
women(ling).

married(abraham, mona).
offspring(abraham, mona, homer).
offspring(abraham, mona, herbert).

married(homer, marge).
offspring(homer, marge, bart).
offspring(homer, marge, lisa).
offspring(homer, marge, maggie).

offspring(clancy, jacqueline, marge).
offspring(clancy, jacqueline, patty).
offspring(clancy, jacqueline, selma).

parent(selma, ling).


married(M, D) :- married(D, M), D\=M.

parent(P, C) :- offspring(P, _, C).
parent(P, C) :- offspring(_, P, C).

father(F, C) :- man(F), parent(F, C).
mother(M, C) :- women(M), parent(M, C).
sibling(A, B) :- brother(A, B); sister(A, B).
%sibling(A, B) :- parent(A, P), parent(B, P), A\=B, B\=P, A\=P.

daughter(C, P) :- women(C), parent(P, C).
son(C, P) :- man(C), parent(P, C).

grandChild(C, G) :- parent(P, C), parent(G, P), C\=G.

brother(B, C) :- son(B, P), parent(P, C), B\=C.
sister(S, C) :- daughter(S, P), parent(P, C), S\=C.

uncle(U, C) :- pasisrent(P, C), brother(U, P).
aunt(A, C) :- parent(P, C), sister(A, P).

cousin(C, D) :- parent(P, C), parent(Q, D), sibling(P, Q), not(sibling(C, D)), P\=Q.

grandDad(D, C) :- man(D), grandChild(C, D).
grandMom(M, C) :- women(M), grandChild(C, M).

descendent(D, A) :- parent(A, D). 
descendent(D, A) :- parent(P, D), descendent(P, A), A\=D. 

ancestor(A, D) :- parent(A, D). 
ancestor(A, D) :- parent(A, P), ancestor(P, D), A\=D. 


