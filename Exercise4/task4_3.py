﻿#Пользователь вводит любое целое положительное число (сделать проверку). Программа должна просуммировать 
#все числа от 1 до введенного пользователем числа (не включая его).
try:
    x = int(input("Введите любое целое положительное число "))
    if x < 0:
        print("Это не положительное число!")
    else:
        sum = 0
        while x > 0:
            x -= 1
            sum = sum + x
        print('Сумма равна {:d}'.format(sum))
except:
    print("Некорректные данные!")
    


    