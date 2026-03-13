% Match pattern [X, Y, X] with a list
match([X,Y,X], List) :- List = [X,Y,X].

% Match list starting with 'a'
starts_with_a([a|_]).

% Extract head and tail
head_tail([H|T], H, T).

% Query: match([X,Y,X], [1,2,1]).          % X=1, Y=2
% Query: starts_with_a([a,b,c]).            % true
% Query: head_tail([1,2,3], H, T).          % H=1, T=[2,3]