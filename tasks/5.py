a = [1,3,4,5,6,7,12,15,29,19,17]
s = 0
for n in a:
    if n % 3 == 0 and n < 30:
        print(n)
    else:
        s += n
print(s)