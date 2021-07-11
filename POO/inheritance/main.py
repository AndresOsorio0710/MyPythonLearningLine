from fraction import Fraction, MixedFraction
from vehicle import Vehicle, Car


def main():
    car_a = Car("Blue", 4, 120, 1500)
    vehicle_a = Vehicle("Red", 4)
    print(car_a)
    print(vehicle_a)
    fraction_a = Fraction(8, 6)
    fraction_b = Fraction(4, 3)
    mixed_fraction_a = MixedFraction(4, 8, 6)
    mixed_fraction_b = MixedFraction(3, 7, 4)
    print(fraction_a)
    print(fraction_b)
    print(f"{fraction_a}+{fraction_b}={fraction_a+fraction_b}")
    print(f"{fraction_a}-{fraction_b}={fraction_a-fraction_b}")
    print(f"{fraction_a}*{fraction_b}={fraction_a*fraction_b}")
    print(f"{fraction_a}/{fraction_b}={fraction_a/fraction_b}")
    print(f"\n{mixed_fraction_a}")
    print(mixed_fraction_b)
    print(f"{mixed_fraction_a}+{mixed_fraction_b}={mixed_fraction_a+mixed_fraction_b}")
    # print(f"{fraction_a}-{fraction_b}={fraction_a-fraction_b}")
    # print(f"{fraction_a}*{fraction_b}={fraction_a*fraction_b}")
    # print(f"{fraction_a}/{fraction_b}={fraction_a/fraction_b}")


if __name__ == "__main__":
    main()
