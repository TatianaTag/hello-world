﻿#Задача: В школе решили набрать три новых математических класса. Так как занятия по математике у них #проходят в одно и то же время, было решено выделить кабинет для каждого класса и купить в них новые #парты. За каждой партой может сидеть не больше двух учеников. Известно количество учащихся в каждом из #трёх классов. Сколько всего нужно закупить парт чтобы их хватило на всех учеников? Программа получает #на #вход три натуральных числа: количество учащихся в каждом из трех классов.

pupil1 = int(input("Pupil1 = "))
pupil2 = int(input("Pupil2 = "))
pupil3 = int(input("Pupil3 = "))
count = pupil1 // 2 + pupil1 % 2 + pupil2 // 2 + pupil2 % 2 + pupil3 // 2 + pupil3 % 2
print('Количество парт = {:d}'.format(count))
 

