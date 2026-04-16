n = int(input())

tub = [True] * (n + 1)
tub[0] = tub[1] = False

for i in range(2, int(n ** 0.5) + 1):
    if tub[i]:
        for j in range(i * i, n + 1, i):
            tub[j] = False

for i in range(2, n + 1):
    if tub[i]:
        print(i, end=" ")