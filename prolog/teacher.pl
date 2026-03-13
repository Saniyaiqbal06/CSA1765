teaches(john, math).
teaches(jane, english).
teaches(bob, science).
teaches(sue, history).
teaches(tom, art).
takes(alice, math).
takes(alice, science).
takes(bob, english).
takes(bob, science).
takes(carol, history).
takes(carol, art).
takes(dave, math).
takes(dave, english).
takes(dave, art).
teaching_subjects(Teacher, Subject) :-
    teaches(Teacher, Subject).
taking_students(Subject, Student) :-
    takes(Student, Subject).