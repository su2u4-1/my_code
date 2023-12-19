# u上d下l左r右f前b後
# w白y黃o橘r紅g綠b藍
rc = {}
for i in range(9):
    rc[f"u{i}"] = "w"
    rc[f"d{i}"] = "y"
    rc[f"l{i}"] = "o"
    rc[f"r{i}"] = "r"
    rc[f"f{i}"] = "g"
    rc[f"b{i}"] = "b"

"""
0 1 2
3 4 5
6 7 8
"""


def r1(s: str):  # 順
    a = rc[f"{s}0"]
    rc[f"{s}0"] = rc[f"{s}6"]
    rc[f"{s}6"] = rc[f"{s}8"]
    rc[f"{s}8"] = rc[f"{s}2"]
    rc[f"{s}2"] = a
    a = rc[f"{s}1"]
    rc[f"{s}1"] = rc[f"{s}3"]
    rc[f"{s}3"] = rc[f"{s}7"]
    rc[f"{s}7"] = rc[f"{s}5"]
    rc[f"{s}5"] = a


def r2(s: str):  # 逆
    a = rc[f"{s}0"]
    rc[f"{s}0"] = rc[f"{s}2"]
    rc[f"{s}2"] = rc[f"{s}8"]
    rc[f"{s}8"] = rc[f"{s}6"]
    rc[f"{s}6"] = a
    a = rc[f"{s}1"]
    rc[f"{s}1"] = rc[f"{s}5"]
    rc[f"{s}5"] = rc[f"{s}7"]
    rc[f"{s}7"] = rc[f"{s}3"]
    rc[f"{s}3"] = a


def f1l():
    for i in range(3):
        a = rc[f"f{i}"]
        rc[f"f{i}"] = rc[f"r{i}"]
        rc[f"r{i}"] = rc[f"b{i}"]
        rc[f"b{i}"] = rc[f"l{i}"]
        rc[f"l{i}"] = a
    r1("u")


def f2l():
    for i in range(3, 6):
        a = rc[f"f{i}"]
        rc[f"f{i}"] = rc[f"r{i}"]
        rc[f"r{i}"] = rc[f"b{i}"]
        rc[f"b{i}"] = rc[f"l{i}"]
        rc[f"l{i}"] = a


def f3l():
    for i in range(6, 9):
        a = rc[f"f{i}"]
        rc[f"f{i}"] = rc[f"r{i}"]
        rc[f"r{i}"] = rc[f"b{i}"]
        rc[f"b{i}"] = rc[f"l{i}"]
        rc[f"l{i}"] = a
    r2("d")


def f1r():
    for i in range(3):
        a = rc[f"f{i}"]
        rc[f"f{i}"] = rc[f"l{i}"]
        rc[f"l{i}"] = rc[f"b{i}"]
        rc[f"b{i}"] = rc[f"r{i}"]
        rc[f"r{i}"] = a
    r2("u")


def f2r():
    for i in range(3, 6):
        a = rc[f"f{i}"]
        rc[f"f{i}"] = rc[f"l{i}"]
        rc[f"l{i}"] = rc[f"b{i}"]
        rc[f"b{i}"] = rc[f"r{i}"]
        rc[f"r{i}"] = a


def f3r():
    for i in range(6, 9):
        a = rc[f"f{i}"]
        rc[f"f{i}"] = rc[f"l{i}"]
        rc[f"l{i}"] = rc[f"b{i}"]
        rc[f"b{i}"] = rc[f"r{i}"]
        rc[f"r{i}"] = a
    r1("u")


def l1l():
    pass


def l2l():
    pass


def l3l():
    pass


def l1r():
    pass


def l2r():
    pass


def l3r():
    pass


def r1l():
    pass


def r2l():
    pass


def r3l():
    pass


def r1r():
    pass


def r2r():
    pass


def r3r():
    pass
