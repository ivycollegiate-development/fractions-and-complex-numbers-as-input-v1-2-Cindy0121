try:
    from fractions import Fraction
    a = Fraction (input("Please input a fraction, ex: 3/4: "))
    print(a)
except ZeroDivisionError:
    print("Invalid fraction: denominator cannot be zero")
except ValueError:
    print("Invalid response. Please input a frational value.")