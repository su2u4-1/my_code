# 載入模組
from random import randint as ri
from time import time


# 氣泡排序法
def bubble_sort(l):
    for i in range(len(l)):
        for n in range(len(l) - i - 1):
            if l[n] > l[n + 1]:
                l[n], l[n + 1] = l[n + 1], l[n]
    return l


# 雞尾酒排序法
def cocktail_sort(l):
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
def selection_sort(l):
    for i in range(len(l) - 1):
        x = i
        for j in range(i, len(l)):
            if l[j] < l[x]:
                x = j
        l[i], l[x] = l[x], l[i]
    return l


# 插入排序法
def insertion_sort(l):
    for i in range(1, len(l)):
        for j in range(i, -1, -1):
            if l[i] >= l[j]:
                break
        else:
            j -= 1
        a = l.pop(i)
        l.insert(j + 1, a)
    return l


l = []
for _ in range(10000):
    l.append(ri(0, 99))

s = time()
bubble = bubble_sort(l.copy())
e = time()
bubble_time = e - s

s = time()
cocktail = cocktail_sort(l.copy())
e = time()
cocktail_time = e - s

s = time()
selection = selection_sort(l.copy())
e = time()
selection_time = e - s

s = time()
insertion = insertion_sort(l.copy())
e = time()
insertion_time = e - s

# print("原始列表:",l)
# print("氣泡排序法結過:",bubble)
# print("雞尾酒排序法結過:",cocktail)
# print("選擇排序法結過:",selection)
# print("插入排序法結過:",insertion)
print("氣泡排序法所花時間:", bubble_time)
print("雞尾酒排序法所花時間:", cocktail_time)
print("選擇排序法所花時間:", selection_time)
print("插入排序法所花時間:", insertion_time)
