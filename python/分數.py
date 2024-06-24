from typing import Any, Self, Iterable, Optional, Literal, Mapping

class Fraction:
    def __init__(self, *args):
        if len(args) == 1:
            if type(args[0]) == float:
                pass
            elif type(args[0]) == int:
                pass
            elif type(args[0]) == Fraction:
                pass
        elif len(args) == 2:
            pass
        else:
            raise TypeError()