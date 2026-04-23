n = int(input())
birlar_soni = 0
while n > 0: 
    ohirgi_raqam = n % 10  
    if ohirgi_raqam == 1:
        birlar_soni += 1

    n = n // 10  

print(birlar_soni)