﻿#Заполнить список из десяти элементов произвольными целочисленными значениями. 
#Затем четные элементы расположить в начале списка, нечетные - в конце.

try:
    x = int(input("Введите трёхзначное число "))
    if len(str(x))!=3:
        print('Вы ввели не трёхзначное число')
    else:
        p = 1
        s = str(x)
        
        #Вариант 1
        for i in s:            
            p = p * int(i)
        print('1. Произведение равно {:d}'.format(p)) 

        #Вариант 2
        p = 1
        for i in range(len(s)):
            p = p * int(s[i])
        print('2. Произведение равно {:d}'.format(p)) 
except:
    print("Некорректные данные")