def digit_sum(x):
    s = 0
    for digit in str(x):
        s += int(digit)
    return s