# n = int(input())
# is_prime = True

# if n < 2:
#     is_prime = False
# else:
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             is_prime = False
#             break

# if is_prime:
#     print("Yes")
# else:
#     print("No")

# 2 - usul
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
if is_prime(n):
    print("Yes")
else:
    print("No")
