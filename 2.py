from random import randint
import time

def bin_search(a, n):
    start_time = time.time()
    lis = [randint(-10, 10) for i in range(n)]
    lis2 = sorted(lis)
    mid = len(lis2) // 2
    low = 0
    high = len(lis2) - 1
    while lis2[mid] != a and low <= high:
        if a > lis2[mid]:
            low = mid + 1
        else:
            high = mid - 1
            mid = (low + high) // 2
 
    if low > high:
        print("Нет значения")
    else:
        print(mid)
