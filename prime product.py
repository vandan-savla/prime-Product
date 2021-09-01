def primeproduct(m):
    l = []
    # if m>0:
    for i in range(2, m):
            if m % i == 0:
                l += [i]
    if len(l) == 2:
        if l[0]*l[1] == m:
            if l[1]%l[0] == 0:
                return False
            else:
                return True
        elif len(l) == 1:
            if l[0]*l[0] == m:
                return True
            return False
        else:
            return False
