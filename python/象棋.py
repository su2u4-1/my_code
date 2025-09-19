"""
中國象棋模擬程式
功能：
- 棋盤類別
- 棋子類別
- 移動規則
- 合法走子判斷
- 狀態生成（可用於計算狀態數）
"""

from typing import Literal, Optional


BOARD_ROWS = 10
BOARD_COLS = 9


class Piece:
    def __init__(self, name: str, color: Literal["red", "black"], pos: tuple[int, int]):
        self.name = name  # 棋子名稱
        self.color = color  # 'red' 或 'black'
        self.pos = pos  # (row, col)

    def __repr__(self):
        return f"{self.color[0].upper()}{self.name}@{self.pos}"


class Board:
    def __init__(self):
        self.grid: list[list[Optional[Piece]]] = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
        self.pieces: list[Piece] = []
        self.init_pieces()

    def init_pieces(self):
        # 紅方
        red_init = [
            ("車", (9, 0)),
            ("馬", (9, 1)),
            ("相", (9, 2)),
            ("仕", (9, 3)),
            ("帥", (9, 4)),
            ("仕", (9, 5)),
            ("相", (9, 6)),
            ("馬", (9, 7)),
            ("車", (9, 8)),
            ("炮", (7, 1)),
            ("炮", (7, 7)),
            ("兵", (6, 0)),
            ("兵", (6, 2)),
            ("兵", (6, 4)),
            ("兵", (6, 6)),
            ("兵", (6, 8)),
        ]
        # 黑方
        black_init = [
            ("車", (0, 0)),
            ("馬", (0, 1)),
            ("象", (0, 2)),
            ("士", (0, 3)),
            ("將", (0, 4)),
            ("士", (0, 5)),
            ("象", (0, 6)),
            ("馬", (0, 7)),
            ("車", (0, 8)),
            ("炮", (2, 1)),
            ("炮", (2, 7)),
            ("卒", (3, 0)),
            ("卒", (3, 2)),
            ("卒", (3, 4)),
            ("卒", (3, 6)),
            ("卒", (3, 8)),
        ]
        for name, pos in red_init:
            p = Piece(name, "red", pos)
            self.pieces.append(p)
            self.grid[pos[0]][pos[1]] = p
        for name, pos in black_init:
            p = Piece(name, "black", pos)
            self.pieces.append(p)
            self.grid[pos[0]][pos[1]] = p

    def move_piece(self, piece: Piece, new_pos: tuple[int, int]) -> bool:
        old_r, old_c = piece.pos
        new_r, new_c = new_pos
        # 檢查新位置是否有己方棋子
        target = self.grid[new_r][new_c]
        if target and target.color == piece.color:
            return False
        # 合法性判斷
        if not self.is_legal_move(piece, new_pos):
            return False
        # 執行移動
        self.grid[old_r][old_c] = None
        if target:
            self.pieces.remove(target)
        piece.pos = new_pos
        self.grid[new_r][new_c] = piece
        return True

    def is_legal_move(self, piece: Piece, new_pos: tuple[int, int]) -> bool:
        # 根據棋子種類判斷
        r, c = piece.pos
        nr, nc = new_pos
        dr, dc = nr - r, nc - c
        name = piece.name
        color = piece.color
        # 帥/將
        if name in ["帥", "將"]:
            if nc < 3 or nc > 5:
                return False
            if color == "red" and nr < 7:
                return False
            if color == "black" and nr > 2:
                return False
            if abs(dr) + abs(dc) != 1:
                return False
            return True
        # 士/仕
        if name in ["士", "仕"]:
            if nc < 3 or nc > 5:
                return False
            if color == "red" and nr < 7:
                return False
            if color == "black" and nr > 2:
                return False
            if abs(dr) == 1 and abs(dc) == 1:
                return True
            return False
        # 象/相
        if name in ["象", "相"]:
            if color == "red" and nr < 5:
                return False
            if color == "black" and nr > 4:
                return False
            if abs(dr) == 2 and abs(dc) == 2:
                # 檢查象眼
                eye_r = r + dr // 2
                eye_c = c + dc // 2
                if self.grid[eye_r][eye_c] is None:
                    return True
            return False
        # 馬
        if name == "馬":
            if (abs(dr), abs(dc)) in [(2, 1), (1, 2)]:
                # 檢查蹩馬腿
                if abs(dr) == 2:
                    leg_r = r + dr // 2
                    leg_c = c
                else:
                    leg_r = r
                    leg_c = c + dc // 2
                if self.grid[leg_r][leg_c] is None:
                    return True
            return False
        # 車
        if name == "車":
            if dr == 0 and dc != 0:
                step = 1 if dc > 0 else -1
                for i in range(c + step, nc, step):
                    if self.grid[r][i]:
                        return False
                return True
            if dc == 0 and dr != 0:
                step = 1 if dr > 0 else -1
                for i in range(r + step, nr, step):
                    if self.grid[i][c]:
                        return False
                return True
            return False
        # 炮
        if name == "炮":
            if dr == 0 and dc != 0:
                step = 1 if dc > 0 else -1
                count = 0
                for i in range(c + step, nc, step):
                    if self.grid[r][i]:
                        count += 1
                target = self.grid[nr][nc]
                if target:
                    return count == 1
                else:
                    return count == 0
            if dc == 0 and dr != 0:
                step = 1 if dr > 0 else -1
                count = 0
                for i in range(r + step, nr, step):
                    if self.grid[i][c]:
                        count += 1
                target = self.grid[nr][nc]
                if target:
                    return count == 1
                else:
                    return count == 0
            return False
        # 兵/卒
        if name in ["兵", "卒"]:
            if color == "red":
                if r > 4:
                    # 未過河只能直走
                    if dr == -1 and dc == 0:
                        return True
                else:
                    # 過河可左右
                    if (dr, dc) in [(-1, 0), (0, -1), (0, 1)]:
                        return True
            if color == "black":
                if r < 5:
                    if dr == 1 and dc == 0:
                        return True
                else:
                    if (dr, dc) in [(1, 0), (0, -1), (0, 1)]:
                        return True
            return False
        return False

    def print_board(self):
        for r in range(BOARD_ROWS):
            row: list[str] = []
            for c in range(BOARD_COLS):
                p = self.grid[r][c]
                if p:
                    row.append(p.name if p.color == "red" else p.name)
                else:
                    row.append(" ·")
            print(" ".join(row))
        print()

    def get_all_moves(self, color: Literal["red", "black"]) -> list[tuple[Piece, tuple[int, int]]]:
        moves: list[tuple[Piece, tuple[int, int]]] = []
        for p in self.pieces:
            if p.color != color:
                continue
            # r, c = p.pos
            for nr in range(BOARD_ROWS):
                for nc in range(BOARD_COLS):
                    if self.is_legal_move(p, (nr, nc)):
                        moves.append((p, (nr, nc)))
        return moves


# 狀態計算範例
if __name__ == "__main__":
    import copy

    def board_state_hash(board: Board) -> str:
        # 以所有棋子的位置和種類編碼
        return "|".join(sorted(f"{p.color[0]}{p.name}{p.pos[0]},{p.pos[1]}" for p in board.pieces))

    def dfs(board: Board, turn: Literal["black", "red"], depth: int, max_depth: int, states: set[str]):
        if depth == max_depth:
            states.add(board_state_hash(board))
            return
        moves = board.get_all_moves(turn)
        for piece, new_pos in moves:
            # 儲存原始狀態
            old_pos = piece.pos
            # target = board.grid[new_pos[0]][new_pos[1]]
            # 深複製棋盤
            board_copy = copy.deepcopy(board)
            # 嘗試走子
            moved = board_copy.move_piece(next(p for p in board_copy.pieces if p.name == piece.name and p.color == piece.color and p.pos == old_pos), new_pos)
            if moved:
                dfs(board_copy, "red" if turn == "black" else "black", depth + 1, max_depth, states)

    n = 3
    board = Board()
    states: set[str] = set()
    dfs(board, "black", 0, n, states)  # 黑方先手，雙方各走n步
    print(f"黑方先手，雙方共走{n}步後的狀態數: {len(states)}")
