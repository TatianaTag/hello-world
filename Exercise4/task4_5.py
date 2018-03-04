#Найдите количество четных цифр введёного натурального числа.

try:
    x = int(input("Введите натуральное число "))
    if x < 0:
        print("Вы ввели отрицательное число")
    else:
        m = 0;
        a = str(x)

        for i in range(0, len(a)):
            if int(a[i])%2 == 0:
                m = m + int(a[i]) 

        print('{:d}'.format(m))
except:
    print("Некорректные данные")
 