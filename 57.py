def sum_digits(n):
    s = 0
    for i in str(n):
        s += int(i)
    return s