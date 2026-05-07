# def map_square(sequence):
#     new = []
#     for n in sequence:
#         new.append(n * n)
#     return new
# print(map_square([1, 2, 3, 4, 5]))

def map_square(sequence):
    return map(lambda n: n * n, sequence)