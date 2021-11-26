from random import randint
import time

def lin_search(a, n):
    start_time = time.time()
    lis = [randint(-10, 10) for i in range(n)]
    lis2 = sorted(lis)
    for i in range (len(lis2)):
        if lis2[i] == a:
            print(i)
            break
        elif a not in lis2:
            print('Такого числа нет')
            break
    print('Время выполнения %s' % (time.time() - start_time))
# 10 - 0.05343508720397949
# 100 - 0.054341793060302734
# 10^3 - 0.05568885803222656
# 10^6 - 
