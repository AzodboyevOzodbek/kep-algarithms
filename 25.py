
import math

a = int(input())
b = int(input())

D = a*a - 4*b

x = (a + math.sqrt(D)) / 2
y = (a - math.sqrt(D)) / 2

print(F"{x} {y}")