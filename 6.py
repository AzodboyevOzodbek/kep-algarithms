import math

n = int(input())
root_n = math.isqrt(n)
result = 0
for k in range(1, root_n):
    result += k * ((k + 1)**2 - k**2)
result += root_n * (n - root_n**2 + 1)
print(result)