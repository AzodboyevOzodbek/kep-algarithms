for n in range(1000, 10000):
    s = str(n)
    if s[0] != '0':
        rev_s = s[::-1]
        if rev_s[0] != '0':
            if int(rev_s) == 4 * n:
                print(n)
                break