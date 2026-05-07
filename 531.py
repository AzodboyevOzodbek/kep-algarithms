
def filter_odd(sequence):
    return filter(lambda n: n % 2 == 0, sequence)
print(list(filter_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))