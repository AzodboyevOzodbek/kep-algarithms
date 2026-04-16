sonlar = []
for number in range(1000, 10000):
    d1 = number // 1000
    d2 = (number // 100) % 10
    d3 = (number // 10) % 10
    d4 = number % 10
    
    raqamlar_yigindisi = d1 + d2 + d3 + d4
    
    if raqamlar_yigindisi % 2 == 0:
        sonlar.append(str(number))

print((sonlar))