def digit_sum(x):
    s = 0
    for digit in str(x):
        s += int(digit)
    return s
def kopaytma(x):
    s = 1
    for digit in str(x):
        s *= int(digit)
    return s
for i in range(100, 1000):
    if kopaytma(i) % digit_sum(i) == 0:
        print(i)