% state(Monkey, Box, OnBox, HasBanana)
% positions: atdoor, atwindow, atcenter
start(state(atdoor, atwindow, no, no)).
goal(state(atcenter, atcenter, yes, yes)).

% walk: monkey moves from anywhere (ignored) to M2, provided M2 is not where the box is
move(state(_, B, O, H), walk(M2), state(M2, B, O, H)) :- M2 \= B.

% push: monkey and box at same position, push to M2
move(state(M, M, no, H), push(M2), state(M2, M2, no, H)) :- M2 \= M.

% climb: monkey at box, box on floor, climb onto box
move(state(M, M, no, H), climb, state(M, M, yes, H)).

% grasp: monkey on box, no banana yet, grasp banana
move(state(M, M, yes, no), grasp, state(M, M, yes, yes)).

% solve(State, Plan): find a plan from State to goal
solve(State, []) :- goal(State).
solve(State, [Action|Moves]) :-
    move(State, Action, NewState),
    solve(NewState, Moves).