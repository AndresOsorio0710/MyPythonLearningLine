class Fraction:
    numerator = 0
    denominator = 0

    def __init__(self, numerator, denominator):
        # print("Constructor")
        # print(self.numerator)
        # print(self.denominator)
        # self.numerator = numerator
        # self.denominator = denominator
        if isinstance(numerator, int):
            self.numerator = numerator
        else:
            self.numerator = 0
        if isinstance(denominator, int) and denominator != 0:
            self.denominator = denominator
        else:
            self.denominator = 1

    def __del__(self):
        print("Destroyed the object", self.numerator, "/", self.denominator)

    def __str__(self):
        return ("{"+str(self.numerator) + "/"+str(self.denominator)+"}")

    def to_print(self):
        print(self.numerator, "/", self.denominator)

    def multiply(self, fraction):
        numerator = self.numerator * fraction.numerator
        denominator = self.denominator * fraction.denominator
        result = Fraction(numerator, denominator)
        return result

    def __add__(self, fraction):
        numerator = self.numerator * fraction.denominator + \
            self.denominator * fraction.numerator
        denominator = self.denominator * fraction.denominator
        result = Fraction(numerator, denominator)
        return result

    def __sub__(self, fraction):
        numerator = self.numerator * fraction.denominator - \
            self.denominator * fraction.numerator
        denominator = self.denominator * fraction.denominator
        result = Fraction(numerator, denominator)
        return result

    def __mul__(self, fraction):
        numerator = self.numerator * fraction.numerator
        denominator = self.denominator * fraction.denominator
        result = Fraction(numerator, denominator)
        return result

    def __truediv__(self, fraction):
        numerator = self.numerator * fraction.denominator
        denominator = self.denominator * fraction.numerator
        result = Fraction(numerator, denominator)
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


def main():
    # fraction_a = Fraction(3, 2)
    # fraction_a.to_print()
    #fraction_b = Fraction(7, 4)
    # fraction_b.to_print()
    # fraction_c = fraction_a.multiply(fraction_b)
    # fraction_c.to_print()
    #fraction_a = Fraction(3.6, 2)
    # fraction_a.to_print()
    fraction_a = Fraction(2, 10)
    # fraction_a.to_print()
    # print(fraction_a)
    fraction_b = Fraction(4, 5)
    # fraction_b.to_print()
    #fraction_c = fraction_a*fraction_b
    #print("*", fraction_c)
    #fraction_c = fraction_a+fraction_b
    #print("+", fraction_c)
    #fraction_c = fraction_a-fraction_b
    #print("-", fraction_c)
    print("==", fraction_a == fraction_b)
    print(">", fraction_a > fraction_b)
    print("<", fraction_a < fraction_b)
    fraction_c = fraction_a/fraction_b
    print(fraction_c)


if __name__ == "__main__":
    main()
