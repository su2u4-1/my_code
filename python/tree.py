def print_tree(node: int, tree_structure: dict[int, list[int]], tree: dict[int, int], indent: str = "", is_last: bool = True) -> None:
    branch = "└── " if is_last else "├── "
    output.append(f"{indent}{branch}{tree[node]}>{node}")
    indent += "    " if is_last else "│   "
    if node in tree_structure:
        children = tree_structure[node]
        for i, child in enumerate(children):
            print_tree(child, tree_structure, tree, indent, i == len(children) - 1)


tree: dict[int, int] = {}
output: list[str] = []
tree_structure: dict[int, list[int]] = {}
d: list[tuple[int, int]] = []
with open("./virus.txt", "r") as f:
    for i in f.readlines()[102:-1]:
        i = i.split()
        tree[int(i[0][:-1])] = int(i[-1][:-2])
for k, v in tree.items():
    if v == -1:
        continue
    elif v not in tree_structure:
        tree_structure[v] = []
    tree_structure[v].append(k)
output.append("0")
children = tree_structure[0]
for i, k in enumerate(children):
    print_tree(k, tree_structure, tree, "", i == len(children) - 1)
with open("./tree.txt", "w+") as f:
    f.write("\n".join(output))
for k, v in tree_structure.items():
    d.append((k, len(v)))
d.sort(key=lambda x: x[1])
for i in d:
    print(i)


import matplotlib.axes as axes
import matplotlib.figure as fi
import matplotlib.pyplot as plt
import networkx as nx
import seaborn as sns
from random import random

G = nx.DiGraph()
for k, v in tree.items():
    if v == -1:
        G.add_node(k)
    else:
        G.add_edge(v, k)
colors = [random() for _ in G.nodes()]
cmap = sns.color_palette("coolwarm", as_cmap=True)
nx.draw(
    G,
    nx.spring_layout(G),
    with_labels=True,
    node_size=[100 for _ in G.nodes()],
    node_color=colors,
    cmap=cmap,
    edge_color="gray",
    arrows=False,
)
sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=min(colors), vmax=max(colors)))
sm.set_array([])
plt.colorbar(sm, axes.Axes(fi.Figure(None), 1, 1, 1))
plt.show()
