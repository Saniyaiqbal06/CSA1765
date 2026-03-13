% Simple recursive sum
sum(0, 0).
sum(N, Sum) :-
    N > 0,
    N1 is N - 1,
    sum(N1, SubSum),
    Sum is SubSum + N.

% Tail‑recursive sum (more efficient for large N)
sum_tail(N, Sum) :- sum_acc(N, 0, Sum).

sum_acc(0, Acc, Acc).
sum_acc(N, Acc, Sum) :-
    N > 0,
    NewAcc is Acc + N,
    N1 is N - 1,
    sum_acc(N1, NewAcc, Sum).