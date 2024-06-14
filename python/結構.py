from typing import Any, Self, Iterable, Optional, Literal, Mapping

class Node:
    def __init__(self, name:Any, son:Optional[Iterable[Self]|Self]=None):
        self.name = name
        if type(son) == Node:
            self.son = [son]
        else:
            self.son = list(son)

class Tree:
    def __init__(self, node_list:Iterable[Node]|Mapping[Any, Any]):
        if type(node_list) == Iterable:
            self.l = list(node_list)
        elif type(node_list) == Mapping:
            pass
        self.build_tree(0)

    def build_tree(self, mode:Literal[0, 1, 2, 3, 4]):
        pass