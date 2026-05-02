n = int(input())
s,i = 0,0
# for i in range(n):
#     a = int(input())
#     if a % 2 == 0:
#         s += a
# print(s)

while i < n:
    a = int(input())
    if a % 2 == 0:
        s += a
    i += 1
print(s)