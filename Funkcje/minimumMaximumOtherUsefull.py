def maximum(a, b, c):
    if (a >= b) and (a >= c):
        largest = a
    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c
    return largest

def minimum(a, b, c):
    if (a <= b) and (a <= c):
        minimal = a
    elif (b <= a) and (b <= c):
        minimal = b
    else:
        minimal = c
    return minimal
