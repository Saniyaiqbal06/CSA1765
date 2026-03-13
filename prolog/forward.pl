:- dynamic fact/1.

% Initial facts
fact(animal(dog)).
fact(animal(cat)).
fact(mammal(dog)).

% Rule: if animal(X) and mammal(X) then pet(X) (if not already a fact)
pet_rule(X) :-
    fact(animal(X)),
    fact(mammal(X)),
    \+ fact(pet(X)).

% Forward chaining: apply rule repeatedly until no new facts
forward :-
    pet_rule(X),
    assertz(fact(pet(X))),
    forward.
forward.   % halt when no rule applies