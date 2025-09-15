#Define a class Fraction that represents a rational number with a numerator and a denominator (both assumed to be integers).
__author__ = 'Emma, Jolie, Pratyush'

from gcd import gcd
# num = numerator; deno = denominator
class Fraction:
    def __init__(self, num, deno):
        if deno == 0:
            raise ValueError("Denominator cannot be 0")
        div = gcd(num, deno)
        self.num = num // div
        self.deno = deno // div

    def __repr__(self):
        # return str(self.num)/str(self.deno)
        return f'{self.num}/{self.deno}'

    def __add__(self, other):
        return Fraction(self.num * other.deno + self.deno * other.num, self.deno*other.deno)

    def __truediv__(self, other):
        return Fraction(self.num*other.deno, self.deno*other.num)
    def __mul__(self, other):
        return Fraction(self.num*other.num, self.deno*other.deno)
v = Fraction(2,4)
