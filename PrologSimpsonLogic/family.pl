man(abraham).
man(herb).
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
women(zia).

married(abraham, mona).
offspring(abraham, mona, homer).
parent(abraham, herb).
%offspring(abraham, mona, herb).

married(homer, marge).
offspring(homer, marge, bart).
offspring(homer, marge, lisa).
offspring(homer, marge, maggie).

married(milhouse, lisa).
offspring(milhouse, lisa, zia).

offspring(clancy, jacqueline, marge).
offspring(clancy, jacqueline, patty).
offspring(clancy, jacqueline, selma).

parent(selma, ling).


married(M, D) :- married(D, M), D\=M.

parent(P, C) :- offspring(P, _, C).
parent(P, C) :- offspring(_, P, C).

child(A, B) :- parent(P, A), parent(P, B), A\=B.

cousin(C, D) :- parent(P, C), parent(Q, D), child(P, Q), not(child(C, D)), P\=Q.

greatGrandParent(P, C) :- parent(D, C), parent(G, D), parent(P, G).

grandChild(C, G) :- parent(P, C), parent(G, P), C\=G.

descendent(D, A) :- parent(A, D). 
descendent(D, A) :- parent(P, D), descendent(P, A), A\=D. 

ancestor(A, D) :- parent(A, D). 
ancestor(A, D) :- parent(A, P), ancestor(P, D), A\=D.

father(F, C) :- man(F), parent(F, C).
mother(M, C) :- women(M), parent(M, C).

daughter(C, P) :- women(C), parent(P, C).
son(C, P) :- man(C), parent(P, C).

brother(B, C) :- son(B, P), parent(P, C), B\=C.
sister(S, C) :- daughter(S, P), parent(P, C), S\=C.

uncle(U, C) :- parent(P, C), brother(U, P).
aunt(A, C) :- parent(P, C), sister(A, P).

grandDad(D, C) :- man(D), grandChild(C, D).
grandMom(M, C) :- women(M), grandChild(C, M).

