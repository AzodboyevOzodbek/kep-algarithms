a = int(input())
b = int(input())
s = 0
if a > b:
    a, b = b, a
for n in range(a, b + 1):
    if n % 4 == 0 :
        s += 1
print(s)