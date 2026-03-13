diet(diabetes, 'Avoid sugar, eat low-carb').
diet(hypertension, 'Low salt, more fruits and vegetables').
diet(anemia, 'Iron-rich foods like spinach and red meat').
diet(celiac, 'Strict gluten-free diet').
suggest_diet(Disease) :-
    diet(Disease, Suggestion),
    format('For ~w: ~w~n', [Disease, Suggestion]).