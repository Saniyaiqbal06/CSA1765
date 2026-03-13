bird(sparrow).
bird(penguin).
bird(eagle).
fly(sparrow).
fly(eagle).
% rule: a bird can fly if it is known to fly
can_fly(X) :- bird(X), fly(X).