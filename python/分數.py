from typing import Any, Self, Iterable, Optional, Literal, Mapping

class Fraction:
    def __init__(self, numerator, denominator=1):
        if type(numerator) == float:
            while numerator - int(numerator) != 0:
                denominator *= 10
                numerator *= 10
            numerator = int(numerator)
        elif type(numerator) == Fraction:
            denominator *= numerator.denominator
            numerator = numerator.numerator
        elif type(numerator) != int:
            try:
                numerator = int(numerator)
            except:
                raise TypeError()

        if type(denominator) == float:
            while denominator - int(denominator) != 0:
                denominator *= 10
                numerator *= 10
            denominator = int(denominator)
        elif type(denominator) == Fraction:
            numerator *= denominator.denominator
            denominator = denominator.numerator
        elif type(denominator) != int:
            try:
                denominator = int(denominator)
            except:
                raise TypeError()
        self.approx()

    def approx(self):
        for i in range(2, min(self.numerator, self.denominator)+1):
            if self.numerator % i == 0 and self.denominator % i == 0:
                self.denominator /= i
                self.numerator /= i
