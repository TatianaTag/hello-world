﻿#Заполнить список из шести элементов квадратными корнями произвольныз целочисленныз значений. #Вывести список на экран через запятую.

import random
i = 0
l1 = []
while i < 6:
    l1.append(random.randint(-10, 10)**2)
    i += 1
print('Список {}'.format(l1))

i = 0
while i < 6:
    print(l1[i], end = ',' if i!=5 else '\n')
    i += 1