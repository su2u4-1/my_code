from typing import Optional, Any
from math import gcd, lcm
from numbers import Number


class Fraction(Number):
    def __init__(self, a: Any, b: Any = 1) -> None:
        if isinstance(a, str):
            if a.count("/") == 1:
                a = Fraction(*map(int, a.split("/")))
            else:
                a = float(a)
        if isinstance(b, str):
            if b.count("/") == 1:
                b = Fraction(*map(int, b.split("/")))
            else:
                b = float(b)
        if not isinstance(a, (int, float, Fraction)) or not isinstance(b, (int, float, Fraction)):
            raise TypeError("Arguments must be numbers.")
        if b == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        if isinstance(a, float) and not a.is_integer():
            a = Fraction(*a.as_integer_ratio())
        elif isinstance(a, Fraction):
            b *= a.b
            a = a.a
        if isinstance(b, float) and not b.is_integer():
            b = Fraction(*b.as_integer_ratio())
        elif isinstance(b, Fraction):
            a *= b.b
            b = b.a
        self.a: int = int(a)
        self.b: int = int(b)
        self._approx()

    def __add__(self, other: Any) -> "Fraction":
        try:
            other = Fraction(other)
        except TypeError:
            return NotImplemented
        b = lcm(self.b, other.b)
        a = self.a * (b // self.b) + other.a * (b // other.b)
        return Fraction(a, b)

    def __sub__(self, other: Any) -> "Fraction":
        try:
            other = Fraction(other)
        except TypeError:
            return NotImplemented
        b = lcm(self.b, other.b)
        a = self.a * (b // self.b) - other.a * (b // other.b)
        return Fraction(a, b)

    def __mul__(self, other: Any) -> "Fraction":
        try:
            other = Fraction(other)
        except TypeError:
            return NotImplemented
        return Fraction(self.a * other.a, self.b * other.b)

    def __truediv__(self, other: Any) -> "Fraction":
        try:
            other = Fraction(other)
        except TypeError:
            return NotImplemented
        if other == 0:
            raise ZeroDivisionError("division by zero")
        return Fraction(self.a * other.b, self.b * other.a)

    def __floordiv__(self, other: Any) -> int:
        try:
            other = Fraction(other)
        except TypeError:
            return NotImplemented
        if other == 0:
            raise ZeroDivisionError("division by zero")
        return (self.a * other.b) // (self.b * other.a)

    def __mod__(self, other: Any) -> "Fraction":
        return self - other * (self // other)

    def __divmod__(self, other: Any) -> tuple[int, "Fraction"]:
        return self.__floordiv__(other), self.__mod__(other)

    def __pow__(self, other: Any, mod: Optional[Number] = None) -> "Fraction":
        def root(x: int, n: int) -> tuple[bool, int]:
            if x < 0 and n % 2 == 0:
                return False, -1
            if x < 0:
                x = -x
            low, high = 0, x + 1
            while low + 1 < high:
                mid = (low + high) // 2
                p = mid**n
                if p == x:
                    return True, mid if x >= 0 else -mid
                elif p < x:
                    low = mid
                else:
                    high = mid
            return False, -1

        try:
            o = Fraction(other)
        except TypeError:
            return NotImplemented
        if self.a == 0:
            if o == 0:
                raise ValueError("0 cannot be raised to the power of 0.")
            return Fraction(0)
        if self.a == 1:
            return Fraction(1)
        t = Fraction(self)
        if o.a < 0:
            o.a *= -1
            t.a, t.b = t.b, t.a
        if o.b == 1:
            t.a = t.a**o.a
            t.b = t.b**o.a
        else:
            f, t.a = root(t.a, o.b)
            if not f:
                raise ValueError("Result is not a rational number.")
            t.a = t.a**o.a
            f, t.b = root(t.b, o.b)
            if not f:
                raise ValueError("Result is not a rational number.")
            t.b = t.b**o.a
        t._approx()
        if mod is None:
            return t
        return t.__mod__(mod)

    def __radd__(self, other: Any) -> "Fraction":
        return self.__add__(other)

    def __rsub__(self, other: Any) -> "Fraction":
        try:
            other = Fraction(other)
        except TypeError:
            return NotImplemented
        return other.__sub__(self)

    def __rmul__(self, other: Any) -> "Fraction":
        return self.__mul__(other)

    def __rtruediv__(self, other: Any) -> "Fraction":
        try:
            other = Fraction(other)
        except TypeError:
            return NotImplemented
        return other.__truediv__(self)

    def __rfloordiv__(self, other: Any) -> int:
        try:
            other = Fraction(other)
        except TypeError:
            return NotImplemented
        return other.__floordiv__(self)

    def __rmod__(self, other: Any) -> "Fraction":
        try:
            other = Fraction(other)
        except TypeError:
            return NotImplemented
        return other.__mod__(self)

    def __rdivmod__(self, other: Any) -> tuple[int, "Fraction"]:
        return self.__rfloordiv__(other), self.__rmod__(other)

    def __rpow__(self, other: Any, mod: Optional[Number] = None) -> "Fraction":
        try:
            other = Fraction(other)
        except TypeError:
            return NotImplemented
        return other.__pow__(self, mod)

    def __iadd__(self, other: Any) -> "Fraction":
        return self.__add__(other)

    def __isub__(self, other: Any) -> "Fraction":
        return self.__sub__(other)

    def __imul__(self, other: Any) -> "Fraction":
        return self.__mul__(other)

    def __itruediv__(self, other: Any) -> "Fraction":
        return self.__truediv__(other)

    def __ifloordiv__(self, other: Any) -> int:
        return self.__floordiv__(other)

    def __imod__(self, other: Any) -> "Fraction":
        return self.__mod__(other)

    def __ipow__(self, other: Any, modulo: Optional[None] = None) -> "Fraction":
        return self.__pow__(other, modulo)

    def __neg__(self) -> "Fraction":
        return Fraction(-self.a, self.b)

    def __pos__(self) -> "Fraction":
        return Fraction(self.a, self.b)

    def __abs__(self) -> "Fraction":
        return Fraction(abs(self.a), self.b)

    def __complex__(self) -> complex:
        return complex(self.__float__())

    def __int__(self) -> int:
        return int(self.__float__())

    def __float__(self) -> float:
        return self.a / self.b

    def __index__(self) -> int:
        return self.__int__()

    def __round__(self, n_digits: Optional[int] = None) -> "Fraction":
        a, b = self.a, self.b
        m = 1
        if n_digits is not None:
            a *= 10**n_digits
            m = 10**n_digits
        if (a % b) * 2 >= b:
            return Fraction(a // b + 1, m)
        else:
            return Fraction(a // b, m)

    def __trunc__(self) -> int:
        if self < 0:
            return self.__ceil__()
        return self.__floor__()

    def __floor__(self) -> int:
        q, r = divmod(self.a, self.b)
        return q if self.a >= 0 else q - (1 if r != 0 else 0)

    def __ceil__(self) -> int:
        q, r = divmod(self.a, self.b)
        return q if self.a <= 0 else q + (1 if r != 0 else 0)

    def __lt__(self, other: Any) -> bool:
        try:
            other = Fraction(other)
        except TypeError:
            return NotImplemented
        return self.a * other.b < other.a * self.b

    def __le__(self, other: Any) -> bool:
        return self.__eq__(other) or self.__lt__(other)

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Fraction):
            try:
                value = Fraction(value)
            except TypeError:
                return NotImplemented
        return self.a == value.a and self.b == value.b

    def __ne__(self, value: object) -> bool:
        if not isinstance(value, Fraction):
            try:
                value = Fraction(value)
            except TypeError:
                return NotImplemented
        return self.a != value.a or self.b != value.b

    def __gt__(self, other: Any) -> bool:
        try:
            other = Fraction(other)
        except TypeError:
            return NotImplemented
        return self.a * other.b > other.a * self.b

    def __ge__(self, other: Any) -> bool:
        return self.__eq__(other) or self.__gt__(other)

    def __str__(self) -> str:
        if self.a == 0:
            return "0"
        if self.b == 1:
            return str(self.a)
        return f"{self.a}/{self.b}"

    def __repr__(self) -> str:
        return f"Fraction({self.a}/{self.b})"

    def __format__(self, _) -> str:
        return self.__str__()

    def __hash__(self) -> int:
        return hash((self.a, self.b))

    def _approx(self) -> None:
        if self.b < 0:
            self.a *= -1
            self.b *= -1
        i = gcd(self.a, self.b)
        self.a //= i
        self.b //= i
