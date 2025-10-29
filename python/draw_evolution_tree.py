#!/usr/bin/env python3
"""
draw_evolution_tree.py

讀取 cell_logs.json，將 parent == -1 的項目視為 root，建立父子樹，並繪製演化樹。
每個節點以一個六邊形呈現 dna（六個值在 [0,1]），六邊形的各頂點到中心的距離對應該 dna 值，便於可視化差異。

此版本會產生互動式 HTML（使用 Bokeh，預設輸出為 draw_tree_bokeh.html）。在互動模式下，節點中心可拖曳，六邊形與連線會即時更新。
請先安裝 Bokeh：
    pip install bokeh

用法範例:
    python draw_evolution_tree.py --json ../cell_logs.json --out draw_tree_bokeh.html --interactive

註：原始程式的早期版本會輸出靜態 PNG（matplotlib）；目前程式碼預設採用 Bokeh 互動輸出，因此文件與提示已更新。
"""
from json import load
from math import pi, cos, sin

from bokeh.plotting import figure, output_file, save
from bokeh.models import ColumnDataSource, CustomJS, HoverTool
from bokeh.models.tools import PointDrawTool


class Info:
    def __init__(self, id: int, parent: int, dna: list[float]) -> None:
        self.id = id
        self.parent = parent
        self.dna = dna


def load_nodes(json_path: str) -> tuple[dict[int, Info], dict[int, list[int]]]:
    """Load nodes from a JSON file.

    Returns a tuple (nodes, children) where:
      - nodes: mapping id -> {'id': id, 'parent': parent, 'dna': dna}
      - children: mapping parent_id -> list of child ids
    """
    with open(json_path, "r", encoding="utf-8") as f:
        data = load(f)
    nodes: dict[int, Info] = {}
    children: dict[int, list[int]] = {}
    for item in data:
        # robustly coerce ID and parent to int when possible
        id_raw = item.get("ID")
        parent_raw = item.get("parent")
        try:
            nid: int = int(id_raw)
        except (TypeError, ValueError):
            # fallback: keep as-is (but most JSON should have numeric IDs)
            nid = id_raw  # type: ignore
        try:
            parent: int = int(parent_raw)
        except (TypeError, ValueError):
            parent = -1
        # only keep what we need
        nodes[nid] = Info(nid, parent, item.get("dna"))
        children.setdefault(parent, []).append(nid)

    return nodes, children


def merge_identical_nodes(nodes: dict[int, Info], children: dict[int, list[int]]) -> tuple[dict[int, Info], dict[int, list[int]]]:
    """Merge nodes whose DNA are exactly identical and are either siblings (same parent)
    or in a parent-child relationship.

    Rules:
      - Nodes are considered equal only if their dna lists are exactly equal element-wise.
      - If nodes are connected by sibling or parent-child edges and have identical DNA,
        they are merged into a single node whose id is the minimum id in the group.
      - After merging, all parent references are updated to point to the representative id.
      - A representative must keep the same dna. If a parent's id maps to the same id as the
        child (self-parent), the parent is set to -1 (becomes a root).

    Returns updated (nodes, children) with merged nodes removed and children rebuilt.
    """
    # union-find (DSU) for grouping
    parent_map: dict[int, int] = {nid: nid for nid in nodes}

    def find(a: int) -> int:
        # path compression
        while parent_map[a] != a:
            parent_map[a] = parent_map[parent_map[a]]
            a = parent_map[a]
        return a

    def union(a: int, b: int) -> None:
        ra = find(a)
        rb = find(b)
        if ra == rb:
            return
        # keep smaller id as representative
        if ra < rb:
            parent_map[rb] = ra
        else:
            parent_map[ra] = rb

    def dna_key(dna_value: list[float]) -> tuple[float, float, float, float, float, float]:
        """Create a stable, hashable key from dna list.

        - Accepts lists/tuples of numbers.
        - Rounds floats to avoid tiny FP differences.
        - If dna is None or not iterable, return empty tuple.
        """
        return tuple(round(float(x), 2) for x in dna_value)  # type: ignore

    # union siblings with identical dna (group per parent)
    # children dict maps parent -> list of child ids
    for p, chs in list(children.items()):
        if not chs:
            continue
        # only consider children that still exist in nodes
        present_children = [c for c in chs if c in nodes]
        if len(present_children) <= 1:
            continue
        dna_groups: dict[tuple[float, ...], list[int]] = {}
        for c in present_children:
            dna_k = dna_key(nodes[c].dna)
            dna_groups.setdefault(dna_k, []).append(c)
        for same in dna_groups.values():
            if len(same) > 1:
                first = same[0]
                for other in same[1:]:
                    union(first, other)

    # union parent-child when dna identical
    for nid, info in list(nodes.items()):
        p = info.parent
        if p == -1:
            continue
        if p not in nodes:
            continue
        if dna_key(nodes[p].dna) == dna_key(nodes[nid].dna):
            union(p, nid)

    # build components mapping representative -> members
    comps: dict[int, list[int]] = {}
    for nid in nodes:
        rep = find(nid)
        comps.setdefault(rep, []).append(nid)

    # if no merges needed, return original
    merged_any = any(len(members) > 1 for members in comps.values())
    if not merged_any:
        return nodes, children

    # create mapping old_id -> new_rep (representative chosen as min id in component)
    old_to_new: dict[int, int] = {}
    for rep, members in comps.items():
        new_rep = min(members)
        for m in members:
            old_to_new[m] = new_rep

    # build new nodes dict keeping only representatives
    new_nodes: dict[int, Info] = {}
    for nid, info in nodes.items():
        rep = old_to_new[nid]
        if rep != nid:
            # skip merged-away node
            continue
        # update parent mapping through old_to_new
        orig_parent: int = info.parent
        if orig_parent == -1:
            new_parent = orig_parent
        else:
            new_parent = old_to_new.get(orig_parent, orig_parent)
            # avoid self-parent
            if new_parent == rep:
                new_parent = -1
        # keep dna from representative (no change)
        new_nodes[rep] = Info(rep, new_parent, info.dna)

    # rebuild children mapping (unique, sorted lists)
    new_children: dict[int, list[int]] = {}
    for nid, info in new_nodes.items():
        p: int = info.parent
        new_children.setdefault(p, []).append(nid)
    # ensure children lists are unique and sorted for determinism
    for k in list(new_children.keys()):
        vals = sorted(set(new_children[k]))
        new_children[k] = vals

    return new_nodes, new_children


def compute_positions(roots: list[int], children_map: dict[int, list[int]]) -> dict[int, tuple[float, float]]:
    """
    Simple tree layout: assign x positions by DFS-order for leaves, and center parents above their children.
    Multiple roots are placed left-to-right with a small gap.
    Returns: dict id -> (x, y)
    """
    positions: dict[int, tuple[float, float]] = {}
    x_counter: dict[str, float] = {"x": 0}

    def dfs(u: int, depth: int) -> tuple[float, float]:
        ch = children_map.get(u, [])
        if not ch:
            x = x_counter["x"]
            positions[u] = (x, -depth)
            x_counter["x"] += 1
            return positions[u]
        xs: list[float] = []
        for c in ch:
            xs.append(dfs(c, depth + 1)[0])
        xmin = min(xs)
        xmax = max(xs)
        positions[u] = ((xmin + xmax) / 2.0, -depth)
        return positions[u]

    # run DFS for each root, but insert a small gap between root subtrees
    gap = 1.0
    for _, r in enumerate(roots):
        dfs(r, 0)
        # after finishing subtree, add a gap
        x_counter["x"] += gap

    return positions


def hexagon_vertices(center: tuple[float, float], size: float, values: list[float]) -> list[tuple[float, float]]:
    """返回六邊形的頂點座標。values: 長度為6，取值 0..1，為每個方向的比例。
    center: (x,y), size: 最大半徑
    順序從角度 90° (向上) 開始，順時鐘。
    """
    cx, cy = center
    vert_list: list[tuple[float, float]] = []
    for i in range(6):
        angle = pi / 2 - i * (2 * pi / 6)  # start at top, clockwise
        r = max(0.0, min(1.0, values[i])) * size
        x = cx + r * cos(angle)
        y = cy + r * sin(angle)
        vert_list.append((x, y))
    return vert_list


def main() -> None:
    args_json = "d:/my_code/cell_logs.json"
    args_out = "d:/my_code/draw_tree_bokeh.html"
    args_node_size = 1.0
    args_interactive = True

    nodes, children = load_nodes(args_json)
    # merge nodes that have identical dna and are siblings or parent-child
    nodes, children = merge_identical_nodes(nodes, children)

    # find roots: parent == -1 (recompute after possible merges)
    roots = [nid for nid, info in nodes.items() if info.parent == -1]
    if not roots:
        print("找不到 parent == -1 的 root 節點")
        return

    # Build children_map keyed by node id. The children dict groups nodes by their parent id;
    # entries with parent == -1 represent top-level roots and are skipped here because
    # we treat roots separately (they are provided to compute_positions via `roots`).
    children_map: dict[int, list[int]] = {}
    for parent, chs in children.items():
        if parent == -1:
            # these are top-level roots; ensure they exist in nodes so we can layout
            continue
        children_map[parent] = chs

    # ensure that children entries exist for nodes even if empty
    for nid in nodes.keys():
        children_map.setdefault(nid, [])

    # Note: we do not create pseudo-parent nodes. Roots are passed directly to
    # compute_positions so each root subtree is laid out independently.

    positions = compute_positions(roots, children_map)

    if args_interactive:
        # prepare data for bokeh
        node_ids: list[str] = []
        xs: list[float] = []
        ys: list[float] = []
        dna_list: list[list[float]] = []
        patch_xs: list[list[float]] = []
        patch_ys: list[list[float]] = []
        for nid, info in nodes.items():
            if nid not in positions:
                continue
            x, y = positions[nid]
            node_ids.append(str(nid))
            xs.append(x)
            ys.append(y)
            dna: list[float] = info.dna
            dna_list.append(dna)
            vert_list = hexagon_vertices((x, y), args_node_size, dna)
            px = [v[0] for v in vert_list]
            py = [v[1] for v in vert_list]
            patch_xs.append(px)
            patch_ys.append(py)

        edge_xs: list[tuple[float, float]] = []
        edge_ys: list[tuple[float, float]] = []
        for nid, info in nodes.items():
            parent = info.parent
            if parent == -1:
                continue
            if parent not in positions or nid not in positions:
                continue
            x0, y0 = positions[parent]
            x1, y1 = positions[nid]
            edge_xs.append((x0, x1))
            edge_ys.append((y0, y1))

        patches_source = ColumnDataSource(data=dict(xs=patch_xs, ys=patch_ys, id=node_ids, dna=dna_list))
        centers_source = ColumnDataSource(data=dict(x=xs, y=ys, id=node_ids, dna=dna_list))
        edges_source = ColumnDataSource(data=dict(xs=edge_xs, ys=edge_ys))

        p = figure(title="Evolution Tree (drag nodes to move)", active_scroll="wheel_zoom", match_aspect=True)
        # 不加入全域的 HoverTool()，否則會對 edges/patches 也觸發 tooltip
        # 之後針對 centers (circle renderer `r`) 加上專屬的 HoverTool (見下方)
        p.multi_line("xs", "ys", source=edges_source, color="gray", line_width=1)
        p.patches("xs", "ys", source=patches_source, fill_alpha=0.6, fill_color="navy", line_color="black")
        r = p.circle("x", "y", source=centers_source, radius=0.1, color="red")
        hover = HoverTool(tooltips=[("id", "@id"), ("dna", "@dna")], renderers=[r])
        p.add_tools(hover)
        draw_tool = PointDrawTool(renderers=[r], add=False)  # type: ignore
        p.add_tools(draw_tool)
        p.toolbar.active_drag = draw_tool

        js_code = """
        const data = centers_source.data;
        const px = patches_source.data;
        const ed = edges_source.data;
        const n = data['x'].length;
        const node_size = __NODE_SIZE__;
        const new_xs = [];
        const new_ys = [];
        for (let i=0;i<n;i++){
            const cx = data['x'][i];
            const cy = data['y'][i];
            const dna = data['dna'][i];
            const vx = [];
            const vy = [];
            for (let j=0;j<6;j++){
                const angle = Math.PI/2 - j*(2*Math.PI/6);
                const r = Math.max(0, Math.min(1, dna[j]))*node_size;
                vx.push(cx + r*Math.cos(angle));
                vy.push(cy + r*Math.sin(angle));
            }
            new_xs.push(vx);
            new_ys.push(vy);
        }
        px['xs'] = new_xs;
        px['ys'] = new_ys;
        const old_xs = ed['xs'];
        const old_ys = ed['ys'];
        const new_exs = [];
        const new_eys = [];
        for (let k=0;k<old_xs.length;k++){
            let x0 = old_xs[k][0];
            let y0 = old_ys[k][0];
            let x1 = old_xs[k][1];
            let y1 = old_ys[k][1];
            let idx0 = 0, idx1 = 0, min0=1e9, min1=1e9;
            for (let i=0;i<n;i++){
                const dx0 = Math.abs(data['x'][i]-x0) + Math.abs(data['y'][i]-y0);
                if (dx0 < min0){ min0 = dx0; idx0 = i; }
                const dx1 = Math.abs(data['x'][i]-x1) + Math.abs(data['y'][i]-y1);
                if (dx1 < min1){ min1 = dx1; idx1 = i; }
            }
            new_exs.push([data['x'][idx0], data['x'][idx1]]);
            new_eys.push([data['y'][idx0], data['y'][idx1]]);
        }
        ed['xs'] = new_exs;
        ed['ys'] = new_eys;
        patches_source.change.emit();
        edges_source.change.emit();
        """
        js_code = js_code.replace("__NODE_SIZE__", str(args_node_size))
        callback = CustomJS(args=dict(centers_source=centers_source, patches_source=patches_source, edges_source=edges_source), code=js_code)
        centers_source.js_on_change("data", callback)

        output_file(args_out, title="Evolution Tree")
        save(p)
        print(f"Interactive HTML 已產生: {args_out}")
        return


if __name__ == "__main__":
    main()
