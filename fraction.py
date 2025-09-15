from gcd import gcd
# num = numerator; deno = denominator
class Fraction():
    def __init__(self, num, deno):
        if deno == 0:
            raise ValueError("Denominator cannot be 0")
        div = gcd(num, deno)
        self.num = num // div
        self.deno = deno // div

