% edge(From, To)
% heuristic(Node, Value)
edge(a,b). edge(a,c). edge(b,d). edge(c,d). edge(d,e).
h(a,4). h(b,3). h(c,2). h(d,1). h(e,0).

best_first(Start, Goal, [Start|Path]) :-
    best_first_help(Start, Goal, Path).

best_first_help(Goal, Goal, []).
best_first_help(Node, Goal, [Next|Path]) :-
    findall(N, edge(Node, N), Neighbors),
    best_neighbor(Neighbors, Next, Goal),
    best_first_help(Next, Goal, Path).

best_neighbor([N|Ns], Best, Goal) :-
    heuristic(N, H),
    best_neighbor(Ns, N, H, Best, Goal).

best_neighbor([], Best, _, Best, _).
best_neighbor([N|Ns], Cand, CH, Best, Goal) :-
    heuristic(N, H),
    ( H < CH -> best_neighbor(Ns, N, H, Best, Goal)
    ; best_neighbor(Ns, Cand, CH, Best, Goal) ).

heuristic(N, H) :- h(N, H).
heuristic(_, 0) :- !.   % any goal (or unknown node) gets heuristic 0