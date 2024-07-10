# 載入模組
from random import randint as ri
from time import time
from typing import Callable


def t(f: Callable) -> Callable:
    def t1(l: list[int]) -> float | int:
        s = time()
        result = f(l.copy())
        e = time()
        ti = e - s
        if result == ans:
            return ti
        else:
            return -1

    return t1


# 氣泡排序法
@t
def bubble_sort(l: list[int]) -> list[int]:
    for i in range(len(l)):
        for n in range(len(l) - i - 1):
            if l[n] > l[n + 1]:
                l[n], l[n + 1] = l[n + 1], l[n]
    return l


# 雞尾酒排序法
@t
def cocktail_sort(l: list[int]) -> list[int]:
    t = len(l) - 1
    b = 0
    while b < t:
        for n in range(b, t):
            if l[n] > l[n + 1]:
                l[n], l[n + 1] = l[n + 1], l[n]
        t -= 1
        for n in range(t, b, -1):
            if l[n] < l[n - 1]:
                l[n], l[n - 1] = l[n - 1], l[n]
        b += 1
    return l


# 選擇排序法
@t
def selection_sort(l: list[int]) -> list[int]:
    for i in range(len(l) - 1):
        x = i
        for j in range(i, len(l)):
            if l[j] < l[x]:
                x = j
        l[i], l[x] = l[x], l[i]
    return l


# 插入排序法(error)
@t
def insertion_sort(l: list[int]) -> list[int]:
    for i in range(1, len(l)):
        for j in range(i, 0, -1):
            if l[j] >= l[j - 1]:
                break
            l[j], l[j - 1] = l[j - 1], l[j]
    return l


# 合併排序法
def merge_sort(l: list[int]) -> list[int]:
    if len(l) <= 1:
        return l
    rl = merge_sort(l[: len(l) // 2])
    ll = merge_sort(l[len(l) // 2 :])
    t = []
    rp, lp = 0, 0
    for _ in range(len(l)):
        if rl[rp] < ll[lp]:
            t.append(rl[rp])
            rp += 1
        else:
            t.append(ll[lp])
            lp += 1
        if rp == len(rl):
            t.extend(ll[lp:])
            break
        if lp == len(ll):
            t.extend(rl[rp:])
            break
    return t


l = []
for _ in range(10000):
    l.append(ri(0, 99))
ans = sorted(l)

bubble_time = bubble_sort(l)
cocktail_time = cocktail_sort(l)
selection_time = selection_sort(l)
merge_time = t(merge_sort)(l)
insertion_time = insertion_sort(l)

print("氣泡排序法所花時間:", bubble_time)
print("雞尾酒排序法所花時間:", cocktail_time)
print("選擇排序法所花時間:", selection_time)
print("合併排序法所花時間:", merge_time)
print("插入排序法所花時間:", insertion_time)
