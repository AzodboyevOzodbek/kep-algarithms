def even_index_or_value(lst):
    result = []
    
    for i in range(len(lst)):
        if i % 2 == 0 or lst[i] % 2 == 0:
            result.append(lst[i])
    
    return result