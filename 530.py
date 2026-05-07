def map(func, sequence):
    list = []
    for i in sequence:
        list.append(func(i))
    return list