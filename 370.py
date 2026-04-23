n = int(input())
royhat = list(map(int, input().split()))
for i in range(1, n + 1 , 2):
    print(royhat[i-1], end = " ")
