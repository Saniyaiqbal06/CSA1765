vowel(a). vowel(e). vowel(i). vowel(o). vowel(u).

count_vowels([], 0).
count_vowels([H|T], Count) :-
    vowel(H),
    count_vowels(T, Rest),
    Count is Rest + 1.
count_vowels([_|T], Count) :-
    count_vowels(T, Count).

% Query: count_vowels([h,e,l,l,o], N).          % N = 2 (e,o)
% Query: count_vowels([p,r,o,l,o,g], N).        % N = 2 (o,o)