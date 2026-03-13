symptom(john, fever).
symptom(john, cough).
symptom(john, fatigue).
symptom(mary, cough).
symptom(mary, sneeze).
disease(flu, [fever, cough, fatigue]).
disease(cold, [cough, sneeze]).
disease(covid, [fever, cough, loss_of_taste]).
diagnose(Patient, Disease) :-
    disease(Disease, SymptomList),
    forall(member(S, SymptomList), symptom(Patient, S)).