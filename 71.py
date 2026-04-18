n = input()
s = 0
s1 = 0
n1 = n[0:3]
n2 = n[3:6]
for i in n1:
    s += int(i)
for a in n2:
    s1 += int(a)
if s == s1:
    print("True")
else:
    print("False")  
