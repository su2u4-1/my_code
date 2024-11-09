from typing import Optional
import numbers


def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


class Fraction(numbers.Number):
    def __init__(self, numerator: "N", denominator: "N" = 1) -> None:
        if isinstance(numerator, float):
            while not numerator.is_integer():
                denominator *= 10
                numerator *= 10
            numerator = int(numerator)
        elif isinstance(numerator, Fraction):
            denominator *= numerator.denominator
            numerator = numerator.numerator
        else:
            numerator = int(numerator)
        if isinstance(denominator, float):
            while not denominator.is_integer():
                denominator *= 10
                numerator *= 10
            denominator = int(denominator)
        elif isinstance(denominator, Fraction):
            numerator *= denominator.denominator
            denominator = denominator.numerator
        else:
            denominator = int(denominator)
        self.numerator: int = numerator
        self.denominator: int = denominator
        self.approx()

    def __add__(self, other: "N") -> "Fraction":
        if not isinstance(other, Fraction):
            try:
                other = Fraction(other)
            except:
                return NotImplemented
        denominator = lcm(self.denominator, other.denominator)
        numerator = self.numerator * (denominator / self.denominator) + other.numerator * (denominator / other.denominator)
        return Fraction(numerator, denominator)

    def __sub__(self, other: "N") -> "Fraction":
        if not isinstance(other, Fraction):
            try:
                other = Fraction(other)
            except:
                return NotImplemented
        denominator = lcm(self.denominator, other.denominator)
        numerator = self.numerator * (denominator / self.denominator) - other.numerator * (denominator / other.denominator)
        return Fraction(numerator, denominator)

    def __mul__(self, other: "N") -> "Fraction":
        if not isinstance(other, Fraction):
            try:
                other = Fraction(other)
            except:
                return NotImplemented
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other: "N") -> "Fraction":
        if not isinstance(other, Fraction):
            try:
                other = Fraction(other)
            except:
                return NotImplemented
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __floordiv__(self, other: "N") -> int:
        if not isinstance(other, Fraction):
            try:
                other = Fraction(other)
            except:
                return NotImplemented
        return (self.numerator * other.denominator) // (self.denominator * other.numerator)

    def __mod__(self, other: "N") -> "Fraction":
        return self - other * (self // other)

    def __divmod__(self, other: "N") -> tuple[int, "Fraction"]:
        return self.__floordiv__(other), self.__mod__(other)

    def __pow__(self, other: "N", mod: Optional["N"] = None) -> "Fraction":
        if self.numerator < 0:
            raise ValueError()
        if self.numerator == 0:
            if other == 0:
                raise ValueError()
            return Fraction(0)
        if self.numerator == 1:
            return Fraction(1)
        t = Fraction(self)
        if type(other) == int or type(other) == float:
            t.numerator = t.numerator**other
            t.denominator = t.denominator**other
            if type(other) == float:
                t.approx()
        else:
            if not isinstance(other, Fraction):
                try:
                    other = Fraction(other)
                except:
                    return NotImplemented
            t.numerator = t.numerator**other.numerator
            t.numerator = t.numerator ** (1 / other.denominator)
            t.denominator = t.denominator**other.numerator
            t.denominator = t.denominator ** (1 / other.denominator)
            t.approx()
        if mod is None:
            return t
        return t.__mod__(mod)

    def __radd__(self, other: "N") -> "Fraction":
        return self.__add__(other)

    def __rsub__(self, other: "N") -> "Fraction":
        if not isinstance(other, Fraction):
            try:
                other = Fraction(other)
            except:
                return NotImplemented
        denominator = lcm(self.denominator, other.denominator)
        numerator = other.numerator * (denominator / other.denominator) - self.numerator * (denominator / self.denominator)
        return Fraction(numerator, denominator)

    def __rmul__(self, other: "N") -> "Fraction":
        return self.__mul__(other)

    def __rtruediv__(self, other: "N") -> "Fraction":
        if not isinstance(other, Fraction):
            try:
                other = Fraction(other)
            except:
                return NotImplemented
        return Fraction(self.denominator * other.numerator, self.numerator * other.denominator)

    def __rfloordiv__(self, other: "N") -> int:
        if isinstance(other, int) or isinstance(other, float):
            return self.denominator * other // self.numerator
        if not isinstance(other, Fraction):
            try:
                other = Fraction(other)
            except:
                return NotImplemented
        return self.denominator * other.numerator // self.numerator * other.denominator

    def __rmod__(self, other: "N") -> "Fraction":
        if not isinstance(other, Fraction):
            try:
                other = Fraction(other)
            except:
                return NotImplemented
        return other.__mod__(self)

    def __rdivmod__(self, other: "N") -> tuple[int, "Fraction"]:
        return self.__rfloordiv__(other), self.__rmod__(other)

    def __rpow__(self, other: "N", mod: Optional["N"] = None) -> "Fraction":
        if not isinstance(other, Fraction):
            try:
                other = Fraction(other)
            except:
                return NotImplemented
        other.numerator = other.numerator**self.numerator
        other.numerator = other.numerator ** (1 / self.denominator)
        other.denominator = other.denominator**self.numerator
        other.denominator = other.denominator ** (1 / self.denominator)
        other.approx()
        if mod is None:
            return other
        return other.__mod__(mod)

    def __iadd__(self, other: "N") -> "Fraction":
        return self.__add__(other)

    def __isub__(self, other: "N") -> "Fraction":
        return self.__sub__(other)

    def __imul__(self, other: "N") -> "Fraction":
        return self.__mul__(other)

    def __itruediv__(self, other: "N") -> "Fraction":
        return self.__truediv__(other)

    def __ifloordiv__(self, other: "N") -> int:
        return self.__floordiv__(other)

    def __imod__(self, other: "N") -> "Fraction":
        return self.__mod__(other)

    def __ipow__(self, other: "N", modulo: Optional[None] = None) -> "Fraction":
        return self.__pow__(other, modulo)

    def __neg__(self) -> "Fraction":
        return self * -1

    def __pos__(self) -> "Fraction":
        return self

    def __abs__(self) -> "Fraction":
        if self < 0:
            return self.__neg__()
        return self

    def __complex__(self) -> complex:
        return complex(self.__float__())

    def __int__(self) -> int:
        return int(self.__float__())

    def __float__(self) -> float:
        return self.numerator / self.denominator

    def __index__(self) -> int:
        return self.__int__()

    def __round__(self, ndigits: int | None = None) -> int | float:
        if ndigits is None:
            return round(self.__float__())
        return round(self.__float__(), ndigits)

    def __trunc__(self) -> int:
        if self < 0:
            return self.__ceil__()
        return self.__floor__()

    def __floor__(self) -> int:
        if self.numerator < 0:
            t = self.__float__()
            if t.is_integer():
                return int(t)
            return int(t) - 1
        else:
            return self.__int__()

    def __ceil__(self) -> int:
        if self.numerator > 0:
            t = self.__float__()
            if t.is_integer():
                return int(t)
            return int(t) + 1
        else:
            return self.__int__()

    def __lt__(self, other: "N") -> bool:
        if not isinstance(other, Fraction):
            try:
                other = Fraction(other)
            except:
                return NotImplemented
        denominator = lcm(self.denominator, other.denominator)
        return self.numerator * (denominator / self.denominator) < other.numerator * (denominator / other.denominator)

    def __le__(self, other: "N") -> bool:
        return self.__eq__(other) or self.__lt__(other)

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Fraction):
            try:
                value = Fraction(value)
            except:
                return NotImplemented
        return self.numerator == value.numerator and self.denominator == value.denominator

    def __ne__(self, value: object) -> bool:
        if not isinstance(value, Fraction):
            try:
                value = Fraction(value)
            except:
                return NotImplemented
        return self.numerator != value.numerator or self.denominator != value.denominator

    def __gt__(self, other: "N") -> bool:
        if not isinstance(other, Fraction):
            try:
                other = Fraction(other)
            except:
                return NotImplemented
        denominator = lcm(self.denominator, other.denominator)
        return self.numerator * (denominator / self.denominator) > other.numerator * (denominator / other.denominator)

    def __ge__(self, other: "N") -> bool:
        return self.__eq__(other) or self.__gt__(other)

    def __str__(self) -> str:
        if self.numerator == 0:
            return "0"
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self) -> str:
        return f"Fraction({self.numerator}/{self.denominator})"

    def __format__(self, _) -> str:
        return self.__str__()

    def __hash__(self) -> int:
        return hash((self.numerator, self.denominator))

    def approx(self) -> None:
        t = 1
        if self.numerator < 0:
            t = -1
            self.numerator = -self.numerator
        if self.denominator < 0:
            t *= -1
            self.denominator = -self.denominator
        i = gcd(self.numerator, self.denominator)
        self.numerator = int(self.numerator / i * t)
        self.denominator = int(self.denominator / i)


N = float | Fraction
