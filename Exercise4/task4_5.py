#Найдите количество четных цифр введёного натурального числа.

x = str(input("Введите натуральное число "))
a = tuple(x)
m = 0;

for i in range(0, len(a)):
    if int(a[i])%2 == 0:
        m = m + int(a[i]) 

print('{:d}'.format(m))
 