# def map_divisors_count(sequence):
    # return map(lambda n: len(list(filter(lambda x: n % x == 0, range(1, n + 1)))), sequence)
def divisors_count(son):
    count = 0
    for i in range(1, son + 1):
        if son % i == 0:
            count += 1
    return count
def map_divisors_count(sequence):
    return map(divisors_count, sequence)
# print(list(map_divisors_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
