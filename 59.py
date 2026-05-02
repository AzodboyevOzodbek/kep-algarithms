def max_2(*args):
    max_1 = max(args)
    args = list(args)
    args.remove(max_1)
    return max(args)