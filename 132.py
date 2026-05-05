def argv_int(*args):
    c = 0
    for arg in args:
        if type(arg) == int:
            c += 1
        return c