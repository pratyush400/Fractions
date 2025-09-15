# Fractions
This is a group project for alogrithms class.
This assignment gives you practice writing Python classes, implementing nontrivial algorithms, and working as part of a team.

Define a class Fraction that represents a rational number with a numerator and a denominator (both assumed to be integers). This class should allow you to work with fractions in Python's read-eval-print loop:

>>> a = Fraction(2, 3)
>>> a
2/3
>>> b = Fraction(2, 8)
>>> b
1/4
>>> a + b
11/12
>>> float(a)
0.6666666666666666

All of the methods you need to implement are magic methods:

__init__-PJ
__repr__-EH
__add__-PJ
__sub__-JN
__mul__-EH
__truediv__-PJ
__float__-JN

This is a team assignment. When you are done, one member of your team should submit the file, including (as a comment at the top of the file) the names of everyone who contributed.
Files

    test_fraction.py

On Working as a Team

This project is, intentionally, too much for one student to complete in a reasonable amount of time. You will need to work together as a team!

The first thing to work out is communication and scheduling. Exchange email addresses or phone numbers. Set up a group chat or other means of communication. Figure out when you can meet to work on the project. It will take several hours. It's best if you can all work together, but if not, figure out who can work at what times and plan to hand off the code to the rest of the team after each session.

When working, it's a good idea to use pair programming.

Break the problem down into steps. Have one pair (or person) do the first step, then a different pair do the next step, and so on. Here's a good sequence for this assignment:

    Make sure everyone has the code and can run the tests.
    Pass test_represents_simple_fraction.
    Pass test_reduces_to_lowest_terms.
    Pass test_handles_negative_numerator.
    Pass test_handles_negative_denominator.
    Pass test_handles_negative_numerator_and_denominator.
    Pass test_represents_improper_fraction.
    Pass test_adds.
    Pass test_subtracts.
    Pass test_multiplies.
    Pass test_divides.
    Clean up the code: remove commented-out code, improve names of local variables, eliminate redundancy, etc.
    If you have time, save a copy and then consider tackling optional challenge problems.
    Clean up the code again.
    Have one person hand in your solution with everyone's names on it.

Remember to trade off who is "driving" (typing) after each step. Avoid having someone who never gets a chance to contribute or someone who "heroically" does almost all of the work. If you feel your teammates are more experienced than you, ask questions! If you feel you are more experienced, be patient and remember that making your team stronger is more important than completing the project as quickly as possible.
