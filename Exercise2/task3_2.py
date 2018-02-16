#Определить четверть координатной плоскости по координатам x и y. Применить минимум два разных подхода в #указании условий.
x = int(input("Координата Х = "))
y = int(input("Координата Y = "))

if not y or not x:
    print("Точка на оси")
else:
    if y > 0:
        if x > 0:
            print("I четверть")
        else:
            print("II четверть")
    else:  
        if x > 0:
            print("VI четверть")
        else:
            print("III четверть")  

if not y or not x:
    print("Точка на оси")
elif y > 0 < x:
    print("I четверть")
elif y > 0 > x:
    print("II четверть")
elif y < 0 > x:
    print("III четверть")
else:
    print("VI четверть")

