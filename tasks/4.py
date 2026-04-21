def month_to_asason(a):
    if a <= 2 or a == 12:
        return("Qish")
    elif a >=3 or a <=5:
        return("Bahor")
    elif a >= 6 or a <=8:
        return("Yoz")
    elif a >=9 or a <=11:
        return("Kuz")
print(month_to_asason(1))