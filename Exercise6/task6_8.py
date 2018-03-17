#Заполнить список из десяти элементов произвольными целочисленными значениями. 
#Затем четные элементы расположить в начале списка, нечетные - в конце.

import random
i = 0
l1 =[random.randint(-100,100) for i in range(0, 10)]
print('Список {}'.format(l1))

l2 =[]
i = 0
for i in range(len(l1)):     
    if (i + 1) % 2 == 0:        
        l2.insert((i + 1) // 2 - 1, l1[i])
    else:
        l2.append(l1[i])
print('Список {}'.format(l2))      