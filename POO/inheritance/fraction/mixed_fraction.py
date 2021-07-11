from .fraction import Fraction


class MixedFraction(Fraction):
    def __init__(self, integer, numerator, denominator):
        if isinstance(integer, int):
            self.integer = integer
        else:
            self.integer = 0
        super().__init__(numerator, denominator)
        self.simplify()
        super().simplify()

    def __str__(self):
        return str(self.integer)+super().__str__()

    def __add__(self, mixed_fraction):
        integer = self.integer+mixed_fraction.integer
        fraction = super().__add__(mixed_fraction)
        result = MixedFraction(
            integer, fraction.numerator, fraction.denominator)
        return result

    def simplify(self):
        if self.numerator > self.denominator:
            aux = self.numerator//self.denominator
            self.integer = self.integer+aux
            self.numerator -= (aux*self.denominator)
