def bino(n, r):
    if r == 0 or n == r:
        return 1
    else:
        return bino(n-1, r-1)+bino(n-1, r)


k = bino(5, 2)
print(k)
