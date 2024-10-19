from random import randint as ri


def adjust(arr: list[int], i: int, n: int):
    child = 2 * i
    item = arr[i - 1]
    while child <= n:
        if child < n and arr[child - 1] < arr[child]:
            child += 1
        if item >= arr[child - 1]:
            break
        arr[(child // 2) - 1] = arr[child - 1]
        child *= 2
    arr[int(child // 2) - 1] = item


def heapify(arr: list[int], n: int):
    for i in range(int(n // 2), 0, -1):
        adjust(arr, i, len(arr))


def heapSort(arr: list[int], n: int):
    heapify(arr, len(arr))
    for i in range(n, 1, -1):
        arr[i - 1], arr[0] = arr[0], arr[i - 1]
        adjust(arr, 1, i - 1)
    return arr


arr = [ri(0, 99) for _ in range(10000)]
print(arr)
heapSort(arr, len(arr))
print(arr)
