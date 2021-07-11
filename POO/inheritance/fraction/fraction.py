class Fraction:
    numerator = 0
    denominator = 0

    def __init__(self, numerator, denominator):
        if isinstance(numerator, int):
            self.numerator = numerator
        else:
            self.numerator = 0
        if isinstance(denominator, int) and denominator != 0:
            self.denominator = denominator
        else:
            self.denominator = 1
        self.simplify()

    def __str__(self):
        if self.denominator == 1:
            return (str(self.numerator))
        elif self.numerator == 0:
            return ("0")
        elif self.denominator == 0:
            return ("Indeterminate")
        else:
            return ("("+str(self.numerator) + "/"+str(self.denominator)+")")

    def to_print(self):
        print(self.numerator, "/", self.denominator)

    def multiply(self, fraction):
        numerator = self.numerator * fraction.numerator
        denominator = self.denominator * fraction.denominator
        result = Fraction(numerator, denominator)
        result.simplify()
        return result

    def __add__(self, fraction):
        numerator = self.numerator * fraction.denominator + \
            self.denominator * fraction.numerator
        denominator = self.denominator * fraction.denominator
        result = Fraction(numerator, denominator)
        result.simplify()
        return result

    def __sub__(self, fraction):
        numerator = self.numerator * fraction.denominator - \
            self.denominator * fraction.numerator
        denominator = self.denominator * fraction.denominator
        result = Fraction(numerator, denominator)
        result.simplify()
        return result

    def __mul__(self, fraction):
        numerator = self.numerator * fraction.numerator
        denominator = self.denominator * fraction.denominator
        result = Fraction(numerator, denominator)
        result.simplify()
        return result

    def __truediv__(self, fraction):
        numerator = self.numerator * fraction.denominator
        denominator = self.denominator * fraction.numerator
        result = Fraction(numerator, denominator)
        result.simplify()
        return result

    def __eq__(self, fraction):
        if self.numerator/self.denominator == fraction.numerator/fraction.denominator:
            return True
        else:
            return False

    def __it__(self, fraction):
        if self.numerator/self.denominator < fraction.numerator/fraction.denominator:
            return True
        else:
            return False

    def __gt__(self, fraction):
        if self.numerator/self.denominator > fraction.numerator/fraction.denominator:
            return True
        else:
            return False

    def simplify(self):
        greatest_common_divisor = self.calculate_greatest_common_divisor(
            self.numerator, self.denominator)
        self.numerator = int(self.numerator/greatest_common_divisor)
        self.denominator = int(self.denominator/greatest_common_divisor)

    def calculate_greatest_common_divisor(self, a, b):
        if b == 0:
            return a
        else:
            return self.calculate_greatest_common_divisor(b, a % b)
