n = int(input())
divisors = []
for i in range(1, n):
    if n % i != 0:
        divisors.append(i)
sorted(divisors)
print(divisors[0])