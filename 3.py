def bsearch(lis, st, en, a):
    if (en < st):
        return None
    else:
        m = st + ((en - st) // 2)
        if lis[m] > a:
            return bsearch(lis, st, m - 1, a)
        elif a[m] < key:
            return bsearch(lis, m + 1, en, a)
        else:
            return m
