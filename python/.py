from math import trunc, floor, ceil
from fraction import Fraction

a = Fraction(3, 2)
aa = 1.5
b = Fraction(-3, 4)
ba = -0.75
c = 2.5
tq = [a, b, c]
ta = [aa, ba, c]

for i in range(3):
    for j in range(3):
        print(tq[i], tq[j])
        print("+")
        if (tq[i] + tq[j]) != (ta[i] + ta[j]):
            print("+", tq[i] + tq[j], end=", ans: ")
            print(ta[i] + ta[j])
        print("-")
        if (tq[i] - tq[j]) != (ta[i] - ta[j]):
            print("-", tq[i] - tq[j], end=", ans: ")
            print(ta[i] - ta[j])
        print("*")
        if (tq[i] * tq[j]) != (ta[i] * ta[j]):
            print("*", tq[i] * tq[j], end=", ans: ")
            print(ta[i] * ta[j])
        print("/")
        if (tq[i] / tq[j]) != (ta[i] / ta[j]):
            print("/", tq[i] / tq[j], end=", ans: ")
            print(ta[i] / ta[j])
        print("//")
        if (tq[i] // tq[j]) != (ta[i] // ta[j]):
            print("//", tq[i] // tq[j], end=", ans: ")
            print(ta[i] // ta[j])
        print("%")
        if (tq[i] % tq[j]) != (ta[i] % ta[j]):
            print("%", tq[i] % tq[j], end=", ans: ")
            print(ta[i] % ta[j])
        print("**")
        if (abs(tq[i]) ** tq[j]) != (abs(ta[i]) ** ta[j]):
            t = abs(tq[i]) ** tq[j]
            t1 = abs(ta[i]) ** ta[j]
            if round(t.numerator / t.denominator, 5) != round(t1, 5):
                print("**", t, end=", ans: ")
                print(t1)
                print(t.numerator / t.denominator, t1, (t.numerator / t.denominator) == t1)
        print("<")
        if (tq[i] < tq[j]) != (ta[i] < ta[j]):
            print("<", tq[i] < tq[j], end=", ans: ")
            print(ta[i] < ta[j])
        print("<=")
        if (tq[i] <= tq[j]) != (ta[i] <= ta[j]):
            print("<=", tq[i] <= tq[j], end=", ans: ")
            print(ta[i] <= ta[j])
        print("==")
        if (tq[i] == tq[j]) != (ta[i] == ta[j]):
            print("==", tq[i] == tq[j], end=", ans: ")
            print(ta[i] == ta[j])
        print("!=")
        if (tq[i] != tq[j]) != (ta[i] != ta[j]):
            print("!=", tq[i] != tq[j], end=", ans: ")
            print(ta[i] != ta[j])
        print(">")
        if (tq[i] > tq[j]) != (ta[i] > ta[j]):
            print(">", tq[i] > tq[j], end=", ans: ")
            print(ta[i] > ta[j])
        print(">=")
        if (tq[i] >= tq[j]) != (ta[i] >= ta[j]):
            print(">=", tq[i] >= tq[j], end=", ans: ")
            print(ta[i] >= ta[j])
        print("divmod")
        if divmod(tq[i], tq[j]) != divmod(ta[i], ta[j]):
            print("divmod", divmod(tq[i], tq[j]), end=", ans: ")
            print(divmod(ta[i], ta[j]))

"""print(abs())
print(complex())
print(int())
print(float())
print(round())
print(trunc())
print(floor())
print(ceil())
print(str())
print(repr())
print('{}'.format())
print(hash())"""
