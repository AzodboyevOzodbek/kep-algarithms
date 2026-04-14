n = int(input())
p = 1
s = 0

for i in range(1, n + 1):
    s += i
    p *= s

print(p)
