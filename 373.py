n = int(input())
royhat = list(map(int, input().split()))
# print(max(royhat))
min_value = royhat[0]
for n in royhat:
    if n < min_value:
        min_value = n
print(min_value)